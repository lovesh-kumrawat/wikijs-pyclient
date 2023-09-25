import json
from enum import Enum
from datetime import date
from dataclasses import asdict, is_dataclass
from typing import Callable, Union, get_args, get_origin, Any

from .regulators import var_mapper, WikiJSExceptions, PayloadTemplate


class GqlBase:
    
    @staticmethod
    def type_stringify(generic_type, optional = False) -> str:

        if generic_type == str: return f"String{'' if optional else '!'}"
        if generic_type == int: return f"Int{'' if optional else '!'}"
        if generic_type == bool: return f"Boolean{'' if optional else '!'}"
        if generic_type == date: return f"Date{'' if optional else '!'}"

        try:
            if issubclass(generic_type, Enum):
                return f"{generic_type.__name__}{'' if optional else '!'}"
        
        except TypeError: ...

        origin = get_origin(generic_type)
        args = get_args(generic_type)
        
        if origin == Union:
            return GqlBase.type_stringify(args[0], optional=True) + ("" if args[1] == type(None) else "!")
        
        if origin == list:
            return "[" + GqlBase.type_stringify(args[0], optional=True) + "]" + ("" if optional else "!")
        
        return f"{generic_type.__name__}"
    
    @staticmethod
    def response_stringify(generic_class) -> str:

        if generic_class in (int, str, bool, date): return ""
        if get_origin(generic_class) in (list, Union): return GqlBase.response_stringify(get_args(generic_class)[0])
        if issubclass(generic_class, Enum): return ""

        attrs = []
        for attr, _type in generic_class.__annotations__.items():
            
            attr = var_mapper.get(attr, attr)
            
            response = GqlBase.response_stringify(_type)
            if response: attrs.append(f"{attr} {{ {response} }}")
            else: attrs.append(attr)
        
        return ", ".join(attrs)
    
    @staticmethod
    def refined_value(value: Any) -> Any:

        if isinstance(value, list): return [GqlBase.refined_value(item) for item in value]
        if is_dataclass(value): return asdict(value)
        return value
    
    def execute(
            self,
            *,
            payload: PayloadTemplate,
            response_class: Any,
            param_hints: dict[str, type],
            params: dict[str, Any]
        ) -> dict[str, Any]:

        param_fields: list[str] = []
        reference_fields: list[str] = []
        
        for name, _type in param_hints.items():
            
            value = GqlBase.refined_value(value.value if isinstance(value:=params.get(name), Enum) else value)
            
            if name in var_mapper:
                del params[name]
                name = var_mapper[name]

            if value != None:
                
                params[name] = value
                ref_name = "$" + name
                _type = GqlBase.type_stringify(_type)
                
                reference_fields.append(f"{ref_name}: {_type}")
                param_fields.append(f"{name}: {ref_name}")
        
        gql_query = payload.format(
            reference=', '.join(reference_fields),
            params=', '.join(param_fields),
            response=GqlBase.response_stringify(response_class)
        )
        
        response = self.gql_post(gql_query, params)
        return response


class Response:

    def __init__(self, response_class: Any, response_json: dict[str, Any]):
        
        self.response_json: dict[str, Any] = response_json
        self.response_instance: response_class = None
        self.response_class: Any = response_class
    
    def __repr__(self) -> str: return json.dumps(self.response_json, indent=4)
    
    @classmethod
    def class_response(cls, generic_class, response: dict[str: Any]) -> Any:
        
        if response is None or generic_class in (int, str, bool, date): return response

        origin = get_origin(generic_class)
        args = get_args(generic_class)

        if origin == Union: return cls.class_response(args[0], response)
        if origin == list: return [cls.class_response(args[0], item) for item in response]
        if issubclass(generic_class, Enum): return getattr(getattr(generic_class, response), "value")
        
        return generic_class(
            **{
                attr: cls.class_response(_type, response[var_mapper.get(attr, attr)])
                for attr, _type in generic_class.__annotations__.items()
            }
        )
    
    def json(self) -> dict[str, Any]:
        return self.response_json

    def instance(self) -> Any:
        
        if self.response_instance == None:
            self.response_instance = self.class_response(self.response_class, self.response_json)
        
        return self.response_instance

    @classmethod
    def verified(cls, response_class: Any, response_json: dict[str, Any] | list[Any], *, _json: bool = False):
        
        if (
            getattr(response_json, 'get', False) and
            response_json.get("responseResult") and
            not response_json.get("responseResult")["succeeded"]
        ):
            raise WikiJSExceptions(                         #noqa: IICE (Immediately Invoked Class Expression) was used
                response_json['responseResult']['slug'],
                response_json['responseResult']['message']
            )
        
        return response_json if _json else cls(response_class, response_json)
    
    @classmethod
    def response(cls, response_class: Any, *, action: str, resource: str, method: str):
        def decorator(func: Callable):
            def wrapper(self, **params):
                
                # For some internal requirements
                _json = params.pop("_json", False)

                payload = PayloadTemplate()
                payload.format(action=action, resource=resource, method=method)

                response = self.execute(
                    payload = payload,
                    response_class = response_class,
                    param_hints = func.__annotations__,
                    params = func(self, **params) or params
                )

                return cls.verified(response_class, response[resource][method], _json = _json)
            return wrapper
        return decorator

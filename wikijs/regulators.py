"""
Configurations which regulates the changes
"""

from string import Template


# Variables mapping between Python & WikiJS
var_mapper: dict[str, str] = {
    "pass_": "pass",
    "input_": "input"
}


class PayloadTemplate:

    def __init__(self) -> None:

        self.query = """
            $action $reference {
                $resource {
                    $method $params
                        $response
                }
            }
        """
    
    def __repr__(self) -> str:
        return self.query
    
    def format(
            self,
            *,
            action: str = None,
            resource: str = None,
            method: str = None,
            reference: str = None,
            params: str = None,
            response: str = None
        ) -> str:

        if reference: reference = f"({reference})"
        if params: params = f"({params})"
        if response: response = f"{{{response}}}"

        self.query = Template(self.query).safe_substitute(
            **{
                var: val
                for var, val in locals().items()
                if val not in (None, self)
            }
        )

        return self.query
    
    def get_query(self) -> str:
        return self.query


@lambda _: _()
class WikiJSExceptions:
    
    """
    Dynamic WikiJS exceptions
    """

    def __init__(self) -> None:
        self.exceptions: dict[str, type] = {}
    
    def __call__(self, exception: str, message: str = None) -> Exception:

        exception = self.trim(exception)
        exc = self.exceptions.setdefault(exception, type(exception, (Exception,), {}))
        return exc(message) if message else exc
    
    @staticmethod
    def trim(exception: str) -> type:
        return exception.rsplit(".", 1)[-1]

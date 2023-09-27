from datetime import date
from typing import Optional
from dataclasses import dataclass

from ..responses import ResponseStatus, KeyValuePair, KeyValuePairInput


@dataclass(kw_only=True)
class AuthenticationStrategy:
    key: str
    props: Optional[list[KeyValuePair]] = None
    title: str
    description: Optional[str] = None
    isAvailable: Optional[bool] = None
    useForm: bool
    usernameType: Optional[str] = None
    logo: Optional[str] = None
    color: Optional[str] = None
    website: Optional[str] = None
    icon: Optional[str] = None


@dataclass(kw_only=True)
class AuthenticationActiveStrategy:
    key: str
    strategy: AuthenticationStrategy
    displayName: str
    order: int
    isEnabled: bool
    config: Optional[list[KeyValuePair]] = None
    selfRegistration: bool
    domainWhitelist: list[str]
    autoEnrollGroups: list[int]


@dataclass(kw_only=True)
class AuthenticationLoginResponse:
    responseResult: Optional[ResponseStatus] = None
    jwt: Optional[str] = None
    mustChangePwd: Optional[bool] = None
    mustProvideTFA: Optional[bool] = None
    mustSetupTFA: Optional[bool] = None
    continuationToken: Optional[str] = None
    redirect: Optional[str] = None
    tfaQRImage: Optional[str] = None


@dataclass(kw_only=True)
class AuthenticationRegisterResponse:
    responseResult: Optional[ResponseStatus] = None
    jwt: Optional[str] = None


@dataclass(kw_only=True)
class AuthenticationStrategyInput:
    key: str
    strategyKey: str
    config: Optional[list[KeyValuePairInput]] = None
    displayName: str
    order: int
    isEnabled: bool
    selfRegistration: bool
    domainWhitelist: list[str]
    autoEnrollGroups: list[int]


@dataclass(kw_only=True)
class AuthenticationApiKey:
    id: int
    name: str
    keyShort: str
    expiration: date
    createdAt: date
    updatedAt: date
    isRevoked: bool


@dataclass(kw_only=True)
class AuthenticationCreateApiKeyResponse:
    responseResult: Optional[ResponseStatus] = None
    key: Optional[str] = None

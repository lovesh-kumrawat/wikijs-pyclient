from typing import Optional
from dataclasses import dataclass

from .resources.pages import Page, PageSearchResult


@dataclass(kw_only=True)
class Translation:
    key: str
    value: str


# Generic Key Value Pair
@dataclass(kw_only=True)
class KeyValuePair:
    key: str
    value: str


# General Key Value Pair Input
@dataclass(kw_only=True)
class KeyValuePairInput:
    key: str
    value: str


# Mutation Status
@dataclass(kw_only=True)
class ResponseStatus:
    succeeded: bool
    errorCode: int
    slug: str
    message: Optional[str] = None


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
class AuthenticationCreateApiKeyResponse:
    responseResult: Optional[ResponseStatus] = None
    key: Optional[str] = None


@dataclass(kw_only=True)
class CommentCreateResponse:
    responseResult: Optional[ResponseStatus] = None
    id: Optional[int] = None


@dataclass(kw_only=True)
class CommentUpdateResponse:
    responseResult: Optional[ResponseStatus] = None
    render: Optional[str] = None


# Generic Mutation Response
@dataclass(kw_only=True)
class DefaultResponse:
    responseResult: Optional[ResponseStatus] = None


@dataclass(kw_only=True)
class PageResponse:
    responseResult: ResponseStatus
    page: Optional[Page] = None


@dataclass(kw_only=True)
class PageMigrationResponse:
    responseResult: ResponseStatus
    count: Optional[int] = None


@dataclass(kw_only=True)
class PageSearchResponse:
    results: list[PageSearchResult]
    suggestions: list[str]
    totalHits: int


@dataclass(kw_only=True)
class SystemImportUsersResponseFailed:
    provider: Optional[str] = None
    email: Optional[str] = None
    error: Optional[str] = None


@dataclass(kw_only=True)
class SystemImportUsersResponse:
    responseResult: Optional[ResponseStatus] = None
    usersCount: Optional[int] = None
    groupsCount: Optional[int] = None
    failed: Optional[list[SystemImportUsersResponseFailed]] = None


@dataclass(kw_only=True)
class UserTokenResponse:
    responseResult: ResponseStatus
    jwt: Optional[str] = None

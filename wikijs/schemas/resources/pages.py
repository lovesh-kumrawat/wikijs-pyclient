from enum import Enum
from datetime import date
from typing import Optional
from dataclasses import dataclass


class PageRuleMatch(Enum):
    START: str = "START"
    EXACT: str = "EXACT"
    END: str = "END"
    REGEX: str = "REGEX"
    TAG: str = "TAG"


@dataclass(kw_only=True)
class PageRule:
    id: str
    deny: bool
    match: PageRuleMatch
    roles: list[str]
    path: str
    locales: list[str]


@dataclass(kw_only=True)
class PageRuleInput:
    id: str
    deny: bool
    match: PageRuleMatch
    roles: list[str]
    path: str
    locales: list[str]


@dataclass(kw_only=True)
class PageTag:
    id: int
    tag: str
    title: Optional[str] = None
    createdAt: date
    updatedAt: date


@dataclass(kw_only=True)
class Page:
    id: int
    path: str
    hash: str
    title: str
    description: str
    isPrivate: bool
    isPublished: bool
    privateNS: Optional[str] = None
    publishStartDate: date
    publishEndDate: date
    tags: list[PageTag]
    content: str
    render: Optional[str] = None
    # toc: Optional[str] = None
    contentType: str
    createdAt: date
    updatedAt: date
    # editor: str
    # locale: str
    scriptCss: Optional[str] = None
    scriptJs: Optional[str] = None
    authorId: int
    authorName: str
    authorEmail: str
    creatorId: int
    creatorName: str
    creatorEmail: str


@dataclass(kw_only=True)
class PageHistory:
    versionId: int
    versionDate: date
    authorId: int
    authorName: str
    actionType: str
    valueBefore: Optional[str] = None
    valueAfter: Optional[str] = None


@dataclass(kw_only=True)
class PageVersion:
    action: str
    authorId: str
    authorName: str
    content: str
    contentType: str
    createdAt: date
    versionDate: date
    description: str
    editor: str
    isPrivate: bool
    isPublished: bool
    locale: str
    pageId: int
    path: str
    publishEndDate: date
    publishStartDate: date
    tags: list[str]
    title: str
    versionId: int


@dataclass(kw_only=True)
class PageHistoryResult:
    trail: Optional[list[PageHistory]] = None
    total: int


@dataclass(kw_only=True)
class PageSearchResult:
    id: str
    title: str
    description: str
    path: str
    locale: str


@dataclass(kw_only=True)
class PageSearchResponse:
    results: list[PageSearchResult]
    suggestions: list[str]
    totalHits: int


@dataclass(kw_only=True)
class PageListItem:
    id: int
    path: str
    locale: str
    title: Optional[str] = None
    description: Optional[str] = None
    contentType: str
    isPublished: bool
    isPrivate: bool
    privateNS: Optional[str] = None
    createdAt: date
    updatedAt: date
    tags: Optional[list[str]] = None


@dataclass(kw_only=True)
class PageTreeItem:
    id: int
    path: str
    depth: int
    title: str
    isPrivate: bool
    isFolder: bool
    privateNS: Optional[str] = None
    parent: Optional[int] = None
    pageId: Optional[int] = None
    locale: str


@dataclass(kw_only=True)
class PageLinkItem:
    id: int
    path: str
    title: str
    links: list[str]


@dataclass(kw_only=True)
class PageConflictLatest:
    id: int
    authorId: str
    authorName: str
    content: str
    createdAt: date
    description: str
    isPublished: bool
    locale: str
    path: str
    tags: Optional[list[str]] = None
    title: str
    updatedAt: date


class PageOrderBy(Enum):
    CREATED: str = "CREATED"
    ID: str = "ID"
    PATH: str = "PATH"
    TITLE: str = "TITLE"
    UPDATED: str = "UPDATED"


class PageOrderByDirection(Enum):
    ASC: str = "ASC"
    DESC: str = "DESC"


class PageTreeMode(Enum):
    FOLDERS: str = "FOLDERS"
    # PAGES: str = "PAGES"
    ALL: str = "ALL"

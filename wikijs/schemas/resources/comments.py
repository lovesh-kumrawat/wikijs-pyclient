from datetime import date
from typing import Optional
from dataclasses import dataclass

from ..responses import KeyValuePair, KeyValuePairInput


@dataclass(kw_only=True)
class CommentProvider:
    isEnabled: bool
    key: str
    title: str
    description: Optional[str] = None
    logo: Optional[str] = None
    website: Optional[str] = None
    isAvailable: Optional[bool] = None
    config: Optional[list[KeyValuePair]] = None


@dataclass(kw_only=True)
class CommentProviderInput:
    isEnabled: bool
    key: str
    config: Optional[list[KeyValuePairInput]] = None


@dataclass(kw_only=True)
class CommentPost:
    id: int
    content: str
    render: str
    authorId: int
    authorName: str
    authorEmail: str
    authorIP: str
    createdAt: date
    updatedAt: date

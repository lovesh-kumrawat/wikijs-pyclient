from enum import Enum
from datetime import date
from typing import Optional
from dataclasses import dataclass

from .users import User


class AssetKind(Enum):
    IMAGE: str = "IMAGE"
    BINARY: str = "BINARY"
    ALL: str = "ALL"


@dataclass(kw_only=True)
class AssetFolder:
    id: int
    slug: str
    name: Optional[str] = None


@dataclass(kw_only=True)
class AssetItem:
    id: int
    filename: str
    ext: str
    kind: AssetKind
    mime: str
    fileSize: int
    metadata: Optional[str] = None
    createdAt: date
    updatedAt: date
    folder: Optional[AssetFolder] = None
    author: Optional[User] = None

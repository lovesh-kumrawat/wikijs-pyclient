from enum import Enum
from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class NavigationItem:
    id: str
    kind: str
    label: Optional[str] = None
    icon: Optional[str] = None
    targetType: Optional[str] = None
    target: Optional[str] = None
    visibilityMode: Optional[str] = None
    visibilityGroups: Optional[list[int]] = None


@dataclass(kw_only=True)
class NavigationItemInput:
    id: str
    kind: str
    label: Optional[str] = None
    icon: Optional[str] = None
    targetType: Optional[str] = None
    target: Optional[str] = None
    visibilityMode: Optional[str] = None
    visibilityGroups: Optional[list[int]] = None


class NavigationMode(Enum):
    NONE: str = "NONE"
    TREE: str = "TREE"
    MIXED: str = "MIXED"
    STATIC: str = "STATIC"


@dataclass(kw_only=True)
class NavigationTree:
    locale: str
    items: list[NavigationItem]


@dataclass(kw_only=True)
class NavigationTreeInput:
    locale: str
    items: list[NavigationItemInput]


@dataclass(kw_only=True)
class NavigationConfig:
    mode: NavigationMode

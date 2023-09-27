from datetime import date
from typing import Optional
from dataclasses import dataclass

from .users import Group            # Resolution of a circular import


@dataclass(kw_only=True)
class GroupMinimal:
    id: int
    name: str
    isSystem: bool
    userCount: Optional[int] = None
    createdAt: date
    updatedAt: date

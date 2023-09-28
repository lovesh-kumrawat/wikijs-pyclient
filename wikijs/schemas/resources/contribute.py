from datetime import date
from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class ContributeContributor:
    id: str
    source: str
    name: str
    joined: date
    website: Optional[str] = None
    twitter: Optional[str] = None
    avatar: Optional[str] = None

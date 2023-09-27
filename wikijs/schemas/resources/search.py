from typing import Optional
from dataclasses import dataclass

from ..responses import KeyValuePair, KeyValuePairInput


@dataclass(kw_only=True)
class SearchEngine:
    isEnabled: bool
    key: str
    title: str
    description: Optional[str] = None
    logo: Optional[str] = None
    website: Optional[str] = None
    isAvailable: Optional[bool] = None
    config: Optional[list[KeyValuePair]] = None


@dataclass(kw_only=True)
class SearchEngineInput:
    isEnabled: bool
    key: str
    config: Optional[list[KeyValuePairInput]] = None

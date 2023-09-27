from datetime import date
from typing import Optional
from dataclasses import dataclass

from ..responses import KeyValuePair, KeyValuePairInput


@dataclass(kw_only=True)
class Logger:
    isEnabled: bool
    key: str
    title: str
    description: Optional[str] = None
    logo: Optional[str] = None
    website: Optional[str] = None
    level: Optional[str] = None
    config: Optional[list[KeyValuePair]] = None


@dataclass(kw_only=True)
class LoggerInput:
    isEnabled: bool
    key: str
    level: str
    config: Optional[list[KeyValuePairInput]] = None


@dataclass(kw_only=True)
class LoggerTrailLine:
    level: str
    output: str
    timestamp: date

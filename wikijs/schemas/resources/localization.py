from datetime import date
from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class LocalizationLocale:
    availability: int
    code: str
    createdAt: date
    installDate: Optional[date] = None
    isInstalled: bool
    isRTL: bool
    name: str
    nativeName: str
    updatedAt: date


@dataclass(kw_only=True)
class LocalizationConfig:
    locale: str
    autoUpdate: bool
    namespacing: bool
    namespaces: list[str]

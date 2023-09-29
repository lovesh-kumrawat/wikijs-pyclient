from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class ThemingConfig:
    theme: str
    iconset: str
    darkMode: bool
    tocPosition: Optional[str] = None
    injectCSS: Optional[str] = None
    injectHead: Optional[str] = None
    injectBody: Optional[str] = None


@dataclass(kw_only=True)
class ThemingTheme:
    key: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None

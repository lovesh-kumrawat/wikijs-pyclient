from typing import Optional
from dataclasses import dataclass

from ..responses import KeyValuePair, KeyValuePairInput


@dataclass(kw_only=True)
class Renderer:
    isEnabled: bool
    key: str
    title: str
    description: Optional[str] = None
    icon: Optional[str] = None
    dependsOn: Optional[str] = None
    input_: Optional[str] = None
    output: Optional[str] = None
    config: Optional[list[KeyValuePair]] = None


@dataclass(kw_only=True)
class RendererInput:
    isEnabled: bool
    key: str
    config: Optional[list[KeyValuePairInput]] = None

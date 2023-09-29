from typing import Optional
from dataclasses import dataclass

from ..responses import KeyValuePair, KeyValuePairInput


@dataclass(kw_only=True)
class StorageTargetAction:
    handler: str
    label: str
    hint: str


@dataclass(kw_only=True)
class StorageTarget:
    isAvailable: bool
    isEnabled: bool
    key: str
    title: str
    description: Optional[str] = None
    logo: Optional[str] = None
    website: Optional[str] = None
    supportedModes: Optional[list[str]] = None
    mode: Optional[str] = None
    hasSchedule: bool
    syncInterval: Optional[str] = None
    syncIntervalDefault: Optional[str] = None
    config: Optional[list[KeyValuePair]] = None
    actions: Optional[list[StorageTargetAction]] = None


@dataclass(kw_only=True)
class StorageTargetInput:
    isEnabled: bool
    key: str
    mode: str
    syncInterval: Optional[str] = None
    config: Optional[list[KeyValuePairInput]] = None


@dataclass(kw_only=True)
class StorageStatus:
    key: str
    title: str
    status: str
    message: str
    lastAttempt: str

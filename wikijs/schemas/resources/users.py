from datetime import date
from typing import Optional
from dataclasses import dataclass

from .pages import PageRule


@dataclass(kw_only=True)
class UserLastLogin:
    id: int
    name: str
    lastLoginAt: date


@dataclass(kw_only=True)
class UserMinimal:
    id: int
    name: str
    email: str
    providerKey: str
    # isSystem: bool
    # isActive: bool
    createdAt: date
    lastLoginAt: Optional[date] = None


@dataclass(kw_only=True)
class Group:
    id: int
    name: str
    isSystem: bool
    redirectOnLogin: Optional[str] = None
    permissions: list[str]
    pageRules: Optional[list[PageRule]] = None
    users: Optional[list[UserMinimal]] = None
    createdAt: date
    updatedAt: date


@dataclass(kw_only=True)
class User:
    id: int
    name: str
    email: str
    providerKey: str
    providerName: Optional[str] = None
    providerId: Optional[str] = None
    providerIs2FACapable: Optional[bool] = None
    isSystem: bool
    isActive: bool
    isVerified: bool
    location: str
    jobTitle: str
    timezone: str
    dateFormat: str
    appearance: str
    createdAt: date
    updatedAt: date
    lastLoginAt: Optional[date] = None
    tfaIsActive: bool
    groups: list[Group]


@dataclass(kw_only=True)
class UserProfile:
    id: int
    name: str
    email: str
    providerKey: Optional[str] = None
    providerName: Optional[str] = None
    isSystem: bool
    isVerified: bool
    location: str
    jobTitle: str
    timezone: str
    dateFormat: str
    appearance: str
    createdAt: date
    updatedAt: date
    lastLoginAt: Optional[date] = None
    groups: list[str]
    pagesTotal: int

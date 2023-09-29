from enum import Enum
from datetime import date
from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class SystemFlag:
    key: str
    value: bool


@dataclass(kw_only=True)
class SystemFlagInput:
    key: str
    value: bool


@dataclass(kw_only=True)
class SystemInfo:
    configFile: Optional[str] = None
    cpuCores: Optional[int] = None
    currentVersion: Optional[str] = None
    dbHost: Optional[str] = None
    dbType: Optional[str] = None
    dbVersion: Optional[str] = None
    groupsTotal: Optional[int] = None
    hostname: Optional[str] = None
    httpPort: Optional[int] = None
    httpRedirection: Optional[bool] = None
    httpsPort: Optional[int] = None
    latestVersion: Optional[str] = None
    latestVersionReleaseDate: Optional[date] = None
    nodeVersion: Optional[str] = None
    operatingSystem: Optional[str] = None
    pagesTotal: Optional[int] = None
    platform: Optional[str] = None
    ramTotal: Optional[str] = None
    sslDomain: Optional[str] = None
    sslExpirationDate: Optional[date] = None
    sslProvider: Optional[str] = None
    sslStatus: Optional[str] = None
    sslSubscriberEmail: Optional[str] = None
    tagsTotal: Optional[int] = None
    telemetry: Optional[bool] = None
    telemetryClientId: Optional[str] = None
    upgradeCapable: Optional[bool] = None
    usersTotal: Optional[int] = None
    workingDirectory: Optional[str] = None


class SystemImportUsersGroupMode(Enum):
    MULTI: str = "MULTI"
    SINGLE: str = "SINGLE"
    NONE: str = "NONE"


@dataclass(kw_only=True)
class SystemExtension:
    key: str
    title: str
    description: str
    isInstalled: bool
    isCompatible: bool


@dataclass(kw_only=True)
class SystemExportStatus:
    status: Optional[str] = None
    progress: Optional[int] = None
    message: Optional[str] = None
    startedAt: Optional[date] = None

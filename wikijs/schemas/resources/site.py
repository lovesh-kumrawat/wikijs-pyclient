from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class SiteConfig:
    host: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    robots: Optional[list[str]] = None
    analyticsService: Optional[str] = None
    analyticsId: Optional[str] = None
    company: Optional[str] = None
    contentLicense: Optional[str] = None
    footerOverride: Optional[str] = None
    logoUrl: Optional[str] = None
    pageExtensions: Optional[str] = None
    authAutoLogin: Optional[bool] = None
    authEnforce2FA: Optional[bool] = None
    authHideLocal: Optional[bool] = None
    authLoginBgUrl: Optional[str] = None
    authJwtAudience: Optional[str] = None
    authJwtExpiration: Optional[str] = None
    authJwtRenewablePeriod: Optional[str] = None
    editFab: Optional[bool] = None
    editMenuBar: Optional[bool] = None
    editMenuBtn: Optional[bool] = None
    editMenuExternalBtn: Optional[bool] = None
    editMenuExternalName: Optional[str] = None
    editMenuExternalIcon: Optional[str] = None
    editMenuExternalUrl: Optional[str] = None
    featurePageRatings: Optional[bool] = None
    featurePageComments: Optional[bool] = None
    featurePersonalWikis: Optional[bool] = None
    securityOpenRedirect: Optional[bool] = None
    securityIframe: Optional[bool] = None
    securityReferrerPolicy: Optional[bool] = None
    securityTrustProxy: Optional[bool] = None
    securitySRI: Optional[bool] = None
    securityHSTS: Optional[bool] = None
    securityHSTSDuration: Optional[int] = None
    securityCSP: Optional[bool] = None
    securityCSPDirectives: Optional[str] = None
    uploadMaxFileSize: Optional[int] = None
    uploadMaxFiles: Optional[int] = None
    uploadScanSVG: Optional[bool] = None
    uploadForceDownload: Optional[bool] = None

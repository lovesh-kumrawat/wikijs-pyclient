from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class MailConfig:
    senderName: Optional[str] = None
    senderEmail: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    name: Optional[str] = None
    secure: Optional[bool] = None
    verifySSL: Optional[bool] = None
    user: Optional[str] = None
    pass_: Optional[str] = None
    useDKIM: Optional[bool] = None
    dkimDomainName: Optional[str] = None
    dkimKeySelector: Optional[str] = None
    dkimPrivateKey: Optional[str] = None

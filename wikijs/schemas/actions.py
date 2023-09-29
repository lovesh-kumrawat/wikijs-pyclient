from typing import Optional
from dataclasses import dataclass

from ..methods.analytics import AnalyticsQuery, AnalyticsMutation
from ..methods.assets import AssetQuery, AssetMutation
from ..methods.authentication import AuthenticationQuery, AuthenticationMutation
from ..methods.comments import CommentQuery, CommentMutation
from ..methods.contribute import ContributeQuery
from ..methods.groups import GroupQuery, GroupMutation
from ..methods.localization import LocalizationQuery, LocalizationMutation
from ..methods.logging import LoggingQuery, LoggingMutation
from ..methods.mail import MailQuery, MailMutation
from ..methods.navigation import NavigationQuery, NavigationMutation
from ..methods.pages import PageQuery, PageMutation
from ..methods.rendering import RenderingQuery, RenderingMutation
from ..methods.search import SearchQuery, SearchMutation
from ..methods.site import SiteQuery, SiteMutation
from ..methods.storage import StorageQuery, StorageMutation
from ..methods.system import SystemQuery, SystemMutation
from ..methods.theming import ThemingQuery, ThemingMutation
from ..methods.users import UserQuery, UserMutation
from .resources.logging import LoggerTrailLine


# Query (Read)
@dataclass(kw_only=True)
class Query:
    analytics: Optional[AnalyticsQuery] = None
    assets: Optional[AssetQuery] = None
    authentication: Optional[AuthenticationQuery] = None
    comments: Optional[CommentQuery] = None
    contribute: Optional[ContributeQuery] = None
    groups: Optional[GroupQuery] = None
    localization: Optional[LocalizationQuery] = None
    logging: Optional[LoggingQuery] = None
    mail: Optional[MailQuery] = None
    navigation: Optional[NavigationQuery] = None
    pages: Optional[PageQuery] = None
    rendering: Optional[RenderingQuery] = None
    search: Optional[SearchQuery] = None
    site: Optional[SiteQuery] = None
    storage: Optional[StorageQuery] = None
    system: Optional[SystemQuery] = None
    theming: Optional[ThemingQuery] = None
    users: Optional[UserQuery] = None


# Mutations (Create, Update, Delete)
@dataclass(kw_only=True)
class Mutation:
    analytics: Optional[AnalyticsMutation] = None
    assets: Optional[AssetMutation] = None
    authentication: Optional[AuthenticationMutation] = None
    comments: Optional[CommentMutation] = None
    groups: Optional[GroupMutation] = None
    localization: Optional[LocalizationMutation] = None
    logging: Optional[LoggingMutation] = None
    mail: Optional[MailMutation] = None
    navigation: Optional[NavigationMutation] = None
    pages: Optional[PageMutation] = None
    rendering: Optional[RenderingMutation] = None
    search: Optional[SearchMutation] = None
    site: Optional[SiteMutation] = None
    storage: Optional[StorageMutation] = None
    system: Optional[SystemMutation] = None
    theming: Optional[ThemingMutation] = None
    users: Optional[UserMutation] = None


# Subscriptions (Push, Real-time)
@dataclass(kw_only=True)
class Subscription:
    loggingLiveTrail: Optional[LoggerTrailLine] = None

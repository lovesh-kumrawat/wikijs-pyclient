import requests
from typing import Any

from .regulators import WikiJSExceptions
from .methods.analytics import AnalyticsQuery, AnalyticsMutation
from .methods.assets import AssetQuery, AssetMutation
from .methods.authentication import AuthenticationQuery, AuthenticationMutation
from .methods.comments import CommentQuery, CommentMutation
from .methods.contribute import ContributeQuery
from .methods.groups import GroupQuery, GroupMutation
from .methods.localization import LocalizationQuery, LocalizationMutation
from .methods.logging import LoggingQuery, LoggingMutation
from .methods.mail import MailQuery, MailMutation
from .methods.navigation import NavigationQuery, NavigationMutation
from .methods.pages import PageQuery, PageMutation
from .methods.rendering import RenderingQuery, RenderingMutation
from .methods.search import SearchQuery, SearchMutation
from .methods.site import SiteQuery, SiteMutation
from .methods.storage import StorageQuery, StorageMutation
from .methods.system import SystemQuery, SystemMutation
from .methods.theming import ThemingQuery, ThemingMutation
from .methods.users import UserQuery, UserMutation


class WikiJS(
    AnalyticsQuery, AnalyticsMutation,
    AssetQuery, AssetMutation,
    AuthenticationQuery, AuthenticationMutation,
    CommentQuery, CommentMutation,
    ContributeQuery,
    GroupQuery, GroupMutation,
    LocalizationQuery, LocalizationMutation,
    LoggingQuery, LoggingMutation,
    MailQuery, MailMutation,
    NavigationQuery, NavigationMutation,
    PageQuery, PageMutation,
    RenderingQuery, RenderingMutation,
    SearchQuery, SearchMutation,
    SiteQuery, SiteMutation,
    StorageQuery, StorageMutation,
    SystemQuery, SystemMutation,
    ThemingQuery, ThemingMutation,
    UserQuery, UserMutation,
):
    
    def __init__(self, url: str, token: str) -> None:
        
        self.endpoint = f"{url}/graphql"
        self.auth = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    
    def gql_post(self, gql_query: str, params: dict[str, Any]) -> dict[str, Any]:
        
        response = requests.post(
            url=self.endpoint,
            headers=self.auth,
            json={
                "query": gql_query,
                "variables": params
            }
        ).json()

        if response.get("errors"):
            
            err = response.get("errors")[0]
            
            raise WikiJSExceptions(         #noqa: IICE (Immediately Invoked Class Expression) was used
                err['extensions']['code'],
                err['message']
            )
        
        return response.get("data")

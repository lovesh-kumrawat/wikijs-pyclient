from typing import Optional

from ..schemas.resources.theming import ThemingTheme, ThemingConfig
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class ThemingQuery:
    
    @Response.response(list[ThemingTheme], action="query", resource="theming", method="themes")
    def get_themes(self) -> Response:
        
        """
        """
    
    @Response.response(ThemingConfig, action="query", resource="theming", method="config")
    def get_theme_config(self) -> Response:
        
        """
        """


class ThemingMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="theming", method="setConfig")
    def set_theme_config(
            self,
            *,
            theme: str,
            iconset: str,
            darkMode: bool,
            tocPosition: Optional[str] = None,
            injectCSS: Optional[str] = None,
            injectHead: Optional[str] = None,
            injectBody: Optional[str] = None
        ) -> Response:
        
        """
        """

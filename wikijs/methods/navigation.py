from ..schemas.resources.navigation import (
    NavigationMode,
    NavigationTree,
    NavigationTreeInput,
    NavigationConfig
)
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class NavigationQuery(GqlBase):
    
    @Response.response(list[NavigationTree], action="query", resource="navigation", method="tree")
    def get_navigation_tree(self) -> Response:
        
        """
        """
    
    @Response.response(NavigationConfig, action="query", resource="navigation", method="config")
    def get_navigation_config(self) -> Response:
    
        """
        """


class NavigationMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="navigation", method="updateTree")
    def update_navigation_tree(self, *, tree: list[NavigationTreeInput]) -> Response:
        
        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="navigation", method="updateConfig")
    def update_navigation_config(self, *, mode: NavigationMode) -> Response:
        
        """
        """

from typing import Optional

from ..schemas.resources.pages import PageRuleInput
from ..schemas.resources.groups import Group, GroupMinimal
from ..schemas.responses import DefaultResponse, GroupResponse
from ..base import GqlBase, Response


class GroupQuery(GqlBase):
    
    @Response.response(list[GroupMinimal], action="query", resource="groups", method="list")
    def get_groups(self, *, filter: Optional[str] = None, orderBy: Optional[str] = None) -> Response:
        
        """
        """
    
    @Response.response(Group, action="query", resource="groups", method="single")
    def get_group(self, *, id: int) -> Response:
        
        """
        """


class GroupMutation(GqlBase):

    @Response.response(GroupResponse, action="mutation", resource="groups", method="create")
    def create_group(self, *, name: str) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="groups", method="update")
    def update_group(
            self,
            *,
            id: int,
            name: str,
            redirectOnLogin: str,
            permissions: list[str],
            pageRules: list[PageRuleInput]
        ) -> Response:
        
        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="groups", method="delete")
    def delete_group(self, *, id: int) -> Response:
        
        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="groups", method="assignUser")
    def assign_user(self, *, groupId: int, userId: int) -> Response:
        
        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="groups", method="unassignUser")
    def unassign_user(self, *, groupId: int, userId: int) -> Response:
        
        """
        """

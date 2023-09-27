from typing import Optional

from ..schemas.resources.comments import CommentProvider, CommentProviderInput, CommentPost
from ..schemas.responses import DefaultResponse, CommentCreateResponse, CommentUpdateResponse
from ..base import GqlBase, Response


class CommentQuery(GqlBase):
    
    @Response.response(list[CommentProvider], action="query", resource="comments", method="providers")
    def get_comment_providers(self) -> Response:

        """
        """
    
    @Response.response(list[CommentPost], action="query", resource="comments", method="list")
    def get_comments(self, *, locale: str, path: str) -> Response:

        """
        """

    @Response.response(CommentPost, action="query", resource="comments", method="single")
    def get_comment(self, *, id: int) -> Response:

        """
        """


class CommentMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="comments", method="updateProviders")
    def update_comment_providers(self, *, providers: Optional[list[CommentProviderInput]] = None) -> Response:

        """
        """

    @Response.response(CommentCreateResponse, action="mutation", resource="comments", method="create")
    def create_comment(
            self,
            *,
            pageId: int,
            replyTo: Optional[int] = None,
            content: str,
            guestName: Optional[str] = None,
            guestEmail: Optional[str] = None
        ) -> Response:

        """
        """

    @Response.response(CommentUpdateResponse, action="mutation", resource="comments", method="update")
    def update_comment(self, *, id: int, content: str) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="comments", method="delete")
    def delete_comment(self, *, id: int) -> Response:

        """
        """

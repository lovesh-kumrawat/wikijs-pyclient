from typing import Optional

from ..schemas.resources.rendering import Renderer, RendererInput
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class RenderingQuery(GqlBase):

    @Response.response(list[Renderer], action="query", resource="rendering", method="renderers")
    def get_renderers(self, *, filter: Optional[str] = None, orderBy: Optional[str] = None) -> Response:
        
        """
        """


class RenderingMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="rendering", method="updateRenderers")
    def update_renderers(self, *, renderers: Optional[list[RendererInput]] = None) -> Response:
        
        """
        """

from typing import Optional

from ..schemas.resources.search import SearchEngine, SearchEngineInput
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class SearchQuery(GqlBase):

    @Response.response(list[SearchEngine], action="query", resource="search", method="searchEngines")
    def get_search_engines(self, *, filter: Optional[str] = None, orderBy: Optional[str] = None) -> Response:
        
        """
        """


class SearchMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="search", method="updateSearchEngines")
    def update_search_engines(self, *, engines: list[SearchEngineInput]) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="search", method="rebuildIndex")
    def rebuild_search_index(self) -> Response:
        
        """
        """

from datetime import date
from typing import Optional

from ..schemas.resources.pages import (
    Page,
    PageListItem,
    PageVersion,
    PageHistoryResult,
    PageTreeItem,
    PageLinkItem,
    PageConflictLatest,
    PageOrderBy,
    PageOrderByDirection,
    PageTreeMode,
    PageTag
)
from ..schemas.responses import (
    DefaultResponse,
    PageMigrationResponse,
    PageResponse,
    PageSearchResponse
)
from ..base import GqlBase, Response


class PageQuery(GqlBase):
    
    @Response.response(PageHistoryResult, action="query", resource="pages", method="history")
    def get_page_history(self, *, id: int, offsetPage: Optional[int] = None, offsetSize: Optional[int] = None) -> Response:
        
        """
        """
    
    @Response.response(PageVersion, action="query", resource="pages", method="version")
    def get_page_version(self, *, pageId: int, versionId: int) -> Response:
        
        """
        """
    
    @Response.response(PageSearchResponse, action="query", resource="pages", method="search")
    def get_pages(self, *, query: str, path: Optional[str] = None, locale: Optional[str] = None) -> Response:

        """
        Get a list of pages by search query, within a path and locale
        """
    
    @Response.response(list[PageListItem], action="query", resource="pages", method="list")
    def list_pages(
            self,
            *,
            limit: Optional[int] = None,
            orderBy: Optional[PageOrderBy] = None,
            orderByDirection: Optional[PageOrderByDirection] = None,
            tags: Optional[list[str]] = None,
            locale: Optional[str] = None,
            creatorId: Optional[int] = None,
            authorId: Optional[int] = None
        ) -> Response:
        
        """
        """

    @Response.response(Page, action="query", resource="pages", method="single")
    def get_page(self, *, id: int) -> Response:
        
        """
        Get single page by ID
        """
    
    @Response.response(Page, action="query", resource="pages", method="singleByPath")
    def get_page_by_path(self, *, path: str, locale: str) -> Response:

        """
        Get single page by path within a locale
        """
    
    @Response.response(list[PageTag], action="query", resource="pages", method="tags")
    def list_tags(self) -> Response:

        """
        """
    
    @Response.response(list[str], action="query", resource="pages", method="searchTags")
    def get_tags(self, *, query: str) -> Response:
        
        """
        Get a list of existing tags by search query
        """
    
    @Response.response(list[PageTreeItem], action="query", resource="pages", method="tree")
    def get_page_tree(
            self,
            *,
            path: Optional[str] = None,
            parent: Optional[int] = None,
            mode: PageTreeMode,
            locale: str,
            includeAncestors: Optional[bool] = None
        ) -> Response:
        
        """
        """

    @Response.response(list[PageLinkItem], action="query", resource="pages", method="links")
    def get_page_links(self, *, locale: str) -> Response:
        
        """
        """
    
    @Response.response(bool, action="query", resource="pages", method="checkConflicts")
    def check_page_conflicts(self, *, id: int, checkoutDate: date) -> Response:
        
        """
        """
    
    @Response.response(PageConflictLatest, action="query", resource="pages", method="conflictLatest")
    def get_page_latest_conflict(self, *, id: int) -> Response:
        
        """
        """


class PageMutation(GqlBase):
    
    @Response.response(PageResponse, action="mutation", resource="pages", method="create")
    def create_page(
            self,
            *,
            content: str,
            description: str,
            editor: str,
            isPublished: bool,
            isPrivate: bool,
            locale: str,
            path: str,
            publishEndDate: Optional[date] = None,
            publishStartDate: Optional[date] = None,
            scriptCss: Optional[str] = None,
            scriptJs: Optional[str] = None,
            tags: list[str],
            title: str
        ) -> Response:
        
        """
        Create a new page if not exists else raise an exception
        """
    
    @Response.response(PageResponse, action="mutation", resource="pages", method="update")
    def update_page(
            self,
            *,
            id: int,
            content: Optional[str] = None,
            description: Optional[str] = None,
            # editor: Optional[str] = None,
            isPrivate: Optional[bool] = None,
            isPublished: Optional[bool] = None,
            # locale: Optional[str] = None,
            path: Optional[str] = None,
            publishEndDate: Optional[date] = None,
            publishStartDate: Optional[date] = None,
            scriptCss: Optional[str] = None,
            scriptJs: Optional[str] = None,
            tags: Optional[list[str]] = None,
            title: Optional[str] = None
        ) -> Response:

        """
        Update a page if exists else raise an exception
        """
        
        params = locals()
        params.pop("self", None)
        
        # To coverup the optional None values
        page = PageQuery.get_page(self, _json=True, id=id)
        return {param : page.get(param) if value is None else value for param, value in params.items()}
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="convert")
    def convert_page(self, *, id: int, editor: str) -> Response:
        
        """
        Convert a page's' editor mode
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="move")
    def move_page(self, *, id: int, destinationPath: str, destinationLocale: str) -> Response:
        """
        Move a page to a new path within a locale
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="delete")
    def delete_page(self, *, id: int) -> Response:

        """
        Delete a page if exists else raise an exception
        """
    
    def delete_page_by_path(self, *, path: str, locale: str) -> Response:
        
        """
        Delete a page by path within a locale
        """
        
        page = PageQuery.get_page_by_path(self, _json=True, path=path, locale=locale)
        response = PageMutation.delete_page(self, id=int(page['id']))
        
        return response
    
    def delete_pages(self, *, query: str = "", path: str = None, locale: str = None) -> Response:

        """
        Delete pages by query, within a path and locale
        """
        
        pages = PageQuery.get_pages(self, _json=True, query=query, path=path, locale=locale)
        responses = [PageMutation.delete_page(self, _json=True, id=int(page['id'])) for page in pages['results']]

        return Response.verified(list[DefaultResponse], responses)
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="deleteTag")
    def delete_tag(self, *, id: int) -> Response:
        
        """
        Delete a tag if exists else raise an exception
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="updateTag")
    def update_tag(self, *, id: int, tag: str, title: str) -> Response:
        
        """
        Update a tag if exists else raise an exception
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="flushCache")
    def flush_page_cache(self) -> Response:
        
        """
        Flush the page cache
        """
    
    @Response.response(PageMigrationResponse, action="mutation", resource="pages", method="migrateToLocale")
    def migrate_page_locale(self, *, sourceLocale: str, targetLocale: str) -> Response:
        
        """
        Migrate pages from source locale to target locale
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="rebuildTree")
    def rebuild_page_tree(self) -> Response:
        
        """
        Rebuild the page tree
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="render")
    def render_page(self, *, id: int) -> Response:
        
        """
        Render a page
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="restore")
    def restore_page_version(self, *, pageId: int, versionId: int) -> Response:
        
        """
        Restore a page to a previous version
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="pages", method="purgeHistory")
    def purge_page_history(self, *, olderThan: str) -> Response:

        """
        Purge page history
        """

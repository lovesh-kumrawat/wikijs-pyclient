from typing import Optional

from ..schemas.resources.assets import AssetFolder, AssetItem, AssetKind
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class AssetQuery(GqlBase):

    @Response.response(list[AssetItem], action="query", resource="assets", method="list")
    def get_assets(self, *, folderId: int, kind: AssetKind) -> Response:
        
        """
        """
    
    @Response.response(list[AssetFolder], action="query", resource="assets", method="folders")
    def get_folders(self, *, parentFolderId: int) -> Response:
        
        """
        """


class AssetMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="assets", method="createFolder")
    def create_folder(self, *, parentFolderId: int, slug: str, name: Optional[str] = None) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="assets", method="renameAsset")
    def rename_asset(self, *, id: int, filename: str) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="assets", method="deleteAsset")
    def delete_asset(self, *, id: int) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="assets", method="flushTempUploads")
    def flush_temp_uploads(self) -> Response:
        
        """
        """

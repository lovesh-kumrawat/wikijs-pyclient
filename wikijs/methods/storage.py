from typing import Optional

from ..schemas.resources.storage import StorageTarget, StorageTargetInput, StorageStatus
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class StorageQuery(GqlBase):

    @Response.response(Optional[list[StorageTarget]], action="query", resource="storage", method="targets")
    def storage_targets(self) -> Response:
        
        """
        """
    
    @Response.response(Optional[list[StorageStatus]], action="query", resource="storage", method="status")
    def storage_status(self) -> Response:
        
        """
        """


class StorageMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="storage", method="updateTargets")
    def update_storage_targets(self, *, targets: list[StorageTargetInput]) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="storage", method="executeAction")
    def execute_storage_action(self, *, targetKey: str, handler: str) -> Response:
        
        """
        """

from typing import Optional

from ..schemas.resources.system import (
    SystemFlag,
    SystemFlagInput,
    SystemInfo,
    SystemImportUsersGroupMode,
    SystemExtension,
    SystemExportStatus
)
from ..schemas.responses import DefaultResponse, SystemImportUsersResponse
from ..base import GqlBase, Response


class SystemQuery:
    
    @Response.response(Optional[list[SystemFlag]], action="query", resource="system", method="flags")
    def get_system_flags(self) -> Response:
        
        """
        """
    
    @Response.response(Optional[SystemInfo], action="query", resource="system", method="info")
    def system_info(self) -> Response:
        
        """
        """
    
    @Response.response(Optional[list[SystemExtension]], action="query", resource="system", method="extensions")
    def system_extensions(self) -> Response:
        
        """
        """
    
    @Response.response(Optional[SystemExportStatus], action="query", resource="system", method="exportStatus")
    def export_system_status(self) -> Response:
        
        """
        """


class SystemMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="system", method="updateFlags")
    def update_system_flags(self, *, flags: list[SystemFlagInput]) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="system", method="resetTelemetryClientId")
    def reset_system_telemetry_client_id(self) -> Response:

        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="system", method="setTelemetry")
    def set_system_telemetry(self, *, enabled: bool) -> Response:

        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="system", method="performUpgrade")
    def perform_system_upgrade(self) -> Response:

        """
        """
    
    @Response.response(SystemImportUsersResponse, action="mutation", resource="system", method="importUsersFromV1def")
    def import_users_from_v1def(self, *, mongoDbConnstr: str, groupMode: SystemImportUsersGroupMode) -> Response:
        
        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="system", method="setHTTPSRedirection")
    def set_system_https_redirection(self, *, enabled: bool) -> Response:

        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="system", method="renewHTTPSCertificate")
    def renew_system_https_certificate(self) -> Response:

        """
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="system", method="export")
    def export_system(self, *, entities: list[str], path: str) -> Response:

        """
        """

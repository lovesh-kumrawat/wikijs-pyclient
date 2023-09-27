from typing import Optional

from ..schemas.resources.authentication import (
    AuthenticationApiKey,
    AuthenticationActiveStrategy,
    AuthenticationStrategy,
    AuthenticationStrategyInput
)
from ..schemas.responses import (
    DefaultResponse,
    AuthenticationCreateApiKeyResponse,
    AuthenticationLoginResponse,
    AuthenticationRegisterResponse
)
from ..base import GqlBase, Response


class AuthenticationQuery(GqlBase):

    @Response.response(list[AuthenticationApiKey], action="query", resource="authentication", method="apiKeys")
    def get_api_keys(self) -> Response:
        
        """
        """

    @Response.response(bool, action="query", resource="authentication", method="apiState")
    def api_state(self) -> Response:
        
        """
        """

    @Response.response(list[AuthenticationStrategy], action="query", resource="authentication", method="strategies")
    def get_strategies(self) -> Response:
        
        """
        """

    @Response.response(list[AuthenticationActiveStrategy], action="query", resource="authentication", method="activeStrategies")
    def get_active_strategies(self, *, enabledOnly: Optional[bool] = None) -> Response:
        
        """
        """


class AuthenticationMutation(GqlBase):

    @Response.response(AuthenticationCreateApiKeyResponse, action="mutation", resource="authentication", method="createApiKey")
    def create_api_key(self, *, name: str, expiration: str, fullAccess: bool, group: Optional[int] = None) -> Response:

        """
        """

    @Response.response(AuthenticationLoginResponse, action="mutation", resource="authentication", method="login")
    def login(self, *, username: str, password: str, strategy: str) -> Response:

        """
        """

    @Response.response(AuthenticationLoginResponse, action="mutation", resource="authentication", method="logintFA")
    def login_TFA(self, *, continuationToken: str, securityCode: str, setup: Optional[bool] = None) -> Response:

        """
        """

    @Response.response(AuthenticationLoginResponse, action="mutation", resource="authentication", method="loginChangePassword")
    def reset_password(self, *, continuationToken: str, newPassword: str) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="authentication", method="forgotPassword")
    def forgot_password(self, *, email: str) -> Response:

        """
        """

    @Response.response(AuthenticationRegisterResponse, action="mutation", resource="authentication", method="register")
    def register(self, *, email: str, password: str, name: str) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="authentication", method="revokeApiKey")
    def revoke_api_key(self, *, id: int) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="authentication", method="setApiState")
    def set_api_state(self, *, enabled: bool) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="authentication", method="updateStrategies")
    def update_strategies(self, *, strategies: list[AuthenticationStrategyInput]) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="authentication", method="regenerateCertificates")
    def regenerate_certificates(self) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="authentication", method="resetGuestUser")
    def reset_guest_user(self) -> Response:

        """
        """

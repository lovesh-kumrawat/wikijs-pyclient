from typing import Optional

from ..schemas.resources.users import UserLastLogin, UserMinimal, User, UserProfile
from ..schemas.responses import DefaultResponse, UserResponse, UserTokenResponse
from ..base import GqlBase, Response


class UserQuery(GqlBase):

    @Response.response(list[UserMinimal], action="query", resource="users", method="list")
    def list_users(self, *, filter: Optional[str] = None, orderBy: Optional[str] = None) -> Response:

        """
        """
    
    @Response.response(list[UserMinimal], action="query", resource="users", method="search")
    def get_users(self, *, query: str) -> Response:

        """
        Get a list of users by search query
        """
    
    @Response.response(User, action="query", resource="users", method="single")
    def get_user(self, *, id: int) -> Response:
        
        """
        Get single user by ID
        """
    
    @Response.response(UserProfile, action="query", resource="users", method="profile")
    def get_admin_profile(self) -> Response:

        """
        """

    @Response.response(list[UserLastLogin], action="query", resource="users", method="lastLogins")
    def get_last_logins(self) -> Response:

        """
        """


class UserMutation(GqlBase):
    
    @Response.response(UserResponse, action="mutation", resource="users", method="create")
    def create_user(
            self,
            *,
            email: str,
            name: str,
            passwordRaw: Optional[str] = None,
            providerKey: str,
            groups: list[int],
            mustChangePassword: Optional[bool] = None,
            sendWelcomeEmail: Optional[bool] = None
        ) -> Response:

        """
        Create a new user
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="users", method="update")
    def update_user(
            self,
            *,
            id: int,
            email: Optional[str] = None,
            name: Optional[str] = None,
            newPassword: Optional[str] = None,
            groups: Optional[list[int]] = None,
            location: Optional[str] = None,
            jobTitle: Optional[str] = None,
            timezone: Optional[str] = None,
            dateFormat: Optional[str] = None,
            appearance: Optional[str] = None
        ) -> Response:

        """
        Update a user
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="users", method="delete")
    def delete_user(self, *, id: int, replaceId: int) -> Response:

        """
        Delete a user
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="users", method="verify")
    def verify_user(self, *, id: int):
        
        """
        Verify a user
        """
    
    @Response.response(DefaultResponse, action="mutation", resource="users", method="activate")
    def activate_user(self, *, id: int) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="users", method="deactivate")
    def deactivate_user(self, *, id: int) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="users", method="enableTFA")
    def enable_user_tfa(self, *, id: int) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="users", method="disableTFA")
    def disable_user_tfa(self, *, id: int) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="users", method="resetPassword")
    def reset_user_password(self, *, id: int) -> Response:

        """
        """

    @Response.response(UserTokenResponse, action="mutation", resource="users", method="updateProfile")
    def update_user_profile(
            self,
            *,
            name: str,
            location: str,
            jobTitle: str,
            timezone: str,
            dateFormat: str,
            appearance: str
        ) -> Response:

        """
        """

    @Response.response(UserTokenResponse, action="mutation", resource="users", method="changePassword")
    def change_user_password(self, *, current: str, new: str) -> Response:

        """
        """

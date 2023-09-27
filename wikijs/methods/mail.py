from ..schemas.resources.mail import MailConfig
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class MailQuery(GqlBase):
    
    @Response.response(MailConfig, action="query", resource="mail", method="config")
    def get_mail_config(self) -> Response:

        """
        """


class MailMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="mail", method="sendTest")
    def send_test_mail(self, *, recipientEmail: str) -> Response:
        
        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="mail", method="updateConfig")
    def update_mail_config(
            self,
            *,
            senderName: str,
            senderEmail: str,
            host: str,
            port: int,
            name: str,
            secure: bool,
            verifySSL: bool,
            user: str,
            pass_: str,
            useDKIM: bool,
            dkimDomainName: str,
            dkimKeySelector: str,
            dkimPrivateKey: str
        ) -> Response:

        """
        """

from typing import Optional

from ..schemas.resources.logging import Logger, LoggerInput
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class LoggingQuery(GqlBase):

    @Response.response(list[Logger], action="query", resource="logging", method="loggers")
    def get_loggers(self, *, filter: Optional[str] = None, orderBy: Optional[str] = None) -> Response:

        """
        """


class LoggingMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="logging", method="updateLoggers")
    def update_loggers(self, *, loggers: Optional[list[LoggerInput]] = None) -> Response:

        """
        """

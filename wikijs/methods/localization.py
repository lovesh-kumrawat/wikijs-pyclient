from ..schemas.resources.localization import LocalizationLocale, LocalizationConfig
from ..schemas.responses import DefaultResponse, Translation
from ..base import GqlBase, Response


class LocalizationQuery(GqlBase):

    @Response.response(list[LocalizationLocale], action="query", resource="localization", method="locales")
    def get_locales(self) -> Response:

        """
        """

    @Response.response(LocalizationConfig, action="query", resource="localization", method="config")
    def get_locale_config(self) -> Response:

        """
        """

    @Response.response(list[Translation], action="query", resource="localization", method="translations")
    def locale_translations(self, *, locale: str, namespace: str) -> Response:

        """
        """


class LocalizationMutation(GqlBase):

    @Response.response(DefaultResponse, action="mutation", resource="localization", method="downloadLocale")
    def download_locale(self, *, locale: str) -> Response:

        """
        """

    @Response.response(DefaultResponse, action="mutation", resource="localization", method="updateLocale")
    def update_locale(self, *, locale: str, autoUpdate: bool, namespacing: bool, namespaces: list[str]) -> Response:

        """
        """

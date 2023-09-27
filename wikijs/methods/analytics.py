from typing import Optional

from ..schemas.resources.analytics import AnalyticsProvider, AnalyticsProviderInput
from ..schemas.responses import DefaultResponse
from ..base import GqlBase, Response


class AnalyticsQuery(GqlBase):
    
    @Response.response(list[AnalyticsProvider], action="query", resource="analytics", method="providers")
    def get_analytics_providers(self, *, isEnabled: Optional[bool] = None) -> Response:

        """
        Fetch list of Analytics providers and their configuration
        
        params:
            isEnabled: Return only active providers
        """


class AnalyticsMutation(GqlBase):
    
    @Response.response(DefaultResponse, action="mutation", resource="analytics", method="updateProviders")
    def update_analytics_providers(self, *, providers: list[AnalyticsProviderInput]) -> Response:
        
        """
        Update a list of Analytics providers and their configuration
        """

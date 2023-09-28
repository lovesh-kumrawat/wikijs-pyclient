from ..schemas.resources.contribute import ContributeContributor
from ..base import GqlBase, Response


class ContributeQuery(GqlBase):

    @Response.response(list[ContributeContributor], action="query", resource="contribute", method="contributors")
    def get_contributors(self) -> Response:

        """
        """

import requests
from typing import Any

from .regulators import WikiJSExceptions


class WikiJS:
    
    def __init__(self, url: str, token: str) -> None:
        
        self.endpoint = f"{url}/graphql"
        self.auth = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    
    def gql_post(self, gql_query: str, params: dict[str, Any]) -> dict[str, Any]:
        
        response = requests.post(
            url=self.endpoint,
            headers=self.auth,
            json={
                "query": gql_query,
                "variables": params
            }
        ).json()

        if response.get("errors"):
            
            err = response.get("errors")[0]
            
            raise WikiJSExceptions(         #noqa: IICE (Immediately Invoked Class Expression) was used
                err['extensions']['code'],
                err['message']
            )
        
        return response.get("data")

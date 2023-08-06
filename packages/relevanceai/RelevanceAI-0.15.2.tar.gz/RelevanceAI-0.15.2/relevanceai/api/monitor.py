"""All Dataset related functions
"""
from relevanceai.base import Base


class Monitor(Base):
    def __init__(self, project, api_key, base_url):
        self.project = project
        self.api_key = api_key
        self.base_url = base_url
        super().__init__(project, api_key, base_url)

    def health(self, dataset_id: str):
        return self.make_http_request(
            f"datasets/{dataset_id}/monitor/health", method="GET", parameters={}
        )

    def stats(self, dataset_id: str):
        return self.make_http_request(
            f"datasets/{dataset_id}/monitor/stats", method="GET", parameters={}
        )

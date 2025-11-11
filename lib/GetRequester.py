import json  # noqa: F401

import requests  # noqa: F401


class GetRequester:
    url = (
        "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    )

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        raw = self.get_response_body()
        return json.loads(raw)

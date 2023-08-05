import json


class CircleResponse:
    def __init__(self, body, code, headers):
        self.body = body
        self.code = code
        self.headers = headers

        json_body = json.loads(body)
        self.data = json_body.get("data", json_body)
        print(self.data)

    @property
    def idempotency_key(self):
        try:
            return self.headers["idempotency-key"]
        except KeyError:
            return None

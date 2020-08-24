import json


class JSONEncoder:
    scheme = "json"

    def encode(self, data):
        return json.dumps(data)

    def decode(self, data):
        return json.loads(data)
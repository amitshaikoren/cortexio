import json


class JSONProtocol:
    scheme = "json"

    # TODO: make this stupid function be able to take as many arguments as it wants and convert it to json
    def serialize(self, user_dict, snapshot_dict, raw_data):
        if user_dict is not None and snapshot_dict is not None:
            serialized_user_dict = json.dumps(user_dict)
            serialized_snapshot_dict = json.dumps(snapshot_dict)
            return serialized_user_dict, serialized_snapshot_dict

        elif raw_data is not None:
            json.dumps(raw_data)

    def deserialize(self, data):
        return json.loads(data)

    def convert_to_python_dict(self, user_json, snapshot_json):
        return self.deserialize(user_json), self.deserialize(snapshot_json)

    def convert_from_python_dict(self, user_dict, snapshot_dict):
        return self.serialize(user_dict, snapshot_dict)

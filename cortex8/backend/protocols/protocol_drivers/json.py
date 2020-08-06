import json
import struct


class JSONProtocol:
    scheme = "json"

    def serialize(self, user_dict, snapshot_dict, raw_data):
        if user_dict and snapshot_dict:
            serialized_user_dict = json.dumps(user_dict)
            serialized_snapshot_dict = json.dumps(snapshot_dict)
            return serialized_user_dict, serialized_snapshot_dict

        elif raw_data:
            json.dumps(raw_data)

    def deserialize(self, data):
        return json.loads(data)

    def convert_to_python_dict(self, user_json, snapshot_json):
        return self.deserialize(user_json), self.deserialize(snapshot_json)

    def convert_from_python_dict(self, user_dict, snapshot_dict):
        return self.serialize(user_dict, snapshot_dict)

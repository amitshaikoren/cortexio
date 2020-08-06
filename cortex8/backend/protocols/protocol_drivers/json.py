import json
import struct


class JSONProtocol:
    scheme = "json"

    def serialize(self, user_dict, snapshot_dict):
        raise NotImplementedError()

    def deserialize(self, data):
        raise NotImplementedError()

    def convert_to_python_dict(self, user, snapshot):
        # TODO: implement
        raise NotImplementedError()

    def convert_from_python_dict(self, user_dict, snapshot_dict):
        # TODO: implement
        raise NotImplementedError()

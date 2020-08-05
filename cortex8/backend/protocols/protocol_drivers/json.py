import json
import struct

class JSONProtocol:
    scheme = "json"

    def serialize(self, user, snapshot):
        user_data = user.SerializeToString()

        snapshot_data = snapshot.SerializeToString()

        serialized_msg = user_len + user_data + snapshot_len + snapshot_data
        return serialized_msg

    def deserialize(self, data):
        stream = io.BytesIO(data)

        user = User()
        user_len, = struct.unpack('I', stream.read(UINT32_SIZE))
        user_bytes = stream.read(user_len)
        user.ParseFromString(user_bytes)

        snapshot = Snapshot()
        snapshot_len, = struct.unpack('I', stream.read(UINT32_SIZE))
        snapshot_bytes = stream.read(snapshot_len)
        snapshot.ParseFromString(snapshot_bytes)

        return user, snapshot
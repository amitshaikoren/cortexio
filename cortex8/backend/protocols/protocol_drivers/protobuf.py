"""
1. Do shit of protobuf
2. implement protobuf driver

"""
import struct
import io
from .protobuf_data import User, Snapshot


UINT32_SIZE = 4


class ProtobufProtocol:
    scheme = "protobuf"

    def serilize(self, user, snapshot):
        user_data = user.SerializeToString()
        user_len = struct.pack('I', len(user_data))

        snapshot_data = snapshot.SerializeToString()
        snapshot_len = struct.pack('I', len(snapshot_data))

        serialized_msg = user_len + user_data + snapshot_len + snapshot_data
        return serialized_msg

    def deserilize(self, data):
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

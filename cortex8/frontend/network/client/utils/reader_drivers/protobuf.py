import gzip
import struct

# TODO: delete:
from cortex8.backend.protocols.protocol_drivers.protobuf_data import User, Snapshot
abs_path_linux = "/home/user/Downloads/exercise7/sample.mind.gz"
#abs_path_mac = "/Users/apple/Desktop/Advanced_System_Design/Exercise_7/sample.mind.gz"

UINT32_SIZE = 4


class ProtobufReader:
    scheme = 'protobuf'

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        # TODO: implement security measures
        # for example, someone can pass a malicious path or a path to a malicious file

        self.stream = gzip.open(self.path, "rb")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stream.close()

    def _get_data(self):
        # TODO: implement security measures
        # for example, someone can pass a larger/smaller size to be read

        size_str = self.stream.read(UINT32_SIZE)
        size_int, = struct.unpack('I', size_str)
        data = self.stream.read(size_int)
        return data

    def get_user(self):
        user = User()
        user.ParseFromString(self._get_data())
        return user

    def get_snapshot(self):
        snapshot = Snapshot()
        try:
            snapshot.ParseFromString(self._get_data())
            return snapshot
        except struct.error:
            return None

# TODO: delete
#if __name__ == "__main__":
 #   with ProtobufReader(abs_path_linux) as pbr:
 #       client_server_protocol = ProtocolManager("protobuf")
  #      user = pbr.get_user()
  #      snapshot = pbr.get_snapshot()
  #      print(client_server_protocol.convert_to_python_dict(user, snapshot))



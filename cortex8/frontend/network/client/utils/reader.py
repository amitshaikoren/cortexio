from cortex8.backend.protocols import ProtocolManager
from cortex8.utils import load_drivers



drivers = load_drivers("reader_drivers")


class Reader:
    def __init__(self, path, reader_scheme="protobuf"):
        self.path = path
        self.reader = drivers[reader_scheme](path)

    def __enter__(self):
        self.reader.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.reader.__exit__(exc_type, exc_val, exc_tb)

    def get_user(self):
        return self.reader.get_user()

    def get_snapshot(self):
        return self.reader.get_snapshot()

    def __iter__(self):
        while snapshot := self.reader.get_snapshot():
            yield snapshot

# TODO: delte
if __name__ == "__main__":
    with Reader(abs_path_linux) as pbr:
        client_server_protocol = ProtocolManager("protobuf")
        user = pbr.get_user()
        snapshot = pbr.get_snapshot()
        print(client_server_protocol.convert_to_python_dict(user, snapshot))


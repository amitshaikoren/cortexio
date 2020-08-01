from cortex8.utils import load_drivers


drivers = load_drivers("reader_drivers")


class Reader:
    def __init__(self, path, file_reader_scheme="protobuf"):
        self.path = path
        self.file_reader = drivers[file_reader_scheme](path)

    def __enter__(self):
        self.file_reader.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_reader.__exit__(exc_type, exc_val, exc_tb)

    def get_user(self):
        return self.file_reader.get_user()

    def get_snapshot(self):
        return self.file_reader.get_snapshot()

    def __iter__(self):
        while snapshot := self.file_reader.get_snapshot():
            yield snapshot


if __name__ == "__main__":
    with Reader("/home/user/Downloads/exercise7/sample.mind.gz") as reader:
        print(reader.get_user())
        # print(reader.get_snapshot())
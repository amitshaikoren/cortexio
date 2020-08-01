UINT64_size = 8
UINT32_size = 4


reader_drivers = my_utils.load_drivers(drivers_path="./brainstreamer/platforms/reader/reader_drivers",
                                       driver_type="class")


class Reader:
    def __init__(self, path, file_reader_scheme="protobuf"):
        self.path = path
        self.file_reader = reader_drivers[file_reader_scheme](path)


    def get_user(self):
        return self.file_reader.get_user()

    def get_snapshot(self):
        return self.file_reader.get_snapshot()

    def __iter__(self):
        while snapshot := self.file_reader.get_snapshot():
            yield snapshot
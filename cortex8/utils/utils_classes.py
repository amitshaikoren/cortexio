import pathlib


class FileSystemManager:
    @staticmethod
    def save(self, data, path):
        p = pathlib.Path(path)
        p.mkdir(parents=True, exist_ok=True)
        with p.open(mode='wb+') as fd:
            fd.write(data)

    @staticmethod
    def load(self, path):
        p = pathlib.Path(path)
        with p.open(mode='rb+') as fd:
            return fd.read()
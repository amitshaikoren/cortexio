import pathlib


class FileSystemManager:
    @staticmethod
    def save(data, path):
        p = pathlib.Path(path)
        new_dir_path = p.parent
        new_dir_path.mkdir(parents=True, exist_ok=True)
        with p.open(mode='wb+') as fd:
            fd.write(data)

    @staticmethod
    def load(path):
        p = pathlib.Path(path)
        with p.open(mode='rb+') as fd:
            return fd.read()


#TODO: fix save method
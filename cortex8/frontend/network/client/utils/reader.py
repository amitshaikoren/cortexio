import gzip
#TODO: import relevant


class Reader:
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        pass

def _get_user_information(path_to_snapshot):
    with open(path_to_snapshot, 'rb') as snapshot_fd:
        snapshot_fd.read()



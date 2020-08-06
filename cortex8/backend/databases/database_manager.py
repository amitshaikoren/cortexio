from urllib.parse import urlparse
from cortex8.utils import load_drivers


drivers = load_drivers("database_drivers")


class DatabaseManager:
    def __init__(self, url):
        parsed_url = urlparse(url)
        scheme, host, port = parsed_url.scheme, parsed_url.host, parsed_url.port
        self.db = drivers[scheme](host, port)

    def __repr__(self):
        return self.db.__repr__()

    def insert_user(self, user):
        self.db.insert_user(user)

    def insert_results(self, data):
        self.db.insert_results(data)

    def get_users(self):
        return self.db.get_users()

    def get_user_by_id(self, user_id):
        return self.db.get_user_by_id(user_id)

    def get_snapshots_by_user_id(self, user_id):
        return self.db.get_snapshots_by_user_id(user_id)

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return self.db.get_snapshot_by_id(user_id, snapshot_id)

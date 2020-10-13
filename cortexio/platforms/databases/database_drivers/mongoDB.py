import pymongo


class MongoDatabase:
    scheme = 'mongodb'

    def __init__(self, host, port):
        self.address = f'{host}:{port}'
        self.client = pymongo.MongoClient(host, int(port))
        self.db = self.client["db"]
        self.users = self.db["users"]
        self.snapshots = self.db["snapshots"]

        # TODO: test connection

    def __repr__(self):
        return f'MongoDB({self.address})'

    def insert_user(self, user):
        self.users.update_one({'user_id': user['user_id']}, {'$set': user}, upsert=True)

    def insert_results(self, data):
        self.snapshots.update_one({'snapshot_id': data['snapshot_id']},
                                  [{'$set': data}], upsert=True)

    def get_users(self):
        return list(self.users.find({}, {'_id': 0}))

    def get_user_by_id(self, user_id):
        return self.users.find_one({'user_id': user_id}, {'_id': 0})

    def get_snapshots_by_user_id(self, user_id):
        return list(self.snapshots.find({'user_id': user_id}, {'_id': 0}))

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return self.snapshots.find_one({'snapshot_id': snapshot_id, 'user_id': str(user_id)}, {'_id': 0})

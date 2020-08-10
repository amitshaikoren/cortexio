import flask

import json

from cortex8.backend.protocols import ProtocolManager
from cortex8.backend.messageQ import MessageQManager
from cortex8.backend.databases import DatabaseManager
from cortex8 import CLIENT_SERVER_PROTOCOL, SERVER_MQ_PROTOCOL, SERVER_SNAPSHOT_PATH, DEFAULT_DATABASE_URL


app = flask.Flask(__name__)
db = None
client_server_protocol = ProtocolManager("json")

def run_api_server(host, port, database_url):

    global db
    db = DatabaseManager(database_url)

    app.run(host=host, port=port)


@app.route("/users", methods=['GET'])
def get_users():
    # Todo: dont like this global
    global db
    #Todo: use protocol manager instead of json.dumps explicitly
    return json.dumps(db.get_users())

@app.route("/users/<user_id>", methods=['GET'])
def get_user_by_id():
    global db
    # Todo: use protocol manager instead of json.dumps explicitly
    return json.dumps(db.get_user_by_id())

# TODO: mock tests with mock clients

if __name__ == "__main__":
    run_api_server("127.0.0.1", 7000, DEFAULT_DATABASE_URL)
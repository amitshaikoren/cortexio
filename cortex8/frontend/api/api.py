import flask


from cortex8.backend.protocols import ProtocolManager
from cortex8.backend.messageQ import MessageQManager
from cortex8.backend.databases import DatabaseManager
from cortex8 import CLIENT_SERVER_PROTOCOL, SERVER_MQ_PROTOCOL, SERVER_SNAPSHOT_PATH, DEFAULT_DATABASE_URL
from flask import jsonify

app = flask.Flask(__name__)
db = None
client_server_protocol = ProtocolManager("json")

def run_api_server(host, port, database_url):

    global db
    db = DatabaseManager(database_url)

    app.run(host=host, port=port)

#TODO: make jsonify call prettier
@app.route("/users", methods=['GET'])
def get_users():
    data = db.get_users()
    users = [(user["user_id"], user["username"]) for user in data]
    return jsonify(users)


@app.route("/users/<int:user_id>", methods=['GET'])
def get_user_by_id(user_id):
    data = db.get_user_by_id(user_id)
    return jsonify(data)


@app.route("/users/<int:user_id>/snapshots", methods=['GET'])
def get_snapshots_by_user_id(user_id):
    data = db.get_snapshots_by_user_id(user_id)
    return jsonify(data)


@app.route("/users/<user_id>/snapshots/<snapshot_id>", methods=['GET'])
def get_snapshot_by_id(user_id, snapshot_id):
    data = db.get_snapshot_by_id(user_id, snapshot_id)
    return jsonify(data)

#TODO: implement
#@app.route("/users/<user_id>/snapshots/<snapshot_id>/<result_name>", methods=['GET'])
#def get_snapshot_by_id(user_id, snapshot_id, result_name):
 #   data = db.get_snapshot_by_id(user_id, snapshot_id)
   # return client_server_protocol.serialize(data)

# TODO: mock tests with mock clients

if __name__ == "__main__":
    run_api_server("127.0.0.1", 7000, DEFAULT_DATABASE_URL)

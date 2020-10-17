import flask


from cortexio.platforms.protocols import ProtocolManager
from cortexio.platforms.databases import DatabaseManager
from cortexio import API_DB_PROTOCOL, DEFAULT_DATABASE_URL
from flask import jsonify, send_file

app = flask.Flask(__name__)
db = None
client_server_protocol = ProtocolManager(API_DB_PROTOCOL)


def run_api_server(host, port, database_url):

    global db
    db = DatabaseManager(database_url)

    app.run(host=host, port=port)


def _wrap_response(data):
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#TODO: make jsonify call prettier
@app.route("/users", methods=['GET'])
def get_users():
    data = db.get_users()
    users = [(user["user_id"], user["username"]) for user in data]
    return _wrap_response(users)


@app.route("/users/<int:user_id>", methods=['GET'])
def get_user_by_id(user_id):
    data = db.get_user_by_id(user_id)
    return _wrap_response(data)


@app.route("/users/<user_id>/snapshots", methods=['GET'])
def get_snapshots_by_user_id(user_id):
    data = db.get_snapshots_by_user_id(user_id)
    return _wrap_response(data)


@app.route("/users/<int:user_id>/snapshots/<snapshot_id>", methods=['GET'])
def get_snapshot_by_id(user_id, snapshot_id):
    data = db.get_snapshot_by_id(user_id, snapshot_id)
    return _wrap_response(data)


@app.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>')
def get_snapshot_result(user_id, snapshot_id, result_name):
    result = db.get_snapshot_by_id(user_id, snapshot_id)['results'][result_name]
    return _wrap_response(result)


@app.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>/data')
def get_snapshot_result_data(user_id, snapshot_id, result_name):
    path = db.get_snapshot_by_id(user_id, snapshot_id)['results'][result_name]['data_path']
    return send_file(path)

# TODO: mock tests with mock clients


if __name__ == "__main__":
    run_api_server("0.0.0.0", 7000, DEFAULT_DATABASE_URL)

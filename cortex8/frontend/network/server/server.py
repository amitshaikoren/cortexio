import threading
import flask
import requests

from cortex8.backend.protocols.protocol_manager import ProtocolManager
from cortex8.backend.messageQ.messageQ_manager import MessageQManager


app = flask.Flask(__name__)
url = None
CLIENT_SERVER_PROTOCOL = "protobuf"
SERVER_MQ_PROTOCOL = "json"

def run_server(host, port, publish):
    # TODO: understand what to do with publish
    app.run(host=host, port=port)


@app.route('/snapshot', methods=['POST'])
def post_snapshot():
    client_server_protocol = ProtocolManager(CLIENT_SERVER_PROTOCOL)
    server_mq_protocol = ProtocolManager(SERVER_MQ_PROTOCOL)

    # TODO: https://tedboy.github.io/flask/generated/generated/flask.Request.get_data.html here it says
    #       it's a bad idea to call method without checking the content length
    #       Idea for security implementation
    # TODO: Consider setting get_data cache parameter to false
    client_data = flask.Request.get_data()
    user, snapshot = client_server_protocol.deserialize(client_data)

    user_dict, snapshot_dict = client_server_protocol.convert_to_python_dict(user, snapshot)
    publishable_user, publishable_snapshot = server_mq_protocol.serialize(user_dict, snapshot_dict)

    mq = MessageQManager(url)
    mq.publish("user", publishable_user)
    mq.publish("snapshot", publishable_snapshot)

    # TODO: return viable template
    return ""


_
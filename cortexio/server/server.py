import flask

import json

from cortexio.platforms.protocols import ProtocolManager
from cortexio.platforms.messageQ import MessageQManager
from cortexio.utils import FileSystemManager as FSM
from cortexio import CLIENT_SERVER_PROTOCOL, SERVER_MQ_PROTOCOL, SERVER_SNAPSHOT_PATH


app = flask.Flask(__name__)
url = None
handler = None

# TODO: replace url argument with optional cli argument, for now its just for testing
def run_server(host, port, publish=None, mq_url="rabbitmq://0.0.0.0:5672/"):
    if publish:
        global handler
        handler = publish

    global url
    url = mq_url

    app.run(host=host, port=port)


@app.route("/" + SERVER_SNAPSHOT_PATH, methods=['POST'])
def post_snapshot():
    client_server_protocol = ProtocolManager(CLIENT_SERVER_PROTOCOL)
    server_mq_protocol = ProtocolManager(SERVER_MQ_PROTOCOL)

    # TODO: https://tedboy.github.io/flask/generated/generated/flask.Request.get_data.html here it says
    #       it's a bad idea to call get_data() method without checking the content length
    #       Idea for security implementation
    # TODO: Consider setting get_data cache parameter to false
    client_data = flask.request.get_data()
    user, snapshot = client_server_protocol.deserialize(client_data)

    if handler:
        # TODO: really dont like this, need to understand more clearly what this handler needs to do
        handler(user, snapshot)
        # TODO: return viable template
        return ""

    user_dict, snapshot_dict = client_server_protocol.convert_to_python_dict(user, snapshot)
    publishable_user, publishable_snapshot = server_mq_protocol.serialize(user_dict, snapshot_dict)

    color_image_data = snapshot.color_image.data
    # TODO: why not serialize also color_image
    # TODO: fix serialize and use that instead of json dumps, figure out why encode is needed
    depth_image_data = json.dumps(list(snapshot.depth_image.data)).encode("utf-8")
    # TODO: dont like how arguments are delivered to function here, fix with how we use snapshot_dict
    FSM.save(color_image_data, snapshot_dict['color_image_path'])
    FSM.save(depth_image_data, snapshot_dict['depth_image_path'])

    mq = MessageQManager(url)
    # TODO: consider relevant exception
    mq.publish("user", publishable_user)
    mq.publish("snapshot", publishable_snapshot)

    # TODO: return viable template
    return ""

if __name__ == "__main__":
    run_server("0.0.0.0", 8080)

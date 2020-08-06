import flask

from cortex8.backend.protocols import ProtocolManager
from cortex8.backend.messageQ import MessageQManager
from cortex8.utils import FileSystemManager as FSM


CLIENT_SERVER_PROTOCOL = "protobuf"
SERVER_MQ_PROTOCOL = "json"

app = flask.Flask(__name__)
url = None
handler = None


def run_server(host, port, publish=None):
    if publish:
        global handler
        handler = publish

    app.run(host=host, port=port)


@app.route('/snapshot', methods=['POST'])
def post_snapshot():
    client_server_protocol = ProtocolManager(CLIENT_SERVER_PROTOCOL)
    server_mq_protocol = ProtocolManager(SERVER_MQ_PROTOCOL)

    # TODO: https://tedboy.github.io/flask/generated/generated/flask.Request.get_data.html here it says
    #       it's a bad idea to call get_data() method without checking the content length
    #       Idea for security implementation
    # TODO: Consider setting get_data cache parameter to false
    client_data = flask.Request.get_data()
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
    depth_image_data = server_mq_protocol.serialize(list(snapshot.depth_image.data))
    # TODO: dont like how arguments are delivered to function here, fix with how we use snapshot_dict
    FSM.save(color_image_data, snapshot_dict['color_image_path'])
    FSM.save(depth_image_data, snapshot_dict['depth_image_path'])

    mq = MessageQManager(url)
    # TODO: consider relevant exception
    mq.publish("user", publishable_user)
    mq.publish("snapshot", publishable_snapshot)

    # TODO: return viable template
    return ""
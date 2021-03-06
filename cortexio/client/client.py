# TODO: make import prettier
from cortexio.client.utils import Reader
from cortexio.platforms.protocols import ProtocolManager
from cortexio import CLIENT_SERVER_PROTOCOL, SERVER_SNAPSHOT_PATH
import requests

# TODO: delete import
from cortexio import SAMPLE_PATH_MAC, SAMPLE_PATH_LINUX



def upload_sample(host, port, data_path):
    url = f'http://{host}:{port}/{SERVER_SNAPSHOT_PATH}'
    with Reader(data_path) as reader:
        user = reader.get_user()
        for snapshot in reader:
            protocol = ProtocolManager(CLIENT_SERVER_PROTOCOL)
            response = requests.post(url=url, data=protocol.serialize(user, snapshot))
            # TODO: handle bad response



# TODO: make import prettier
from cortex8.frontend.network.client.utils import Reader
from cortex8.backend.protocols import ProtocolManager
from cortex8 import CLIENT_SERVER_PROTOCOL, SERVER_SNAPSHOT_PATH
import requests
import click
import json
import typing
import urllib

# TODO: delete import
from cortex8 import SAMPLE_PATH_LINUX, SAMPLE_PATH_MAC



def upload_sample(host, port, data_path):
    with Reader(data_path) as reader:
        user = reader.get_user()
        for snapshot in reader:
            url = f'http://{host}:{port}/{SERVER_SNAPSHOT_PATH}'
            protocol = ProtocolManager(CLIENT_SERVER_PROTOCOL)
            response = requests.post(url=url, data=protocol.serialize(user, snapshot))
            # TODO: handle bad response

if __name__== "__main__":
    upload_sample("127.0.0.1", 8080, SAMPLE_PATH_LINUX)

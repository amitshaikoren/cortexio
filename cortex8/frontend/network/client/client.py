from .utils import Reader
from cortex8.backend.protocols import ProtocolManager
import requests
import click
import json
import typing


PROTOCOL = "protobuf"

def upload_sample(host, port, data_path):
    with Reader(data_path) as reader:
        user = reader.get_user()
        for snapshot in reader:
            url = f'http://{host}:{port}/snapshot'
            protocol = ProtocolManager(PROTOCOL)
            response = requests.post(url=url, data=protocol.serialize(user, snapshot))

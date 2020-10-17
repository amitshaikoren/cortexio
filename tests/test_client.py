import pytest
import requests
from cortexio.client import upload_sample
from cortexio.platforms.protocols import ProtocolManager
from cortexio import CLIENT_SERVER_PROTOCOL


client_server_protocol = ProtocolManager(CLIENT_SERVER_PROTOCOL)

def test_send_snapshot(data_dir, requests_post_data):
    sample = data_dir / 'snapshot.gz'
    upload_sample('0.0.0.0', 12345, sample)

    message = requests_post_data[0]
    user, snapshot = client_server_protocol.deserialize(message)

    assert user.user_id == 42
    assert user.username == 'Dan Gittik'
    assert snapshot.feelings.happiness == 0
    assert snapshot.pose.rotation.x == -0.10888676356214629


@pytest.fixture
def requests_post_data(monkeypatch):
    post_message = []

    class MockResponse:
        status_code = 200

    def mock_post(url, data):
        post_message.append(data)
        return MockResponse()

    monkeypatch.setattr(requests, 'post', mock_post)
    return post_message



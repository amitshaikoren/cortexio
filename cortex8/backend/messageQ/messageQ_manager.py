from urllib.parse import urlparse
from cortex8.utils.utils_functions import load_drivers


drivers = load_drivers("messageQ_drivers")


class MessageQManager:
    def __init__(self, url):
        parsed_url = urlparse(url)
        self.host = parsed_url.hostname
        self.port = parsed_url.port
        self.scheme = parsed_url.scheme
        self.driver = drivers[self.scheme](self.port, self.host)

    def publish(self, topic, handler):
        self.driver.publish(topic, handler)

    def consume(self, topic, handler):
        self.driver.consume(topic, handler)

from urllib.parse import urlparse
from cortexio.utils import load_drivers

# TODO: consider moving load_drivers into the class, why does it need to operate when the module loads?
# TODO: to add in documentation: any time a driver is made, we need to add it in the ___drivers __init__ file
drivers = load_drivers("messageQ_drivers")


class MessageQManager:
    def __init__(self, url):
        parsed_url = urlparse(url)
        self.host = parsed_url.hostname
        self.port = parsed_url.port
        self.scheme = parsed_url.scheme
        self.driver = drivers[self.scheme](self.host, self.port)

    def publish(self, topic, handler):
        self.driver.publish(topic, handler)

    def consume(self, topic, handler):
        self.driver.consume(topic, handler)

if __name__ == "__main__":
    drivers = load_drivers("messageQ_drivers")
    print(drivers)

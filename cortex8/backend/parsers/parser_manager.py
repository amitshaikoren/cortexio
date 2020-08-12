import typing
import threading
from cortex8.utils import load_drivers
from cortex8.backend.messageQ import MessageQManager
from cortex8.backend.parsers.encoders import EncodingManager
from cortex8 import DEFAULT_MESSAGEQ_URL

# TODO: change to a new driver/manager mechanism
import json

# TODO: reorganize module and decouple things

drivers = load_drivers("parser_drivers")

encoding = EncodingManager("json")

parsers =  {
    'pose',
    'feeling',
    'color_image',
    'depth_image'
}

# TODO: use previously mentioned class and implement __getitem_ in order to get elements
def _prepare_to_publish_data(topic, parsed_data, snapshot):
    snapshot_dict = encoding.decode(snapshot)
    data_dict = encoding.decode(parsed_data)

    # TODO: add functionality of __getitem__ to encoding because its not always a dict - need to decouple
    datetime = snapshot_dict["datetime"]
    snapshot_id = snapshot_dict["snapshot_id"]
    user_id = snapshot_dict["user_id"]

    metadata = dict(datetime=datetime, snapshot_id=snapshot_id, user_id=user_id)
    prepared_data = dict(**metadata, results={topic: data_dict})

    return json.dumps(prepared_data)


class ParserManager:
    def __init__(self, parser_name):
        self.parser_driver = drivers[parser_name]

    def parse(self, data):
        try:
            # TODO: not pretty
            data = data.decode("utf-8")
            decoded_data = json.loads(data)
            parsed_data = self.parser_driver.parse(decoded_data)
            encoded_data = json.dumps(parsed_data)
            return encoded_data
        # TODO: except relevant exception if data is not able to be decoded
        except:
            return self.parser_driver.parse(decoded_data)


def run_parser(parser_name, data):
    parser = ParserManager(parser_name)
    return parser.parse(data)


# TODO: move to somewhere that makes more sense: decouple parser manager from messageQ
def consume_publish_with_parser(parser_name, mq_url):
    mq = MessageQManager(mq_url)

    def handler(snapshot):
        parsed_data = run_parser(parser_name, snapshot)
        publishable_data = _prepare_to_publish_data(parser_name, parsed_data, snapshot)
        mq.publish(parser_name, publishable_data)

    mq.consume('snapshot', handler)


def run_parsers():
    for parser in parsers:
        t = threading.Thread(target=consume_publish_with_parser, args=(parser, DEFAULT_MESSAGEQ_URL))
        t.start()


if __name__ == "__main__":
    run_parsers()

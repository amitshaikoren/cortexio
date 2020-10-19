import typing
import threading
from cortexio.utils import load_drivers
from cortexio.platforms.messageQ import MessageQManager
from cortexio import DEFAULT_MESSAGEQ_URL

# TODO: change to a new driver/manager mechanism
import json

# TODO: reorganize module and decouple things

drivers = load_drivers("parser_drivers")


#encoding = EncodingManager("json")

parsers =  {
    'pose',
    'feelings',
    'color_image',
    'depth_image'
}

# TODO: use previously mentioned class and implement __getitem_ in order to get elements
def _prepare_to_publish_data(topic, parsed_data, snapshot):
    # TODO: change this json shit
    snapshot_dict = json.loads(snapshot)

    # TODO: add functionality of __getitem__ to encoding because its not always a dict - need to decouple
    datetime = snapshot_dict["datetime"]
    snapshot_id = snapshot_dict["snapshot_id"]
    user_id = snapshot_dict["user_id"]

    metadata = dict(datetime=datetime, snapshot_id=snapshot_id, user_id=user_id)
    prepared_data = dict(**metadata, results={topic: parsed_data})

    # TODO: change this json shit to something more general in case protocol changes
    return json.dumps(prepared_data)


class ParserManager:
    def __init__(self, parser_name):
        self.parser_driver = drivers[parser_name]

    def parse(self, data):
            decoded_data = json.loads(data)
            parsed_data = self.parser_driver.parse(decoded_data)
            return json.dumps(parsed_data)


def parse(parser_name, data):
    parser = ParserManager(parser_name)
    return parser.parse(data)


# TODO: move to somewhere that makes more sense: decouple parser manager from messageQ
def consume_publish_with_parser(parser_name, mq_url):
    mq = MessageQManager(mq_url)

    def handler(snapshot):
        parsed_data = json.loads(parse(parser_name, snapshot))
        publishable_data = _prepare_to_publish_data(parser_name, parsed_data, snapshot)
        mq.publish(parser_name, publishable_data)

    mq.consume('snapshot', handler)


def run_parsers(mq_url):
    for parser in parsers:
        t = threading.Thread(target=consume_publish_with_parser, args=(parser, mq_url))
        t.start()





# TODO: PROBLEM with messageQ: if message was sent and handler failed
#       then message is lost and has to be sent again by client.

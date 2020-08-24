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
    'feeling',
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

    # TODO: change this json shit
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


def parse(parser_name, data):
    parser = ParserManager(parser_name)
    return parser.parse(data)


# TODO: move to somewhere that makes more sense: decouple parser manager from messageQ
def consume_publish_with_parser(parser_name, mq_url):
    mq = MessageQManager(mq_url)

    def handler(snapshot):
        parsed_data = parse(parser_name, snapshot)
        publishable_data = _prepare_to_publish_data(parser_name, parsed_data, snapshot)
        mq.publish(parser_name, publishable_data)

    mq.consume('snapshot', handler)


def run_parsers():
    for parser in parsers:
        t = threading.Thread(target=consume_publish_with_parser, args=(parser, DEFAULT_MESSAGEQ_URL))
        t.start()



if __name__ == "__main__":
    run_parsers()



# TODO: PROBLEM with messageQ: if message was sent and handler failed
#       then message is lost and has to be sent again by client.
#       For some reason, parser has to be running before message is sent by client... weird.
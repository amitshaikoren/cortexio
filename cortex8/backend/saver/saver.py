import threading

from cortex8.backend.databases import DatabaseManager
from cortex8.backend.protocols import ProtocolManager
from cortex8.backend.messageQ import MessageQManager
from cortex8.backend.parsers import parsers
from cortex8 import SAVER_MQ_PROTOCOL

serializer = ProtocolManager(SAVER_MQ_PROTOCOL)


class Saver:
    def __init__(self, db_url):
        self.db = DatabaseManager(db_url)

    def save(self, topic, data):
        deserialized_data = serializer.deserialize(data)

        if topic == "user":
            self.db.insert_user(deserialized_data)
        else:
            self.db.insert_results(deserialized_data)

    def run_saver(self, topic, mq_url):
        mq = MessageQManager(mq_url)

        def handler(data):
            self.save(data)

        mq.consume(topic, handler)

    def run_all_savers(self, mq_url):
        for parser in parsers:
            thread = threading.Thread(target=self.run_saver, args=(parser, mq_url))
            thread.start()

        # thread for user topic
        thread = threading.Thread(target=self.run_saver, args=("user", mq_url))
        thread.start()

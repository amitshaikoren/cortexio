from cortex8.backend.parsers.encoders.encoding_manager import EncodingManager
from cortex8 import PARSER_MQ_PROTOCOL

encoding = EncodingManager(PARSER_MQ_PROTOCOL)


class FeelingsParser:
    scheme = "feelings"

    def __init__(self, snapshot):
        self.snapshot = encoding.decode(snapshot)

    def parse(self):

        feelings = dict(
            hunger=self.snapshot["feelings_hunger"],
            thirst=self.snapshot["feelings_thirst"],
            exhaustion=self.snapshot["feelings_exhaustion"],
            happiness=self.snapshot["feelings_happiness"]
        )

        return feelings

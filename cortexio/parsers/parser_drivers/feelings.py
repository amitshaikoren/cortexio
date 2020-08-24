from cortexio.parsers.encoders import EncodingManager
from cortexio import PARSER_MQ_PROTOCOL

# TODO: encoding?
encoding = EncodingManager(PARSER_MQ_PROTOCOL)


class FeelingsParser:
    scheme = "feelings"

    @staticmethod
    def parse(snapshot):
        feelings = dict(
            hunger=snapshot["feelings_hunger"],
            thirst=snapshot["feelings_thirst"],
            exhaustion=snapshot["feelings_exhaustion"],
            happiness=snapshot["feelings_happiness"]
        )

        return feelings

import collections
from cortex8.utils.utils_functions import load_drivers


# TODO: consider deleting this module



drivers = load_drivers("encoding_drivers")


# TODO: implementation idea: perhaps intorduce a new class that EncodingManager will use
#       and will be a field in encoding manager if its given as a parameter

class EncodingManager:
    def __init__(self, scheme, data=""):
        self.driver = drivers[scheme]()
        # TODO: not sure if this is best practice, because data is not necessarily encoded
        self.decoded_data = self.decode(data)

    def encode(self, raw_data):
        return self.driver.encode(raw_data)

    def decode(self, raw_data):
        return self.driver.decode(raw_data)

    # TODO: implement __getitem__
    # def __getitem__(self, item):
        # TODO: make sure if collections.Sequence is the correct data type to use
        # if isinstance(self.decoded_data, collections.Sequence):
            # return self.decoded_data.__getitem__(item)

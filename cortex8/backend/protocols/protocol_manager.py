from cortex8.utils import load_drivers


drivers = load_drivers("protocol_drivers")


class ProtocolManager:
    def __init__(self, protocol_manager_scheme):
        self.protocol_driver = drivers[protocol_manager_scheme]()

    def serialize(self, user="", snapshot="", raw_data=""):
        return self.protocol_driver.serialize(user, snapshot, raw_data)

    def deserialize(self, data):
        return self.protocol_driver.deserialize(data)

    def convert_to_python_dict(self, user, snapshot):
        return self.protocol_driver.convert_to_python_dict(user, snapshot)

    def convert_from_python_dict(self, user_dict, snapshot_dict):
        return self.protocol_driver.convert_from_python_dict(user_dict, snapshot_dict)


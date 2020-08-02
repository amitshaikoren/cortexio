from cortex8.utils.utils_functions import load_drivers


drivers = load_drivers("protocol_drivers")


class ProtocolManager:
    def __init__(self, protocol_manager_scheme):
        self.protocol_manager = drivers[protocol_manager_scheme]()

    def serialize(self, user, snapshot):
        return self.protocol_manager.serilize(user, snapshot)

    def deserialize(self, data):
        return self.protocol_manager.deserizile(data)

import matplotlib.pyplot as plt
import pathlib
from cortex8.backend.protocols import ProtocolManager
from cortex8.utils import FileSystemManager as FSM
from cortex8 import PARSER_MQ_PROTOCOL, BASE_SNAPSHOT_IMAGE_PATH

serializer = ProtocolManager(PARSER_MQ_PROTOCOL)


class ColorImageParser:
    scheme = "depth_image"

    def __init__(self, snapshot):
        self.snapshot = serializer.deserialize(snapshot)

    def parse(self):
        width = self.snapshot["depth_image_width"]
        height = self.snapshot["depth_image_height"]
        size = width, height

        path = self.snapshot["depth_image_path"]
        # TODO: perhaps need to serialize
        depth_image_data_stream = FSM.load(path)

        # TODO: is user_id really necessary to be included in the snapshot if we can use unique snapshot_id
        user_id = self.snapshot["user_id"]
        snapshot_id = self.snapshot["snapshot_id"]

        base_path = pathlib.Path(BASE_SNAPSHOT_IMAGE_PATH)
        image_path = base_path / user_id / snapshot_id / "depth_image.png"

        cb = plt.colorbar()
        cb.set_label('Distance from cortex')
        plt.hist2d(depth_image_data_stream[0], depth_image_data_stream[1], bins=100, normed=False, cmap='plasma')
        plt.title('Heatmap of image_depth')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')

        plt.savefig(image_path)

        return dict(image_path=image_path, image_width=width, image_height=height)
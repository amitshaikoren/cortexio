from cortex8.backend.protocols import ProtocolManager
from cortex8.utils import FileSystemManager as FSM
from PIL import Image
import pathlib
from cortex8 import PARSER_MQ_PROTOCOL, BASE_SNAPSHOT_IMAGE_PATH

serializer = ProtocolManager(PARSER_MQ_PROTOCOL)
BASE_PATH = './cortex8/gui/static/snapshot_images'


class ColorImageParser:
    scheme = "color_image"

    def __init__(self, snapshot):
        self.snapshot = serializer.deserialize(snapshot)

    def parse(self):
        width = self.snapshot["color_image_width"]
        height = self.snapshot["color_image_height"]
        size = width, height

        path = self.snapshot["color_image_path"]
        color_image_data_stream = FSM.load(path)

        # TODO: is user_id really necessary to be included in the snapshot if we can use unique snapshot_id
        user_id = self.snapshot["user_id"]
        snapshot_id = self.snapshot["snapshot_id"]

        base_path = pathlib.Path(BASE_SNAPSHOT_IMAGE_PATH)
        image_path = base_path / user_id / snapshot_id / "color_image.png"

        image = Image.frombytes('RGB', size, color_image_data_stream)
        FSM.save(image, image_path)

        return dict(image_path=image_path, image_width=width, image_height=height)




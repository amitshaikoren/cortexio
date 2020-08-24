from cortexio.platforms.protocols import ProtocolManager
from cortexio.utils import FileSystemManager as FSM
from PIL import Image
import pathlib
from cortexio import PARSER_MQ_PROTOCOL, BASE_SNAPSHOT_IMAGE_PATH
import logging

logger = logging.getLogger(__name__)

serializer = ProtocolManager(PARSER_MQ_PROTOCOL)

# TODO: delete
BASE_PATH = './cortexio/gui/static/snapshot_images'


class ColorImageParser:
    scheme = "color_image"

    @staticmethod
    def parse(snapshot):
        logger.debug("triggering color_image parser")

        width = snapshot["color_image_width"]
        height = snapshot["color_image_height"]
        size = width, height

        path = snapshot["color_image_path"]
        color_image_data_stream = FSM.load(path)

        # TODO: is user_id really necessary to be included in the snapshot if we can use unique snapshot_id
        user_id = snapshot["user_id"]
        snapshot_id = snapshot["snapshot_id"]

        base_path = pathlib.Path(BASE_SNAPSHOT_IMAGE_PATH)
        image_path = base_path / user_id / snapshot_id / "color_image.png"

        image = Image.frombytes('RGB', size, color_image_data_stream)

        #create path directiory
        image_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(image_path)

        return dict(image_path=str(image_path), image_width=width, image_height=height)




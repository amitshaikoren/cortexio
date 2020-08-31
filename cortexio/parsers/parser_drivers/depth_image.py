import matplotlib.pyplot as plt
import pathlib
from cortexio.platforms.protocols import ProtocolManager
from cortexio.utils import FileSystemManager as FSM
from cortexio import PARSER_MQ_PROTOCOL, BASE_SNAPSHOT_IMAGE_PATH
import numpy
import matplotlib

serializer = ProtocolManager(PARSER_MQ_PROTOCOL)


class DepthImageParser:
    scheme = "depth_image"

    @staticmethod
    def parse(snapshot):
        width = snapshot["depth_image_width"]
        height = snapshot["depth_image_height"]

        path = snapshot["depth_image_path"]

        # TODO: is user_id really necessary to be included in the snapshot if we can use unique snapshot_id
        user_id = snapshot["user_id"]
        snapshot_id = snapshot["snapshot_id"]

        fig_height, fig_width = _prepare_fig(width, height, path)

        base_path = pathlib.Path(BASE_SNAPSHOT_IMAGE_PATH)
        image_path = base_path / user_id / snapshot_id / "depth_image.png"
        image_path.parent.mkdir(parents=True, exist_ok=True)

        plt.savefig(image_path)

        return dict(data_path=str(image_path), image_width=fig_width, image_height=fig_height)


def _prepare_fig(width, height, path):
    size = height, width
    depth_image_data_stream = FSM.load(path)
    data = serializer.deserialize(depth_image_data_stream)

    shaped = numpy.reshape(data, size)
    fig = plt.imshow(shaped)

    coolwarm_colors = matplotlib.cm.coolwarm_r

    fig.set_cmap(coolwarm_colors)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    return fig.get_size()
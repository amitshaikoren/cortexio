import struct
import io
from .protobuf_data import User, Snapshot
import uuid
from cortex8.utils import epoch_to_datetime
import pathlib
from cortex8 import SERVER_PARSER_SHARED_DATA_DIR


UINT32_SIZE = 4



class ProtobufProtocol:
    scheme = "protobuf"

    # TODO: no need for raw_data, consider reimplmenting protocol_manager in a clever way
    # TODO: consider adding @staticmethod decorator if needed
    def serialize(self, user, snapshot, raw_data):
        user_data = user.SerializeToString()
        user_len = struct.pack('I', len(user_data))

        snapshot_data = snapshot.SerializeToString()
        snapshot_len = struct.pack('I', len(snapshot_data))

        serialized_msg = user_len + user_data + snapshot_len + snapshot_data
        return serialized_msg

    def deserialize(self, data):
        stream = io.BytesIO(data)

        user = User()
        user_len, = struct.unpack('I', stream.read(UINT32_SIZE))
        user_bytes = stream.read(user_len)
        user.ParseFromString(user_bytes)

        snapshot = Snapshot()
        snapshot_len, = struct.unpack('I', stream.read(UINT32_SIZE))
        snapshot_bytes = stream.read(snapshot_len)
        snapshot.ParseFromString(snapshot_bytes)

        return user, snapshot

    def convert_to_python_dict(self, deserialized_user, deserialized_snapshot):
        # TODO: reorganize function
        # TODO: Not very pretty, consider using a different design pattern to allow adding more fields easier
        user_dict = _protobuf_user_to_python_dict(deserialized_user)
        snapshot_dict = _protobuf_snapshot_to_python_dict(deserialized_snapshot)

        snapshot_dict['user_id'] = user_id = str(user_dict["user_id"])
        snapshot_dict['snapshot_id'] = snapshot_id = str(uuid.uuid4())

        image_dir_path = pathlib.Path(SERVER_PARSER_SHARED_DATA_DIR) / user_id / snapshot_id

        snapshot_dict["color_image_path"] = str(image_dir_path / "color_image.raw")
        snapshot_dict["depth_image_path"] = str(image_dir_path / "depth_image.raw")

        return user_dict, snapshot_dict

    def convert_from_python_dict(self, user_dict, snapshot_dict):
        # TODO: implement, not relevant for this project so this step is skipped.
        raise NotImplementedError()

######################################
# UTIL FUNCTIONS
######################################


def _protobuf_snapshot_to_python_dict(snapshot):
    d = dict()

    # TODO: Convert from epoch to datetime
    d["datetime"] = snapshot.datetime

    d["pose_translation_x"] = snapshot.pose.translation.x
    d["pose_translation_y"] = snapshot.pose.translation.y
    d["pose_translation_z"] = snapshot.pose.translation.z

    d["pose_rotation_x"] = snapshot.pose.rotation.x
    d["pose_rotation_y"] = snapshot.pose.rotation.y
    d["pose_rotation_z"] = snapshot.pose.rotation.z
    d["pose_rotation_w"] = snapshot.pose.rotation.w

    d["color_image_width"] = snapshot.color_image.width
    d["color_image_height"] = snapshot.color_image.height

    d["depth_image_width"] = snapshot.depth_image.width
    d["depth_image_height"] = snapshot.depth_image.height

    d["feelings_hunger"] = snapshot.feelings.hunger
    d["feelings_thirst"] = snapshot.feelings.thirst
    d["feelings_exhaustion"] = snapshot.feelings.exhaustion
    d["feelings_happiness"] = snapshot.feelings.happiness

    return d


def _protobuf_user_to_python_dict(user):
    d = dict()

    d["user_id"] = user.user_id
    d["username"] = user.username
    d["birthday"] = epoch_to_datetime(user.birthday, milisecs=True)
    d["gender"] = ['male', 'female', 'unknown'][user.gender]

    return d

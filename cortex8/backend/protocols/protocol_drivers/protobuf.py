"""
1. Do shit of protobuf
2. implement protobuf driver

"""
import struct
import io
from .protobuf_data import User, Snapshot
import uuid


UINT32_SIZE = 4


class ProtobufProtocol:
    scheme = "protobuf"

    def serialize(self, user, snapshot):
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
        raise NotImplementedError()

    def convert_from_python_dict(self, user_dict, snapshot_dict):
        # TODO: implement, not relevant for this project so this step is skipped.
        raise NotImplementedError()


######################################
# UTIL FUNCTIONS, NOT USED YET
######################################

def _snapshot_to_flat_dict(snapshot):
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


def _user_to_flat_dict(user):
    d = dict()

    d["user_id"] = user.user_id
    d["username"] = user.username
    d["birthday"] = user.birthday
    d["gender"] = user.gender

    return d


def _get_arranged_dicts(user, snapshot):
    # User Preparation
    user_dict = _user_to_flat_dict(user)

    user_dict['gender'] = ['male', 'female', 'unknown'][user.gender]
    user_dict['birthday'] = user.birthday

    # Snapshot Preparation
    snapshot_dict = _snapshot_to_flat_dict(snapshot)

    snapshot_dict['snapshot_id'] = snapshot_id = str(uuid.uuid4())
    snapshot_dict['user_id'] = user_id = user_dict["user_id"]

    image_dir_path = f'{server_mq_protocol.get_data_path()}/{user_id}/{snapshot_id}'
    snapshot_dict["color_image_path"] = f'{image_dir_path}/color_image.raw'
    snapshot_dict["depth_image_path"] = f'{image_dir_path}/depth_image.raw'

    return user_dict, snapshot_dict
from cortexio.parsers.encoders import EncodingManager
from cortexio import PARSER_MQ_PROTOCOL

encoding = EncodingManager(PARSER_MQ_PROTOCOL)

#TODO: consider changing parsers to functions instead of classes and changing load drivers accordingly

class PoseParser:
    scheme = "pose"

    @staticmethod
    def parse(snapshot):
        rotation = dict(
            x=snapshot["pose_rotation_x"],
            y=snapshot["pose_rotation_y"],
            z=snapshot["pose_rotation_z"],
            w=snapshot["pose_rotation_w"]
        )

        translation = dict(
            x=snapshot["pose_translation_x"],
            y=snapshot["pose_translation_y"],
            z=snapshot["pose_translation_z"]
        )

        return dict(rotation=rotation, translation=translation)

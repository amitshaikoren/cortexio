from cortex8.backend.parsers.encoders.encoding_manager import EncodingManager


encoding = EncodingManager("json")


class PoseParser:
    scheme = "pose"

    def __init__(self, snapshot):
        self.snapshot = encoding.decode(snapshot)

    def parse(self):
        rotation = dict(
            x=self.snapshot["pose_rotation_x"],
            y=self.snapshot["pose_rotation_y"],
            z=self.snapshot["pose_rotation_z"],
            w=self.snapshot["pose_rotation_w"]
        )

        translation = dict(
            x=self.snapshot["pose_translation_x"],
            y=self.snapshot["pose_translation_y"],
            z=self.snapshot["pose_translation_z"]
        )

        return dict(rotation=rotation, translation=translation)

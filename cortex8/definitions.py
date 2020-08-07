"""insert useful project variables that can easily be changed if necessary"""

#######################
# GENERAL
#######################
PROJECT_NAME = "cortex8"

#######################
# PROTOCOLS
#######################
CLIENT_SERVER_PROTOCOL = "protobuf"
SERVER_MQ_PROTOCOL = "json"
PARSER_MQ_PROTOCOL = "json"
SAVER_MQ_PROTOCOL = "json"

#######################
# PATHS
#######################
SERVER_SNAPSHOT_PATH = "snapshot"
BASE_SNAPSHOT_IMAGE_PATH = f'./{PROJECT_NAME}/gui/static/snapshot_images'

#######################
# LOCAL TESTS PRE PRODUCTION
#######################
SAMPLE_PATH_LINUX = "/home/user/Downloads/exercise7/sample.mind.gz"
SAMPLE_PATH_MAC = "/Users/apple/Desktop/Advanced_System_Design/Exercise_7/sample.mind.gz"

"""insert useful project variables that can easily be changed if necessary"""

#######################
# GENERAL
#######################
PROJECT_NAME = "cortex8"

#######################
# PROTOCOLS
#######################
# Options: "protobuf", "json"

CLIENT_SERVER_PROTOCOL = "protobuf"
SERVER_MQ_PROTOCOL = "json"
PARSER_MQ_PROTOCOL = "json"
SAVER_MQ_PROTOCOL = "json"

#######################
# PATHS
#######################
SERVER_SNAPSHOT_PATH = "snapshot"
BASE_SNAPSHOT_IMAGE_PATH = f'./{PROJECT_NAME}/gui/static/snapshot_images'
SERVER_PARSER_SHARED_DATA_DIR = f'./{PROJECT_NAME}/data/shared_data'

#######################
# URLS
#######################
DEFAULT_MESSAGEQ_URL = "rabbitmq://127.0.0.1:5672/"
DEFAULT_DATABASE_URL = "mongodb://127.0.0.1:27017"

#######################
# LOCAL TESTS PRE PRODUCTION
#######################
SAMPLE_PATH_LINUX = "/home/user/Downloads/exercise7/sample.mind.gz"
SAMPLE_PATH_MAC = "/Users/apple/Desktop/Advanced_System_Design/Exercise_7/sample.mind.gz"

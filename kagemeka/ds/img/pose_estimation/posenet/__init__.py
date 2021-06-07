from .constants import *
from .decode_multi import decode_multiple_poses
from .model import load_model
from .utils import *

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


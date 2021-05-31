from .color_generator import (
  ColorGenerator,
)


from .types import (
  FrameSz,
)
'''cv2 resize interpolation 
caution: x, y is vice verse
  img_shape: (h, w, 3)
  dsize: (w, h)

Enlarge 
- cv2.INTER_LINEAR 
- cv2.INTER_CUBIC 

Shrink 
- cv2.INTER_AREA 
'''


from .img_proc import (
  ImgProc,
)

from tensorflow \
  .keras \
  .applications \
  .vgg16 import (
  VGG16,
)

from .video_props import (
  VideoProps,
  ChangeProps,
)


from .video import (
  Video,
)

from .video_proc import (
  VideoProc,
)


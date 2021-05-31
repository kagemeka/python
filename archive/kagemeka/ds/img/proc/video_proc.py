import cv2 


from ....gen import (
  PathManager as PM, 
  VideoFormats as VF,
)


from \
  moviepy \
  .editor \
import (
  VideoFileClip,
)


from \
  typing \
import (
  Tuple,
  NoReturn,
)

from \
  . \
import (
  ImgProc as IP,
  FrameSz,
  Video,
)

from tqdm import (
  trange,
)

from \
  datetime \
import (
  datetime as dt,
  time,
)


from \
  ... \
import (
  AudioProc as AP,
)


class VideoProc:

  @staticmethod 
  def to_frames(
    src_vid: str,
    dst_dir: str,
  ) -> NoReturn:
    ok = VF.assert_fmt(src_vid)
    if not ok:
      return
    v = Video.make(
      src=src_vid,
    )
    n = v.src_props.frame_cnt
    i = 0
    
    for _ in trange(n):
      frame = v.read()
      if frame is None:
        continue
      dst = (
        f'{dst_dir}/'
        f'{i:06}.png'
      )
      IP.save(
        path=dst,
        img=frame,
      )
      i += 1
    v.release()


  @classmethod 
  def make_writer(
    cls,
    video: Video,
  ) -> cv2.VideoWriter:
    v = video
    assert v.writer is None
    props = v.dst_props
    assert props is not None
    dst = v.dst
    fourcc = cls.fourcc(dst)
    if fourcc is None:
      return None
    fps = props.fps 
    size = (*props.size,)
    writer = cv2.VideoWriter(
      dst,
      fourcc, 
      fps,
      frameSize=size,
    )
    return writer


  @staticmethod 
  def fourcc(
    dst: str,
  ) -> int:

    ok = VF.assert_fmt(
      path=dst,
    )
    if not ok:
      return None
    fmt = VF.get_fmt(dst)
    f = fmt.fourcc.name
    f = cv2.VideoWriter_fourcc(
      *f,
    )
    return f
  


  @staticmethod 
  def crop(
    src: str,
    start: int,
    end: int,
    dst: str,
  ) -> NoReturn:
    for f in (src, dst):
      if VF.assert_fmt(f):
        continue
      return
    clip = VideoFileClip(src)
    clip = clip.subclip(
      start,
      end,
    )
    PM.prepare_dir(dst)
    clip.write_videofile(dst)


  @staticmethod 
  def to_audio(
    src: str,
    dst: str,
  ) -> NoReturn:
    AP.from_video(
      src,
      dst,
    )
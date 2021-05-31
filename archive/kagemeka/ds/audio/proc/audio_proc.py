from moviepy.editor import (
  VideoFileClip,
  AudioFileClip,
)

from ....gen import (
  PathManager as PM,
  VideoFormats as VF,
  AudioFormats as AF, 
)

from pydub import (
  AudioSegment as AS,
)

from typing import (
  NoReturn,
)



class AudioProc:
  ...

  @classmethod
  def from_video(
    cls,
    src: str,
    dst: str,
  ) -> None:
    clip = cls.video_clip(src)
    if clip is None:
      return

    ok = AF.assert_fmt(dst)
    if not ok:
      return
    
    PM.prepare_dir(dst)
    clip.audio.write_audiofile(
      dst,
    )


  @classmethod
  def video_clip(
    cls,
    path: str,
  ) -> VideoFileClip:
    ok = VF.assert_fmt(path)
    if not ok:
      return
    clip = VideoFileClip(path)
    return clip
    
  
  @classmethod
  def convert(
    cls,
    src: str,
    dst: str,
  ) -> NoReturn:
    seg = cls.load_seg(src)
    if seg is None:
      return
    
    cls.save_seg(seg, dst)


  @classmethod 
  def load_seg(
    cls,
    path: str,
  ) -> AS:
    ok = AF.assert_fmt(path)
    if not ok:
      return
    
    ext = PM.ext(path)
    seg = AS.from_file(
      file=path,
      format=ext,
    )
    # seg.set_channels()
    return seg 
  

  @classmethod 
  def save_seg(
    cls,
    seg: AS,
    path: str,
  ) -> NoReturn:
    ok = AF.assert_fmt(path)
    if not ok:
      return 
    
    ext = PM.ext(path)
    PM.prepare_dir(path)
    seg.export(
      out_f=path,
      format=ext,
    )

  
  @classmethod 
  def crop(
    cls,
    src: str,
    start: int,
    end: int,
    dst: str,
  ) -> NoReturn:
    seg = cls.load_seg(src)
    if seg is None:
      return 
    
    seg = seg[start:end]
    cls.save_seg(seg, dst)
  

  @staticmethod
  def monoral(
    seg: AS,
  ) -> AS:
    seg.set_channels(1)


from tqdm import (
  trange,
)


from kagemeka.ds import (
  Video,
)

from kagemeka.gen import (
  PathManager as PM,
)

cfd = PM.cfd(__file__)

src = f'{cfd}/<movie>.mp4'

dst = f'{cfd}/<movie>.mov'


video = Video.make(
  src,
  dst,
)


n = video.src_props.frame_cnt 

i = 0 
for _ in trange(n):
  i += 1 
  frame = video.read() 
  if frame is None:
    continue 
  video.write(frame)

video.release()



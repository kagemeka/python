
from . import (
  Path_,
)

import os

import re 
from glob import glob 


from typing import (
  List,
  Iterable,
  NoReturn,
)

from itertools import (
  chain,
)
import shutil


class PathManager:
  

  @staticmethod
  def dir_(
    path: Path_,
  ) -> NoReturn:
    dir_ = os.path.dirname(
      path,
    )
    return dir_
  

  @staticmethod 
  def base(
    path: Path_,
  ) -> str:
    s = os.path.basename(
      path,
    )
    return s


  @staticmethod 
  def root(
    path: Path_,
  ) -> str:
    rt = os.path.splitext(
      path,
    )[0]
    return rt 


  @staticmethod 
  def ext(
    path: Path_,
  ) -> str:
    e = os.path.splitext(
      path,
    )[-1].lstrip('.')
    e = e.lower()
    return e  


  @classmethod 
  def rtbase(
    cls,
    path: Path_,
  ) -> str:
    base = cls.base(path)
    return cls.root(base)


  @staticmethod 
  def cfd(
    __file__: str
  ) -> str:
    cfd = os.path.dirname(
      os.path.abspath(__file__)
    )
    return cfd


  @staticmethod 
  def ch_ignorecase(
    s: Path_,
    from_: str,
    to: str,
  ) -> str:
    s = str(s)
    s = re.sub(
      pattern=from_,
      repl=to,
      string=s,
      flags=re.IGNORECASE,
    )
    return s
  

  @classmethod 
  def prepare_dir(
    cls,
    path: Path_,
  ) -> NoReturn:
    dir_ = cls.dir_(
      path,
    )
    os.makedirs(
      name=dir_,
      exist_ok=True,
    )


  @classmethod 
  def mkfile(
    cls,
    path: Path_,
  ) -> NoReturn:
    cls.prepare_dir(path)
    with open(
      file=path,
      mode='w',
    ) as _:
      pass 


  @staticmethod 
  def find_dirs(
    dirpath: Path_,
  ) -> List[str]:
    dirs = glob(
      f'{dirpath}/**/*/',
      recursive=True,
    ) 
    dirs.sort()
    return dirs
  

  @staticmethod 
  def find_files(
    dirpath: Path_,
    exts: Iterable[str]=[
      '*',
    ],
  ) -> List[str]:
    files: List[List[str]]
    files = [
      glob(
        f'{dirpath}/**/'
        f'*.{ext}',
        recursive=True,
      )
      for ext in exts
    ]
    files = chain(*files)
    files = sorted(files)
    return files


  @classmethod
  def assert_ext(
    cls,
    path: Path_,
    ext: str='*'
  ):
    ext = re.compile(
      ext,
      re.IGNORECASE,
    )
    matched = ext.match(
      cls.ext(path),
    ) 
    assert (
      matched
    ), (
      'extension must be '
      f'{ext}'
    )
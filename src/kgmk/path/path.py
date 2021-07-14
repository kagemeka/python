import dataclasses 
import os


@dataclasses.dataclass
class Path():
  __path: str


  def __call__(
    self,
  ) -> str:
    return os.path.abspath(
      self.__path,
    )
  

  def __repr__(
    self,
  ) -> str:
    return self()
  

  @property
  def base(
    self,
  ) -> str:
    return os.path.basename(
      self.__path,
    )


  @property 
  def dir(
    self,
  ) -> str:
    return os.path.dirname(
      self(),
    )
    

  @property
  def ext(
    self,
  ) -> str:
    return os.path.splitext(
      self.__path,
    )[-1].lstrip('.').lower()
  

  @property
  def root(
    self,
  ) -> str:
    return os.path.splitext(
      self(),
    )[0]
  
  
  @property
  def rtbase(
    self,
  ) -> str:
    return os.path.basename(
      self.root,
    )

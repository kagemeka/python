import typing 
import dataclasses



@dataclasses.dataclass 
class Author():
  en: typing.Optional[
    typing.Union[typing.List[str], str]
  ] = None 
  ja: typing.Optional[
    typing.Union[typing.List[str], str]
  ] = None 



class Parse():
  def __call__(
    self,
    data: dict,
  ) -> Author:
    self.__data = data
    self.__parse()
    return self.__author
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    data = self.__data
    author = Author(**{
      f.name: data[f.name].get('name', None)
      for f in dataclasses.fields(Author)
      if data[f.name]
    })
    self.__author = author
    self.__to_list()


  def __to_list(
    self,
  ) -> typing.NoReturn:
    a = self.__author
    for f in dataclasses.fields(a):
      f = f.name
      v = getattr(a, f)
      if v is None: continue
      if type(v) == list: continue
      setattr(a, f, [v])
  
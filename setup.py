version = '0.1.7'

import typing
import pathlib
from setuptools import (
  setup,
  find_packages,
)
import setuptools 

import os
cfd = os.path.dirname(__file__)
cfd = os.path.abspath(cfd)

class ReadRequirements():
  def __call__(
    self,
    path: str,
  ) -> typing.List[str]:
    with open(
      path, 
      mode='r',
    ) as f:
      ls = f.readlines()
      ls = [
        l.rstrip()
        for l in ls
        if not l.startswith(
          'git+',
        )
      ]
    return ls


class GetExtrasRequire():
  def __call__(
    self,
    root_dir: str,
  ) -> typing.NoReturn:
    self.__root_dir = root_dir
    self.__find_paths()
    self.__get_require()
    return self.__require
  

  def __get_require(
    self,
  ) -> typing.NoReturn:
    import os
    paths = self.__paths
    fn = ReadRequirements()
    req = dict()
    for p in paths:
      name = p.split(
        os.path.sep,
      )[-2]
      requires = fn(p)
      req[name] = requires
    self.__require = req

      
  def __find_paths(
    self,
  ) -> typing.NoReturn:
    from glob import (
      glob,
    )
    self.__paths = glob(
      f'{self.__root_dir}/**/'
      'requirements.txt',
      recursive=True,
    )
    
    



read = ReadRequirements()
reqs = read(
  f'{cfd}/requirements.txt',
)
extras = GetExtrasRequire()(
  f'{cfd}/src/'
)



setuptools.setup(
  name="kagemeka",
  version=version,
  description="",
  long_description="",
  long_description_content_type="text/markdown",
  url="https://github.com/kagemeka/py",
  author="kagemeka",
  author_email="kagemeka1@gmail.com",
  maintainer='kagemeka',
  maintainer_email='kagemeka1@gmail.com',
  license="MIT",
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Operating System :: POSIX :: Linux",
  ],
  package_dir={
    '': 'src',
  },
  packages=find_packages(
    where='./src/',
    exclude=[
      '*tests*',
    ],
  ),
  include_package_data=True,
  install_requires=reqs,
  python_requires=(
    '>=3.6, '
  ),
  extras_require=extras,

)
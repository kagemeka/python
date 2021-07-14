import pathlib
from setuptools import (
  setup,
  find_packages,
)
import setuptools 

import os
cfd = os.path.dirname(__file__)
cfd = os.path.abspath(cfd)

req = f'{cfd}/requirements.txt'

# reader = Reader(src=req)
# with reader as r:
with open(req, mode='r') as f:
    reqs = f.read().split()
    # reqs = r.lines()
    reqs = [
        req
        for req in reqs
        if '+https' not in req
    ]



setuptools.setup(
    name="kagemeka",
    version="0.1.1",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/kagemeka/myenv/lib/python/kagemeka",
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
    packages=find_packages(
        where='.',
    ),
    include_package_data=True,
    install_requires=reqs,
    python_requires=(
        '>=3.9, '
    ),
    # package_dir={
    #     'kagemeka': 'src'
    # },
)
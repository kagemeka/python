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

with open(req, mode='r') as f:
    ls = f.readlines()
    reqs = [
        l.rstrip()
        for l in ls
        if not l.startswith(
            'git+',
        )
    ]



setuptools.setup(
    name="kagemeka",
    version="0.1.1",
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
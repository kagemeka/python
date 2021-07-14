ARG CUDA_VER=11.2.1
ARG UBUNTU_VER=20.04
FROM nvidia/cuda:${CUDA_VER}-cudnn8-devel-ubuntu${UBUNTU_VER}
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root/
ARG PYVER=3.9
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  neovim \
  wget \
  software-properties-common \
  && rm -rf /var/lib/apt/lists/* \
  && apt clean -y \
  && echo "PS1='\w\$ '" >> ~/.bashrc \
  && echo "bind '\"\t\":menu-complete'" >> ~/.bashrc \
  && apt -q=2 update \
  && apt -yq=2 install \
  python3-neovim \
  python3-opencv \
  python3-pip \
  && add-apt-repository -y \
  ppa:deadsnakes/ppa \
  && apt -q=2 update \
  && apt install -y \
  python$PYVER \
  python$PYVER-dev \
  python$PYVER-distutils \
  python$PYVER-tk \
  && ln -fns \
  /usr/bin/python$PYVER \
  /usr/bin/python3 \
  && ln -fns \
  /usr/bin/python3 \
  /usr/bin/python
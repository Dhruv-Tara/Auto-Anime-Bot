#!/bin/bash

# Install Python 3.11.3

sudo apt update

# -- Important Build essential files -- # 

sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

wget https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tgz
tar -xf Python-3.11.3.tgz
cd Python-3.11.3
./configure --enable-optimizations
make -j 12
sudo make altinstall
cd ..
sudo rm -r Python-3.11.3


# Installing ffmpeg 
sudo apt install -y ffmpeg

# Installing LibTorrent 
sudo apt install -y python3-libtorrent

# Installing Required Pypi Packages

sudo python3.11 -m pip install -U -r requirements.txt
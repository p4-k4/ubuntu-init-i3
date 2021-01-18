#!/bin/sh
apt update && sudo apt upgrade

apt-get install -y \
python3 \

chmod +x install.py && /usr/bin/python3 install.py

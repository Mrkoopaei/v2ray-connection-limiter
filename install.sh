!#/bin/bash

apt-get update && apt-get upgrade
apt-get install git
apt-get install python
apt-get install pip
pip install --upgrade schedule
pip install --root-user-action=ignore requests
pip install psutil

git clone https://github.com/Mrkoopaei/v2ray-connection-limiter.git

cd v2ray-connection-limiter
chmod +x $(pwd)/start.py
chmod +x $(pwd)/main.py

python3 $(pwd)/start.py

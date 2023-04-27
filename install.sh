!#/bin/bash

apt-get update && apt-get upgrade

apt-get install python
apt-get install pip
pip install --upgrade schedule
pip install --root-user-action=ignore requests
pip install psutil

chmod +x start.py
chmod +x main.py

python3 start.py

#!/bin/sh

cd /home/pi/HDMI_OnOff_API
git fetch origin
#git reset --hard origin/main
git reset --hard origin/master
git pull

pip3 install -r requirements.txt

python3 hdmi_server.py -o family-board.log -a 0.0.0.0 -p 2202 &

until $(curl --output /dev/null --silent --head --fail http://localhost:2202/api/health); do
    printf '.'
    sleep 5
done

# HDMI On/Off Swith - based on python with Flask 

## Install / Configure HDMI Server
setup python required imports

```sh
pip3 install -r requirements.txt
```

## Startup Server
create a crontab where startscript will be excuted

```sh
crontab -e
\# monthly 1st at 06:10
10 6 * * * sudo reboot
\# Updates weekly
30 4 * * 3 sudo apt-get update && sudo apt-get upgrade -y

@reboot /home/pi/HDMI_OnOff_API/start_hdmi_server.sh
```

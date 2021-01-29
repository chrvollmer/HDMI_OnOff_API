import argparse
from flask import Flask
import os
import logging

import app_config

#HDMI steuern
#https://pypi.org/project/vcgencmd/#:~:text='vcgencmd'%20is%20a%20command%20line,a%20binding%20to%20that%20tool.
#vcgencmd display_power 0

app = Flask(__name__)

hdmiStauts = 0

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/hdmi/on')
def hdmiOn():
    hdmiStatus = 1
    os.system("vcgencmd display_power 1")
    return 'HDMI On'

@app.route('/api/hdmi/off')
def hdmiOff():
    hdmiStatus = 0
    os.system("vcgencmd display_power 0")
    return 'HDMI Off'

@app.route('/api/hdmi/status')
def hdmiStatus():
    zahl = str(hdmiStatus)
    tmp = "HDMI Status" + hdmiStatus
    return tmp


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--logfile', required=False,
                        dest='logfile', help='Name of log file.', type=str, default='server.log')
    parser.add_argument('-a', '--ip', required=False,
                        dest='address', help='IP address to host on.', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port', required=False,
                        dest='port', help='Port to host on.', type=int, default=2202)
    parser.add_argument(
        '-d', '--debug',
        help="Print lots of debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    args = parser.parse_args()

    return args



def print_info(message: str):
    print(message)
    logging.info(message)



if __name__ == "__main__":
    
    # configuration
    args = parse_args()

    logging.basicConfig(
        filename=args.logfile, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=args.loglevel)
    
    # main process
    print_info(f'hosting on http://{args.address}:{args.port}')
    app.run(host=args.address, port=args.port)



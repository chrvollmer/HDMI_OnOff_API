from flask import Flask
import os
app = Flask(__name__)


#HDMI steuern
#https://pypi.org/project/vcgencmd/#:~:text='vcgencmd'%20is%20a%20command%20line,a%20binding%20to%20that%20tool.
#vcgencmd display_power 0


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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
#!/usr/bin/env python

import subprocess
from flask import Flask, request, abort
from subprocess import Popen
from intertechno import Intertechno

app = Flask(__name__)

fmCode = Intertechno()

process = None

app.config.update(dict(
    DEBUG=False
))

def rcswitch(systemCode, deviceCode, state):
    global process
    code = str(fmCode.translate(systemCode, deviceCode, state))
     
    if process is not None:
        process.wait()
		
    print("sending FM code: " + code)
		
    process = Popen(['sudo /usr/bin/fmsend ' + code], shell=True)
    exitCode = process.wait()
	
    return exitCode

@app.route("/send", methods=['POST'])
def send():
    systemCode = request.form['syscode']
    deviceCode = int(request.form['devicecode'])
    state = int(request.form['state'])

    if systemCode is not None and deviceCode is not None and state is not None:
        exitCode = rcswitch(systemCode, deviceCode, state)
		
        if exitCode > 0:
            return 'could not transmit FM code', 500
    else:
        return 'code required', 400

    return "", 200

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
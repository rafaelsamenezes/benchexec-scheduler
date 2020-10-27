import os

from flask import Flask, Response, request, send_from_directory, g
import models.db
#from frame_cap import frame_cap
#from input_cap import input_vid

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.debug("GET home")
    return ""


@app.route('/assets/<path:path>')
def assets(path):
    return ""


@app.route("/cap")
def cap():
    ip = request.args.get("ip", "")
    timeout = request.args.get("timeout", 5.0)
    fps = request.args.get("fps", 24)

    def generate():
        yield "data: 0\n\n"
        frame_cap(ip, fps, timeout)
        yield "data: 100\n\n"

    return "Hello"
    #return Response(, mimetype='text/event-stream')

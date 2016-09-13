#!/usr/bin/env python
from flask import Flask, render_template, Response
from car import *

# emulated camera
# from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)


@app.route('/go')
def car_go():
    Go(0.5)
    return render_template('index.html')

@app.route('/back')
def car_back():
    Back(0.5)
    return render_template('index.html')

@app.route('/turn_r')
def car_turnR():
    TurnRight(0.5)
    return render_template('index.html')

@app.route('/turn_l')
def car_turnL():
    TurnLeft(0.5)
    return render_template('index.html')

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

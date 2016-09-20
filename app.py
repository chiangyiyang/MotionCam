#!/usr/bin/env python
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from car4w import *

# emulated camera
# from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!123456'
socketio = SocketIO(app)

car_t = 0.2


@app.route('/go')
def car_go():
    Go(car_t * 3)
    return render_template('index.html')


@app.route('/back')
def car_back():
    Back(car_t * 3)
    return render_template('index.html')


@app.route('/turn_r')
def car_turnR():
    TurnRight(car_t)
    return render_template('index.html')


@app.route('/turn_l')
def car_turnL():
    TurnLeft(car_t)
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


@socketio.on('car event')
def handle_car_event(json):
    print('received car cmd: ' + str(json))
    # print('cmd: ' + str(json['data']))
    if (json['data'] == 'go'):
        Go(car_t * 3)
    if (json['data'] == 'back'):
        Back(car_t * 3)
    if (json['data'] == 'turnl'):
        TurnLeft(car_t)
    if (json['data'] == 'turnr'):
        TurnRight(car_t)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True, threaded=True)
    socketio.run(app=app, host='0.0.0.0')

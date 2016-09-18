# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin1 = 3 # 3, 5    7,8
pin2 = 5
pin3 = 7
pin4 = 8
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)

swap_t = 0.1

def LeftBackStop():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)


def LeftBack():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)


def LeftGoStop():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)


def LeftGo():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)


def RightGoStop():
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.LOW)


def RightGo():
    GPIO.output(pin3, GPIO.HIGH)
    GPIO.output(pin4, GPIO.LOW)


def RightBackStop():
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.LOW)


def RightBack():
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.HIGH)


def TurnLeft(t):
    RightGo()
    time.sleep(swap_t)
    LeftBack()
    time.sleep(t)
    RightGoStop()
    LeftBackStop()


def TurnRight(t):
    LeftGo()
    time.sleep(swap_t)
    RightBack()
    time.sleep(t)
    LeftGoStop()
    RightBackStop()


def Go(t):
    LeftGo()
    time.sleep(swap_t)
    RightGo()
    time.sleep(t)
    LeftGoStop()
    RightGoStop()


def Back(t):
    LeftBack()
    time.sleep(swap_t)
    RightBack()
    time.sleep(t)
    LeftBackStop()
    RightBackStop()

#
# TurnRight(2)
# time.sleep(1)
# TurnLeft(0.5)
# time.sleep(1)
# Go(1)
# time.sleep(1)
# Back(0.5)
#
# RightGo()
# time.sleep(0.2)
# RightGoStop()
# time.sleep(1)
#
# RightBack()
# time.sleep(0.2)
# RightBackStop()
# time.sleep(1)
#
# LeftGo()
# time.sleep(0.2)
# LeftGoStop()
# time.sleep(1)
#
# LeftBack()
# time.sleep(0.2)
# LeftBackStop()
# time.sleep(1)
#
#
#
# RightGo()
# time.sleep(0.04)
# LeftGo()
# time.sleep(3)
# RightGoStop()
# LeftGoStop()
# time.sleep(1)

# GPIO.cleanup()
# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin1 = 11 # 11, 12    15,16
pin2 = 12 # 11, 12    15,16
pin3 = 15 # 11, 12    15,16
pin4 = 16 # 11, 12    15,16
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)


def RightGo():
    GPIO.output(pin1, GPIO.HIGH)

def RightGoStop():
    GPIO.output(pin1, GPIO.LOW)


def RightBack():
    GPIO.output(pin2, GPIO.HIGH)

def RightBackStop():
    GPIO.output(pin2, GPIO.LOW)


def LeftGo():
    GPIO.output(pin3, GPIO.HIGH)

def LeftGoStop():
    GPIO.output(pin3, GPIO.LOW)


def LeftBack():
    GPIO.output(pin4, GPIO.HIGH)

def LeftBackStop():
    GPIO.output(pin4, GPIO.LOW)

def TurnLeft(t):
    RightGo()
    LeftBack()
    time.sleep(t)
    RightGoStop()
    LeftBackStop()

def TurnRight(t):
    LeftGo()
    RightBack()
    time.sleep(t)
    LeftGoStop()
    RightBackStop()

def Go(t):
    LeftGo()
    RightGo()
    time.sleep(t)
    LeftGoStop()
    RightGoStop()

def Back(t):
    LeftBack()
    RightBack()
    time.sleep(t)
    LeftBackStop()
    RightBackStop()


# TurnRight(0.5)
# time.sleep(1)
# TurnLeft(0.5)
# time.sleep(1)
# Go(0.5)
# time.sleep(1)
# Back(0.5)

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
# GPIO.cleanup()
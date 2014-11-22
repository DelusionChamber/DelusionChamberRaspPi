import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM) 
PULL_PIN = 0 
PUSH_PIN = 1
RANGE_SENSOR_PIN = 2
MOTION_SENSOR_PIN = 3

class WinchController():
    def __init__(self):
        GPIO.setup(PULL_PIN, GPIO.OUT)
        GPIO.setup(PUSH_PIN, GPIO.OUT)
        GPIO.setup(RANGE_SENSOR_PIN, GPIO.IN)
        GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
    def push(self):
        GPIO.output(PULL_PIN, 0)
        GPIO.output(PUSH_PIN, 1)
    def pull(self):
        GPIO.output(PULL_PIN, 1)
        GPIO.output(PUSH_PIN, 0)
    def stop(self):
        GPIO.output(PULL_PIN, 0)
        GPIO.output(PUSH_PIN, 0)
    def motion_sensed(self):
        GPIO.input(MOTION_SENSOR_PIN)

from time import sleep

from random  import randint
import threading
import pdb
LIGHT_DELAY = .01
class LightThread(threading.Thread):
# This thread allows the lights to be constantly changing colors when the objects color values change, making it easier on the main program
    def __init__(self, lc):
        super(LightThread, self).__init__()
        self.lc=lc
        self.actual_r=1
        self.projected_r= 1
        self.actual_g = 1
        self.projected_g = 1
        self.actual_b = 1
        self.projected_b = 1
        self.f_rate = .9
        self.p_rate = .1
        self._stop = threading.Event()

    def stop(self):
        self.lc.red.ChangeDutyCycle(0)
        self.lc.blue.ChangeDutyCycle(0)
        self.lc.green.ChangeDutyCycle(0)
 
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()

    def run(self):
        while True:
            self.set_actual_values()
            self.lc.red.ChangeDutyCycle(self.actual_r)
            self.lc.blue.ChangeDutyCycle(self.actual_b)
            self.lc.green.ChangeDutyCycle(self.actual_g)
            sleep(self.p_rate)

    def set_actual_values(self):
            if self.actual_r < self.projected_r:
                self.actual_r = self.actual_r+.1
                self.actual_r = self.actual_r/self.f_rate if self.actual_r/self.f_rate < self.projected_r else self.projected_r
            if self.actual_r > self.projected_r:
                self.actual_r = self.actual_r*self.f_rate if self.actual_r*self.f_rate > self.projected_r else self.projected_r

            if self.actual_g < self.projected_g:
                self.actual_g = self.actual_g+.1
                self.actual_g = self.actual_g/self.f_rate if self.actual_g/self.f_rate < self.projected_g else self.projected_g
            if self.actual_g > self.projected_g:
                self.actual_g = self.actual_g*self.f_rate if self.actual_g*self.f_rate > self.projected_g else self.projected_g

            if self.actual_b < self.projected_b:
                self.actual_b = self.actual_b+.1
                self.actual_b = self.actual_b/self.f_rate if self.actual_b/self.f_rate < self.projected_b else self.projected_b
            if self.actual_b > self.projected_b:
                self.actual_b = self.actual_b*self.f_rate if self.actual_b*self.f_rate > self.projected_b else self.projected_b



class LightController():
    def __init__(self, GPIO, r, g, b):
        self.GPIO = GPIO
        GPIO.setup(r, GPIO.OUT)
        GPIO.setup(g, GPIO.OUT)
        GPIO.setup(b, GPIO.OUT)
        self.red = GPIO.PWM(r, 100)
        self.green = GPIO.PWM(g, 100)
        self.blue = GPIO.PWM(b, 100)
        self.red_val = 0
        self.blue_val = 0
        self.green_val = 0
        self.red.start(0)
        self.blue.start(0)
        self.green.start(0)
    def fade_red(self):
        for i in range(0, 101):
            self.red.ChangeDutyCycle(i)
            sleep(LIGHT_DELAY)
        for i in range(100, -1, -1):
            self.red.ChangeDutyCycle(i)
            sleep(LIGHT_DELAY)
    def fade_calms(self):
        for i in range(0, 101):
            self.blue.ChangeDutyCycle(i)
            self.green.ChangeDutyCycle(100 - i)
            sleep(LIGHT_DELAY/4)
        for i in range(100, -1, -1):
            self.blue.ChangeDutyCycle(i)
            self.green.ChangeDutyCycle(100 - i)
            sleep(LIGHT_DELAY/4)
        for i in range(0, 101):
            self.blue.ChangeDutyCycle(i)
            self.red.ChangeDutyCycle(i)
            sleep(LIGHT_DELAY/4)
        for i in range(100, -1, -1):
            self.blue.ChangeDutyCycle(100- i)
            self.red.ChangeDutyCycle(100 - i)
            sleep(LIGHT_DELAY/4)
        for i in range(0, 101):
            self.blue.ChangeDutyCycle(i)
            self.green.ChangeDutyCycle(i)
            sleep(LIGHT_DELAY/4)

    def fade_green(self):
        for i in range(0, 101):
            self.green.ChangeDutyCycle(i)
            sleep(LIGHT_DELAY)
        for i in range(100, -1, -1):
            self.green.ChangeDutyCycle(i)
            sleep(LIGHT_DELAY)









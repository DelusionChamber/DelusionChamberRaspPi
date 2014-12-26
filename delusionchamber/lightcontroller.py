from time import sleepQ
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
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()

    def run(self):
        while True:
            if self.actual_r < self.projected_r:
                self.actual_r = self.actual_r/.9 if self.actual_r/.9 < self.projected_r else self.projected_r
                self.lc.red.ChangeDutyCycle(self.actual_r*.5)
            if self.actual_r > self.projected_r:
                self.actual_r = self.actual_r*.9 if self.actual_r*.9 > self.projected_r else self.projected_r
                self.lc.red.ChangeDutyCycle(self.actual_r/.5)

            if self.actual_g < self.projected_g:
                self.actual_g = self.actual_g/.9 if self.actual_g/.9 < self.projected_g else self.projected_g
                self.lc.green.ChangeDutyCycle(self.actual_g)
            if self.actual_g > self.projected_g:
                self.actual_g = self.actual_g*.9 if self.actual_g*.9 > self.projected_g else self.projected_g
                self.lc.green.ChangeDutyCycle(self.actual_g)

            if self.actual_b < self.projected_b:
                self.actual_b = self.actual_b/.9 if self.actual_b/.9 < self.projected_b else self.projected_b
                self.lc.blue.ChangeDutyCycle(self.actual_b)
            if self.actual_b > self.projected_b:
                self.actual_b = self.actual_b*.9 if self.actual_b*.9 > self.projected_b else self.projected_b
                self.lc.blue.ChangeDutyCycle(self.actual_b)
            sleep(.1)



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









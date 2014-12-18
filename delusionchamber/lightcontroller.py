from time import sleep

class LightController():
    def __init__(self, GPIO, r, g, b):
        self.GPIO = GPIO
	GPIO.setup(r, GPIO.OUT)
	GPIO.setup(g, GPIO.OUT)
	GPIO.setup(b, GPIO.OUT)
        self.red = GPIO.PWM(r, 100)
        self.green = GPIO.PWM(g, 100)
        self.blue = GPIO.PWM(b, 100)
    def fade_red(self):
        self.red.start(0)
        for i in range(0, 101):
            self.red.ChangeDutyCycle(i)
            sleep(0.02)
        for i in range(100, -1, -1):
            self.red.ChangeDutyCycle(i)
            sleep(0.02)








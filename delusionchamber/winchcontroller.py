
class WinchController():
    def __init__(self, GPIO, PULL_PIN, PUSH_PIN):
        GPIO.setup(PULL_PIN, GPIO.OUT)
        GPIO.setup(PUSH_PIN, GPIO.OUT)
        self.GPIO = GPIO
    def push(self):
        self.GPIO.output(PULL_PIN, 0)
        self.GPIO.output(PUSH_PIN, 1)
    def pull(self):
        self.GPIO.output(PULL_PIN, 1)
        self.GPIO.output(PUSH_PIN, 0)
    def stop(self):
        self.GPIO.output(PULL_PIN, 0)
        self.GPIO.output(PUSH_PIN, 0)

class WinchController():
    def __init__(self, GPIO, PULL_PIN, PUSH_PIN):
        GPIO.setup(PULL_PIN, GPIO.OUT)
        GPIO.setup(PUSH_PIN, GPIO.OUT)
        self.PULL_PIN = PULL_PIN
        self.PUSH_PIN = PUSH_PIN
        self.GPIO = GPIO
    def push(self):
        self.GPIO.output(self.PULL_PIN, 0)
        self.GPIO.output(self.PUSH_PIN, 1)
    def pull(self):
        self.GPIO.output(self.PUSH_PIN, 0)
        self.GPIO.output(self.PULL_PIN, 1)
    def stop(self):
        self.GPIO.output(self.PULL_PIN, 0)
        self.GPIO.output(self.PUSH_PIN, 0)

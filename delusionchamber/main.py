import RPi.GPIO as GPIO
from randomaudio import RandomAudio
from lightcontroller import LightController
from pygame import mixer
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

MOTION_PIN = 18

class DelusionChamber:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(MOTION_PIN, GPIO.IN)
        self.pm = mixer
        self.pm.init()
        self.random_ideas = RandomAudio('../idea_files', self.pm, 1, 0.2)
        self.random_music = RandomAudio('../music_files', self.pm, 2, 0.7)
        self.light = LightController(GPIO, RED_PIN, GREEN_PIN, BLUE_PIN)
    def start(self):
        while True:
            if GPIO.input(18)
                self.light.fade_red()
            # self.random_music.play_sound()
            # self.random_ideas.play_sound()



        


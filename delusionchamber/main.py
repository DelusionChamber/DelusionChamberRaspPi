import RPi.GPIO as GPIO
from randomaudio import RandomAudio
from lightcontroller import LightController
from pygame import mixer
from time import sleep
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

MOTION_PIN = 18

WINCH_PULL_PIN = 20 
WINCH_PUSH_PIN = 21

class DelusionChamber:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(MOTION_PIN, GPIO.IN)
        self.pm = mixer
        self.pm.init()
        self.random_ideas = RandomAudio('../idea_files', self.pm, 1, 0.2)
        self.random_music = RandomAudio('../music_files', self.pm, 2, 0.7)
        self.light = LightController(GPIO, RED_PIN, GREEN_PIN, BLUE_PIN)
        self.winch = WinchController(GPIO, WINCH_PULL_PIN, WINCH_PUSH_PIN)
    def start(self):
        while True:
            if GPIO.input(MOTION_PIN) == 1:
                self.light.fade_red()
                sleep(2)
            sleep(1)		
            # self.random_music.play_sound()
            # self.random_ideas.play_sound()



        


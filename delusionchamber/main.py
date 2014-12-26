import RPi.GPIO as GPIO
from randomaudio import RandomAudio
from lightcontroller import LightController, LightThread
from winchcontroller import WinchController
from pygame import mixer
from time import sleep
from random import randint
RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 27

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
        self.light_thread = LightThread(self.light)
        self.winch = WinchController(GPIO, WINCH_PULL_PIN, WINCH_PUSH_PIN)
        self.photo = 0
        self.selected_num = 0
    def start(self):
        while self.selected_num < 5:
            if GPIO.input(MOTION_PIN) == 1:
                self.light.fade_green()
                self.selected_num+=1
                sleep(5)
            else:
                self.fade_calms()
                sleep(5)		
        self.selected_num = 0
        while self.photo < 500:
            self.light.fade_red()
            self.winch.push()
        self.random_music.play_sound()
        self.random_ideas.play_sound()

    def fade_calms(self):
        self.light_thread.projected_b = randint(1,100)
        self.light_thread.projected_g = randint(1,100)



        


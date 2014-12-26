import RPi.GPIO as GPIO
from randomaudio import RandomAudio
from lightcontroller import LightController, LightThread
from winchcontroller import WinchController
from repeatedtimer import RepeatedTimer
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
        self.winch = WinchController(GPIO, WINCH_PULL_PIN, WINCH_PUSH_PIN)
        self.light_thread = LightThread(self.light)
        self.photo = 0
        self.selected_num = 0

    def start(self):
        try:
            green_interval = RepeatedTimer(5, pulse_green)
            calms_interval = RepeatedTimer(5, fade_calms)
            warms_interval = RepeatedTimer(5, fade_warms)
            while self.selected_num < 5:
                if GPIO.input(MOTION_PIN) == 1:
                    if calms_interval.is_running:
                        calms_interval.stop()
                        green_interval.start()
                    else if not green_interval.is_running:
                        green_interval.start()
                    self.selected_num+=1
                    sleep(5)
                else:
                    if green_interval.is_running:
                        green_interval.stop()
                        calms_interval.start()
                    else if not calms_interval.is_running:
                        calms_interval.stop()
                    sleep(5)		
            self.selected_num = 0
            green_interval.stop()
            calms_interval.stop()

            while self.photo < 500:
                self.light.fade_warms()
                self.winch.push()
                self.random_music.play_sound()
            self.random_ideas.play_sound()
        except e: 
            green_interval.stop()
            calms_interval.stop()
            self.light_thread.stop()

    def pulse_red(self):
        self.light_thread.projected_r = 100 if self.light_thread.projected_r == 0 else 1

    def pulse_green(self):
        self.light_thread.projected_g = 100 if self.light_thread.projected_g == 0 else 1

    def fade_calms(self):
        self.light_thread.projected_b = randint(1,100)
        self.light_thread.projected_g = randint(1,100)

    def fade_warms(self):
        self.light_thread.projected_g = randint(50, 100)
        self.light_thread.projected_r = randint(50,100)



        


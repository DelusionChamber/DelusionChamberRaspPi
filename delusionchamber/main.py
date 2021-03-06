import RPi.GPIO as GPIO
import pdb, time
from randomaudio import RandomAudio, EasyAudio
from lightcontroller import LightController, LightThread
from winchcontroller import WinchController
from pygame import mixer
from random import randint

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 27

TRAY_MOTION_PIN = 18
INNER_MOTION_PIN = 23

WINCH_PULL_PIN = 20
WINCH_PUSH_PIN = 21

class DelusionChamber:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRAY_MOTION_PIN, GPIO.IN)
        GPIO.setup(INNER_MOTION_PIN, GPIO.IN)
        self.pm = mixer
        self.pm.init()
        self.random_ideas = RandomAudio('../idea_files', self.pm, 1, 0.2)
        self.random_music = RandomAudio('../music_files', self.pm, 2, 0.7)
        self.notification = EasyAudio(self.pm, 3, 1)
        self.light = LightController(GPIO, RED_PIN, GREEN_PIN, BLUE_PIN)
        self.winch = WinchController(GPIO, WINCH_PULL_PIN, WINCH_PUSH_PIN)
        self.light_thread = LightThread(self.light)
        self.photo = 0
        self.selected_num = 0

    def start(self):
        try:
            motion_sensed = False
            next_time = time.time()
            self.light_thread.start()
            self.fade_calms()
            time.sleep(3)
            while self.selected_num < 5 :
                if GPIO.input(TRAY_MOTION_PIN) == 1 or motion_sensed == True:
                    print "Motion Sensed"
                    self.pulse_green()
                    if motion_sensed == False:
                        motion_sensed = True
                        self.selected_num+=1
                    else:
                        motion_sensed = False
                    print self.selected_num
                if time.time() > next_time + 3:
                    next_time = time.time()
                    self.fade_calms()
                time.sleep(2)
            self.selected_num = 0
            while True:
                if GPIO.input(INNER_MOTION_PIN) == 0:
                    self.fade_warms()
                    self.winch.push()
                if GPIO.input(INNER_MOTION_PIN) == 1:
                    self.winch.stop()
                    self.random_ideas.play_random_sound()
        except (KeyboardInterrupt, SystemExit):
            print "stopped"
            self.light_thread.stop()

    def is_motion_sensed(self):
        closure_dict = {'motion_arr': [0 for x in range(100)], 
                'current_pos': 0}
        def add_to_arr():
            if closure_dict['current_pos'] >= len(closure_dict['motion_arr']):
                closure_dict['current_pos'] = 0
            closure_dict['motion_arr'][closure_dict['current_pos']] = GPIO.input(TRAY_MOTION_PIN)
            closure_dict['current_pos']+=1
            return sum(closure_dict['motion_arr'])/len(closure_dict['motion_arr'])
        return add_to_arr

    def pulse_red(self):
        self.light_thread.projected_g = 0
        self.light_thread.projected_b = 0
        self.light_thread.projected_r = 100 if self.light_thread.projected_r == 0 else 1

    def pulse_green(self):
        self.light_thread.projected_b = 0
        self.light_thread.actual_b = 0
        self.light_thread.projected_r = 0
        self.light_thread.actual_r = 0
        self.light_thread.projected_g = 100 if self.light_thread.projected_g < 5 else 0
        time.sleep(2)
        self.light_thread.projected_g = 100 if self.light_thread.projected_g < 5 else 0
        time.sleep(2)

    def fade_calms(self):
        self.light_thread.actual_r = 0
        self.light_thread.projected_b = randint(1,100)
        self.light_thread.projected_g = randint(1,100)

    def fade_warms(self):
        self.light_thread.actual_b = 0
        self.light_thread.projected_b = 0
        self.light_thread.projected_g = randint(50, 100)
        self.light_thread.projected_r = randint(50,100)

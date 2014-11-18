from randomaudio import RandomAudio
from pygame import mixer
class DelusionChamber:
    def __init__(self):
        self.pm = mixer
        self.pm.init()
        self.random_ideas = RandomAudio('../idea_files', self.pm, 1, 0.2)
        self.random_music = RandomAudio('../music_files', self.pm, 2, 0.7)

    def start(self):
        while True:
            self.random_music.play_sound()
            self.random_ideas.play_sound()



        


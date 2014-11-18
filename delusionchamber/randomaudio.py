import os, random, ipdb
class RandomAudio():
    def __init__(self, directory, pygame_mixer, channel, volume=1.0):
        self.pygame_mixer = pygame_mixer
        self.channel_to_play_on = pygame_mixer.Channel(channel)
        self.channel_to_play_on.set_volume(volume, 1.0 - volume)
        self.sound_directory = directory
        self.sound_files = os.listdir(directory)

    def play_sound(self):
        if self.channel_to_play_on.get_busy() == 0:
            sound = self.pygame_mixer.Sound(self.sound_directory+"/"+random.choice(self.sound_files))
            self.channel_to_play_on.play(sound)



            





import pygame
import os


class Player():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.current_beat = None
        self.file_dict = {}

    def play(self, beat, callback=None):
        self.stop(self.current_beat)
        beat.play(loops=-1)
        self.current_beat = beat

    def stop(self, beat):
        if beat is not None:
            beat.stop()

    def load_beats(self):
        beat_folder = "audio"
        beats = {}
        for category in os.listdir(beat_folder):
            category_path = os.path.join(beat_folder, category)
            if os.path.isdir(category_path):
                self.file_dict[category] = os.listdir(category_path)
                beats[category] = []
                for filename in os.listdir(category_path):
                    if filename.endswith(".wav"):
                        beat_path = os.path.join(category_path, filename)
                        beat = pygame.mixer.Sound(beat_path)
                        beats[category].append(beat)
        return beats


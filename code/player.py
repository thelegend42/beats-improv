import pygame


class Player():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.lofi = pygame.mixer.Sound("AUDIO/LoFi.wav")
        self.groovy = pygame.mixer.Sound("AUDIO/Groovy-96bpm.wav")

        self.current_beat = None

    def play(self, beat, callback=None):
        if self.current_beat is not None:
            self.stop(self.current_beat)
        beat.play(loops=-1)
        self.current_beat = beat

    def stop(self, beat):
        if beat is not None:
            beat.stop()

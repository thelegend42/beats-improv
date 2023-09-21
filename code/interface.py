import tkinter as tk
import sv_ttk
from .player import Player
import os


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Beat machine")
        sv_ttk.use_light_theme()
        self.geometry("800x600")

        self.button_width = 10
        self.button_height = 3
        self.police = ('calibre', 14, 'bold')

        self.player = Player()
        self.beats = self.player.load_beats()

        self.volume_fader = None
        self.volume = tk.DoubleVar()
        self.indicator_label = None

        self.create_widget()

    def create_widget(self):
        row_position = 1
        for category, beat_list in self.beats.items():
            category_label = tk.Label(self, text=category, font=self.police)
            category_label.grid(row=row_position, column=1, sticky='w')
            num = 0
            for idx, beat in enumerate(beat_list):
                beat_name = os.path.splitext(self.player.file_dict[category][num])[0]
                beat_button = tk.Button(self,
                                        text=beat_name,
                                        width=self.button_width,
                                        height=self.button_height,
                                        command=lambda b=beat: self.toggle_beat(b),
                                        font=self.police)
                beat_button.grid(row=row_position, column=idx + 2, sticky='w')
                num += 1

            row_position += 1

        self.volume_fader = tk.Scale(self,
                                     from_=100,
                                     to=0,
                                     orient="vertical",
                                     variable=self.volume,
                                     command=self.update_volume)
        self.volume_fader.set(100)
        self.volume_fader.grid(row=1, column=20, rowspan=10)
        self.update_volume()

        stop_button = tk.Button(self,
                                text="STOP!",
                                width=self.button_width,
                                height=self.button_height,
                                command=self.stop_all_beats,
                                font=self.police)
        stop_button.grid(row=1, column=30, rowspan=10)

        self.indicator_label = tk.Label(self,
                                        text="PLAYING!",
                                        bg="black",
                                        width=self.button_width,
                                        height=self.button_height)
        self.indicator_label.grid(row=1, column=40, rowspan=10)

    def toggle_beat(self, beat):
        if self.player.current_beat != beat:
            self.player.play(beat)
            self.indicator_label.config(bg="red")
        else:
            self.stop_all_beats()
        self.update_volume()

    def update_volume(self, *args):
        if self.player.current_beat is not None:
            volume = self.volume.get() / 100.0
            self.player.current_beat.set_volume(volume)

    def stop_all_beats(self):
        if self.player.current_beat:
            self.player.stop(self.player.current_beat)
            self.player.current_beat = None
            self.indicator_label.config(bg="black")

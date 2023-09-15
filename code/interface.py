import tkinter as tk
import sv_ttk
from .player import Player


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Beat machine")
        sv_ttk.use_light_theme()
        self.geometry("400x200")

        self.button_width = 10
        self.button_height = 5
        self.police = ('calibre', 14, 'bold')

        self.player = Player()

        self.volume_fader = None
        self.volume = tk.DoubleVar()

        self.create_widget()

    def create_widget(self):
        lofi_button = tk.Button(self,
                                text="LoFi",
                                width=self.button_width,
                                height=self.button_height,
                                command=lambda: self.toggle_beat(self.player.lofi),
                                font=self.police
                                )
        lofi_button.grid(row=10, column=10)

        groovy_button = tk.Button(self,
                                  text="Groovy",
                                  width=self.button_width,
                                  height=self.button_height,
                                  command=lambda: self.toggle_beat(self.player.groovy),
                                  font=self.police)
        groovy_button.grid(row=10, column=20)

        self.volume_fader = tk.Scale(self, from_=100, to=0, orient="vertical", variable=self.volume, command=self.update_volume)
        self.volume_fader.set(100)
        self.volume_fader.grid(row=10, column=100, columnspan=100)
        self.update_volume()

    def toggle_beat(self, beat):
        if self.player.current_beat != beat:
            self.player.play(beat)
        else:
            self.player.stop(beat)
            self.player.current_beat = None
        self.update_volume()

    def update_volume(self, *args):
        if self.player.current_beat is not None:
            volume = self.volume.get() / 100.0
            self.player.current_beat.set_volume(volume)

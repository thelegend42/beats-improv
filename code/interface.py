import tkinter as tk
import sv_ttk
from .player import Player


class Fenetre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Beat machine")
        sv_ttk.use_light_theme()
        self.geometry("400x200")

        self.button_width = 10
        self.button_height = 5
        self.police = ('calibre', 14, 'bold')

        self.player = Player()

        self.create_widget()

    def create_widget(self):
        lofi_button = tk.Button(self,
                                text="LoFi",
                                width=self.button_width,
                                height=self.button_height,
                                command=self.toggle_lofi,
                                font=self.police
                                )
        lofi_button.grid(row=10, column=10)

        groovy_button = tk.Button(self,
                                  text="Groovy",
                                  width=self.button_width,
                                  height=self.button_height,
                                  command=self.toggle_groovy,
                                  font=self.police)
        groovy_button.grid(row=10, column=20)

    def toggle_lofi(self):
        if self.player.current_beat != self.player.lofi:
            self.player.play(self.player.lofi)
        else:
            self.player.stop(self.player.lofi)

    def toggle_groovy(self):
        if self.player.current_beat != self.player.groovy:
            self.player.play(self.player.groovy)
        else:
            self.player.stop(self.player.groovy)

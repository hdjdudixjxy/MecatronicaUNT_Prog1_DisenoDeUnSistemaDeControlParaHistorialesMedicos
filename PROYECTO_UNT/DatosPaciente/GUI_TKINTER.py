import tkinter as tk

class ventana(tk.Frame):
    def __init__(self, base):
        super().__init__(base, width=1980, height=1020)
        self.pack()
        self.config(background="lightblue")





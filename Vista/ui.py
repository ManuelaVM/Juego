import tkinter as tk
from tkinter import *


THEME_COLOR = "#375362"

class Interface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Juego")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.Ronda1_pregunta = self.canvas.create_text(
            150,
            125,
            text="Algun texto de pregunta",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.canvas.grid(row=2, column=0, columnspan=2, pady=100)


        self.A_button = Button(
            text="Hola",
            background="hot pink",
            padx=20,
        )
        self.A_button.place(x=50, y=400)

        self.B_button = Button(
            text="Hola",
            background="violet red",
            padx=20
            )
        self.B_button.place(x=50,y=450)

        self.C_button = Button(
            text="Hola",
            background="SeaGreen1",
            padx=20
        )
        self.C_button.place(x=150,y=400)

        self.D_button = Button(
            text="Hola",
            background="OliveDrab1",
            padx=20
        )
        self.D_button.place(x=150,y=450)

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()
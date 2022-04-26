import tkinter as tk
from tkinter import *
from Entidades.Juego import juego

THEME_COLOR = "#375362"

class Interface:

    def __init__(self,Juego: juego):
        self.juego = Juego

        self.window = Tk()
        self.window.title("Juego")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.Ronda1_pregunta = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Algun texto de pregunta",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.canvas.grid(row=2, column=0, columnspan=2, pady=100)


        self.A_button = Button(
            text="Hola",
            background="hot pink",
            padx=20,
            #command=self.respuesta_A
        )
        self.A_button.place(x=50, y=400)

        self.B_button = Button(
            text="Hola",
            background="violet red",
            padx=20,
            #command=self.respuesta_B
            )
        self.B_button.place(x=50,y=450)

        self.C_button = Button(
            text="Hola",
            background="SeaGreen1",
            padx=20,
            #command=self.respuesta_C
        )
        self.C_button.place(x=150,y=400)

        self.D_button = Button(
            text="Hola",
            background="OliveDrab1",
            padx=20,
            #command=self.respuesta_D
        )
        self.D_button.place(x=150,y=450)

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.get_pregunta()

        self.window.mainloop()

    def get_pregunta(self):
        q_text = self.juego.siguiente_pregunta()
        self.canvas.itemconfig(self.Ronda1_pregunta, text=q_text)

    # def respuesta_A(self):
    #     self.Juego.comprobar_respuesta()
    #
    # def respuesta_B(self):
    #     self.Juego.comprobar_respuesta("Apolo")
    #
    # def respuesta_C(self):
    #     self.Juego.comprobar_respuesta("Apolo")
    #
    # def respuesta_D(self):
    #     self.Juego.comprobar_respuesta("Apolo")


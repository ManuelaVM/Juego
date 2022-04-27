import tkinter as tk
from tkinter import *
from Entidades.Juego import juego
from Entidades.Ronda1 import *


THEME_COLOR = "#03045E"

class Interface:

    def __init__(self,Juego: juego):
        self.juego = Juego

        self.window = Tk()
        self.window.title("Juego")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="#CAF0F8", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.ronda_label = Label(text="Ronda: 1", fg="#CAF0F8", bg=THEME_COLOR)
        self.ronda_label.grid(row=0, column=2)



        self.canvas = Canvas(width=300, height=250, bg="#CAF0F8")
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
            text=(self.juego.A()),
            background="hot pink",
            padx=20,
            #command=self.true_pressed
        )
        self.A_button.place(x=20, y=400)

        self.B_button = Button(
            text=(self.juego.B()),
            background="violet red",
            padx=20,
            #command=self.false_pressed
        )
        self.B_button.place(x=20, y=450)

        self.C_button = Button(
            text=(self.juego.C()),
            background="SeaGreen1",
            padx=20,
            #command=self.false_pressed
        )
        self.C_button.place(x=150, y=400)

        self.D_button = Button(
            text=(self.juego.D()),
            background="OliveDrab1",
            padx=20,
            #command=self.false_pressed
        )
        self.D_button.place(x=150, y=450)

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.get_pregunta()

        self.window.mainloop()

    def get_pregunta(self):
        q_text = self.juego.siguiente_pregunta()
        self.canvas.itemconfig(self.Ronda1_pregunta, text=q_text)
        #buton_A = self.juego.A()
        #self.A_button.config(self.A_button, text=buton_A)
        #self.A_button.config(self.juego.pregunta_actual(), text=self.juego.siguiente_pregunta(opcionA))

    #def true_pressed(self):
    #      self.give_feedback(self.juego.comprobar_respuesta({self.juego.comprobar_respuesta(self.juego.pregunta_actual.respuesta_correcta)}))

    #def false_pressed(self):
    #      self.give_feedback(self.juego.comprobar_respuesta({self.juego.comprobar_respuesta(self.juego.pregunta_actual.respuestas_incorrectas)}))

    # def true_pressed(self):
    #     self.give_feedback(self.quiz.check_answer("True"))


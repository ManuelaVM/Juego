from tkinter import *
from Entidades.Juego import juego


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

        self.categoria_label = Label(text=(self.juego.ronda_categoria()), fg="#CAF0F8", bg=THEME_COLOR)
        self.categoria_label.grid(row=0, column=3)


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
            command=self.resultado_A
        )
        self.A_button.place(x=20, y=400)

        self.B_button = Button(
            text=(self.juego.B()),
            background="violet red",
            padx=20,
            command=self.resultado_B
        )
        self.B_button.place(x=20, y=450)

        self.C_button = Button(
            text=(self.juego.C()),
            background="SeaGreen1",
            padx=20,
            command=self.resultado_C
        )
        self.C_button.place(x=150, y=400)

        self.D_button = Button(
            text=(self.juego.D()),
            background="OliveDrab1",
            padx=20,
            command=self.resultado_D
        )
        self.D_button.place(x=150, y=450)

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.get_pregunta()

        self.window.mainloop()

    def get_pregunta(self):
        q_text = self.juego.mostrar_pregunta()
        self.canvas.itemconfig(self.Ronda1_pregunta, text=q_text)

    def resultado_A(self):
        entradaA = self.juego.entradaA()
        is_right = self.juego.comprobar_respuesta(entradaA)
        self.Resultado_Pregunta(is_right)

    def resultado_B(self):
        entradaB = self.juego.entradaB()
        self.Resultado_Pregunta(self.juego.comprobar_respuesta(entradaB))


    def resultado_C(self):
        entradaC = self.juego.entradaC()
        is_right = self.juego.comprobar_respuesta(entradaC)
        self.Resultado_Pregunta(is_right)


    def resultado_D(self):
        entradaD = self.juego.entradaD()
        is_right = self.juego.comprobar_respuesta(entradaD)
        self.Resultado_Pregunta(is_right)


    def Resultado_Pregunta(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_pregunta)

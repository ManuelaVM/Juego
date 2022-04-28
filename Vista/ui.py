from tkinter import *
from Entidades.Juego import juego


THEME_COLOR = "#03045E"

class Interface:

    def __init__(self,Juego: juego):
        self.juego = Juego

        self.window = Tk()
        self.window.title("Juego")
        self.window.config(padx=150, pady=100, bg=THEME_COLOR)
        self.window.resizable(False,False)

        self.score_label = Label(text="Score: 0", fg="#CAF0F8", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.categoria_label = Label(text=(self.juego.ronda_categoria()), fg="#CAF0F8", bg=THEME_COLOR)
        self.categoria_label.grid(row=0, column=3)

        self.categoria_dificultad = Label(text=(self.juego.ronda_dificultad()), fg="#CAF0F8", bg=THEME_COLOR)
        self.categoria_dificultad.grid(row=0, column=5)

        self.canvas = Canvas(width=300, height=250, bg="#CAF0F8")
        self.Ronda1_pregunta = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Algun texto de pregunta",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.canvas.grid(row=3, column=0, columnspan=3, pady=100)

        self.A_button = Button(
            text=(self.juego.mostrar_A()),
            background="hot pink",
            width=30,
            command=self.resultado_A
        )
        self.A_button.place(x=350, y=110)

        self.B_button = Button(
            text=(self.juego.mostrar_B()),
            background="violet red",
            width=30,
            command=self.resultado_B
        )
        self.B_button.place(x=350, y=150)

        self.C_button = Button(
            text=(self.juego.mostrar_C()),
            background="SeaGreen1",
            width=30,
            command=self.resultado_C
        )
        self.C_button.place(x=350, y=200)

        self.D_button = Button(
            text=(self.juego.mostrar_D()),
            background="OliveDrab1",
            width=30,
            command=self.resultado_D
        )
        self.D_button.place(x=350, y=250)

        self.Terminar_button = Button(
            text="Terminar Juego 😼",
            background="OliveDrab1",
            width=30,
            command=self.Terminar_Juego
        )
        self.Terminar_button.place(x=350,y=349)

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.get_pregunta()

        self.window.mainloop()

    def get_pregunta(self):
            self.canvas.config(bg="#CAF0F8")
            if self.juego.todavia_tiene_preguntas():
                self.score_label.config(text=f"Score: {self.juego.score}")
                q_text = self.juego.mostrar_pregunta()
                q_respuesta_a = self.juego.mostrar_A()
                q_respuesta_b = self.juego.mostrar_B()
                q_respuesta_c = self.juego.mostrar_C()
                q_respuesta_d = self.juego.mostrar_D()
                q_categoria = self.juego.ronda_categoria()
                q_dificultad = self.juego.ronda_dificultad()
                self.canvas.itemconfig(self.Ronda1_pregunta, text=q_text)
                self.categoria_label.config(text=q_categoria)
                self.categoria_dificultad.config(text=q_dificultad)
                self.A_button.config(self.A_button, text=q_respuesta_a)
                self.B_button.config(self.B_button, text=q_respuesta_b)
                self.C_button.config(self.C_button, text=q_respuesta_c)
                self.D_button.config(self.D_button, text=q_respuesta_d)
                self.Terminar_button

            else:
                self.canvas.itemconfig(self.Ronda1_pregunta, text="")
                self.A_button.config(state="disabled")
                self.B_button.config(state="disabled")
                self.C_button.config(state="disabled")
                self.D_button.config(state="disabled")


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
            self.canvas.config(bg="red", state="disabled")
            self.A_button.config(state="disabled")
            self.B_button.config(state="disabled")
            self.C_button.config(state="disabled")
            self.D_button.config(state="disabled")
        self.window.after(1000, self.get_pregunta)

    def Terminar_Juego(self):
        reiniciar =self.canvas.itemconfig(self.Ronda1_pregunta, text="Bye...")
        return f"{reiniciar}"

import html
import random
from Ronda1 import ronda_1

class juego:

    def __init__(self, q_lista):
        self.numero_pregunta = 0
        self.score = 0
        self.lista_pregunta = q_lista

    def todavia_tiene_preguntas(self):
        return self.numero_pregunta < len(self.lista_pregunta)

    def siguiente_pregunta(self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        self.numero_pregunta += 1
        q_pregunta = html.unescape(self.pregunta_actual.pregunta)
        opcion_A = self.pregunta_actual.respuesta_correcta
        opcion_B = self.pregunta_actual.respuestas_incorrectas[0]
        opcion_C = self.pregunta_actual.respuestas_incorrectas[1]
        opcion_D = self.pregunta_actual.respuestas_incorrectas[2]
        #return f"Q.{self.numero_pregunta}:{self.pregunta_actual.pregunta} :"
        return f"Q.{self.numero_pregunta}:{q_pregunta} : A.{opcion_A} " \
               f"B. {opcion_B} /n C.{opcion_C}/n" \
                f"D. {opcion_D}"
        #respuesta_usuario = input(f"Q.{self.numero_pregunta}: {pregunta_actual.pregunta}: {pregunta_actual.respuestas} : ")
        #self.comprobar_respuesta(respuesta_usuario, pregunta_actual.respuesta)

    def A (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionA = {self.pregunta_actual.respuesta_correcta}
        return f"A.{opcionA}"

    def B (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionB = {self.pregunta_actual.respuestas_incorrectas[0]}
        return f"B.{opcionB}"

    def C (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionC = {self.pregunta_actual.respuestas_incorrectas[1]}
        return f"C.{opcionC}"

    def D (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionD = {self.pregunta_actual.respuestas_incorrectas[2]}
        return f"D.{opcionD}"

    def comprobar_respuesta(self, respuesta_usuario):
        respuesta_correcta = self.pregunta_actual.respuesta_correcta
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            self.score += 1
            print("continua a la siguiente ronda")
        else:
            print("Se acabo el juego")
        print(f"Puntuación actual: {self.score}/{self.numero_pregunta}")
        print("\n")
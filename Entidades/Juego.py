import html
from Ronda1 import ronda_1
from Ronda2 import ronda_2
from Ronda3 import ronda_3
from Ronda4 import ronda_4
from Ronda5 import ronda_5

class juego:

    def __init__(self, q_lista):
        self.correcta = None
        self.numero_pregunta = 0
        self.score = 0
        self.lista_pregunta = q_lista

    def todavia_tiene_preguntas(self):
        return self.numero_pregunta < len(self.lista_pregunta)

    # def siguiente_pregunta(self):
    #     self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
    #     q_pregunta = html.unescape(self.pregunta_actual.pregunta)
    #     while (self.numero_pregunta) :
    #         if ronda_1 == self.pregunta_actual.respuesta_correcta:
    #             self.numero_pregunta += 1
    #             return f"Q.{self.numero_pregunta}:{q_pregunta}"
    #
    #         if ronda_2 == self.pregunta_actual.respuesta_correcta:
    #             self.numero_pregunta += 1
    #             return f"Q.{self.numero_pregunta}:{q_pregunta}"
    #
    #         if ronda_3 == self.pregunta_actual.respuesta_correcta:
    #             self.numero_pregunta += 1
    #             return f"Q.{self.numero_pregunta}:{q_pregunta}"
    #
    #         if ronda_4 == self.pregunta_actual.respuesta_correcta:
    #             self.numero_pregunta += 1
    #             return f"Q.{self.numero_pregunta}:{q_pregunta}"
    #
    #         if ronda_5 == self.pregunta_actual.respuesta_correcta:
    #             self.numero_pregunta += 1
    #             return f"Q.{self.numero_pregunta}:{q_pregunta}"
    #
    #         else:
    #             return "Game Over"

    def mostrar_pregunta(self):
          self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
          q_pregunta = html.unescape(self.pregunta_actual.pregunta)
          self.numero_pregunta += 1
          return f"Q.{self.numero_pregunta}:{q_pregunta}"

    def A (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionA = html.unescape(self.pregunta_actual.respuesta_correcta)
        return f"A.{opcionA}"

    def B (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionB = html.unescape(self.pregunta_actual.respuestas_incorrectas[0])
        return f"B.{opcionB}"

    def C (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionC = html.unescape(self.pregunta_actual.respuestas_incorrectas[1])
        return f"C.{opcionC}"

    def D (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionD = html.unescape(self.pregunta_actual.respuestas_incorrectas[2])
        return f"D.{opcionD}"

    def ronda_categoria(self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        categoria = html.unescape(self.pregunta_actual.categoria)
        return categoria

    def comprobar_respuesta(self, respuesta_usuario):
        self.correcta = self.pregunta_actual.respuesta_correcta
        if respuesta_usuario == self.correcta:
            self.score += 1
            return True
        else:
            return False


    def entradaA  (self):
        entradaA = html.unescape(self.pregunta_actual.respuesta_correcta)
        return f"{entradaA}"

    def entradaB  (self):
        entradaB = html.unescape(self.pregunta_actual.respuestas_incorrectas[0])
        return f"{entradaB}"

    def entradaC  (self):
        entradaC = html.unescape(self.pregunta_actual.respuestas_incorrectas[1])
        return f"{entradaC}"

    def entradaD  (self):
        entradaD = html.unescape(self.pregunta_actual.respuestas_incorrectas[2])
        return f"{entradaD}"
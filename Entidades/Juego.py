import html
import random


class juego:

    def __init__(self, q_lista):
        self.correcta = None
        self.numero_pregunta = 0
        self.score = 0
        self.lista_pregunta = q_lista



    def todavia_tiene_preguntas(self):
        return self.numero_pregunta < len(self.lista_pregunta)

    def mostrar_pregunta(self):
          self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
          self.numero_pregunta += 1
          q_pregunta = html.unescape(self.pregunta_actual.pregunta)
          return f"{self.numero_pregunta}:{q_pregunta}"

    # _____________________________________________________________________________

    def mostrar_A (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionA = html.unescape(self.pregunta_actual.respuesta_correcta)
        return f"A.{opcionA}"

    def mostrar_B (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionB = html.unescape(self.pregunta_actual.respuestas_incorrectas[0])
        return f"B.{opcionB}"

    def mostrar_C (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionC = html.unescape(self.pregunta_actual.respuestas_incorrectas[1])
        return f"C.{opcionC}"

    def mostrar_D (self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        opcionD = html.unescape(self.pregunta_actual.respuestas_incorrectas[2])
        return f"D.{opcionD}"

    # _____________________________________________________________________________

    def ronda_categoria(self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        categoria = html.unescape(self.pregunta_actual.categoria)
        return f"Categoria: {categoria}"

    def ronda_dificultad(self):
        self.pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        dificultad = html.unescape(self.pregunta_actual.dificultad)
        return f"Categoria: {dificultad}"
    # _____________________________________________________________________________

    def comprobar_respuesta(self, respuesta_usuario):
        self.correcta = self.pregunta_actual.respuesta_correcta
        if respuesta_usuario == self.correcta:
            self.score += 1
            return True
        else:
            return False

    # _____________________________________________________________________________

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





class Juego:

    def __init__(self, q_lista):
        self.numero_pregunta = 0
        self.score = 0
        self.lista_pregunta = q_lista

    def todavia_tiene_preguntas(self):
        return self.numero_pregunta < len(self.lista_pregunta)

    def siguiente_pregunta(self):
        pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        self.numero_pregunta += 1
        respuesta_usuario = input(f"Q.{self.numero_pregunta}: {pregunta_actual.pregunta}: {pregunta_actual.respuestas} : ")
        self.comprobar_respuesta(respuesta_usuario, pregunta_actual.respuesta)

    def comprobar_respuesta(self, respuesta_usuario,respuesta_correcta):
        if respuesta_usuario == respuesta_correcta:
            self.score += 1
            print("continua a la siguiente ronda")
        else:
            print("Se acabo el juego")
        print(f"Puntuación actual: {self.score}/{self.numero_pregunta}")
        print("\n")
class Pregunta:

    def __init__(self, q_pregunta,q_respuestas, q_respuesta, q_categoria,q_dificultad,q_respuesta_incorrecta):
        self.pregunta = q_pregunta
        self.respuestas = q_respuestas
        self.respuesta = q_respuesta
        self.respuesta_incorrecta = q_respuesta_incorrecta
        self.categoria = q_categoria
        self.dificultad = q_dificultad
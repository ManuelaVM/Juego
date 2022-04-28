from Entidades.Pregunta import Pregunta
from Entidades.Ronda1 import ronda_1
from Entidades.Juego import juego
from Vista.ui import Interface

banco_preguntas = []
banco_preguntas = []
for Ronda1 in ronda_1:
    Ronda1_pregunta = Ronda1["question"]
    Ronda1_respuesta_correcta = Ronda1["correct_answer"]
    Ronda1_respuestas_incorrectas = Ronda1["incorrect_answers"]
    Ronda1_categoria = Ronda1["category"]
    Ronda1_dificultad = Ronda1["difficulty"]
    new_question = Pregunta(Ronda1_pregunta, Ronda1_respuesta_correcta, Ronda1_respuestas_incorrectas, Ronda1_categoria, Ronda1_dificultad)
    banco_preguntas.append(new_question)

juego = juego(banco_preguntas)
juego_ui = Interface(juego)

# while juego.todavia_tiene_preguntas():
#     juego.siguiente_pregunta()while juego.todavia_tiene_preguntas():
#     juego.siguiente_pregunta()

print("Fin del Juego")
print(f"Puntuacion final: {juego.score}/{juego.numero_pregunta}")


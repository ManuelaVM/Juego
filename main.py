from Pregunta import Pregunta
from Ronda1 import ronda_1
from Juego import Juego

banco_preguntas = []
for Ronda1 in ronda_1:
    Ronda1_pregunta = Ronda1["pregunta"]
    Ronda1_respuestas = Ronda1["respuestas"]
    Ronda1_respuesta = Ronda1["respuesta"]
    Ronda1_respuesta_incorrecta = Ronda1["respuesta_incorrecta"]
    Ronda1_categoria = Ronda1["categoria"]
    Ronda1_dificultad = Ronda1["dificultad"]
    new_pregunta = Pregunta(Ronda1_pregunta, Ronda1_respuestas,Ronda1_respuesta, Ronda1_categoria,Ronda1_dificultad,Ronda1_respuesta_incorrecta)
    banco_preguntas.append(new_pregunta)

juego = Juego(banco_preguntas)

while juego.todavia_tiene_preguntas():
    juego.siguiente_pregunta()

print("Fin del Juego")
print(f"Puntuacion final: {juego.score}/{juego.numero_pregunta}")

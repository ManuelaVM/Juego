import random
from Entidades.Pregunta import Pregunta
from Entidades.Ronda1 import ronda_1
from Entidades.Ronda2 import ronda_2
from Entidades.Ronda3 import ronda_3
from Entidades.Ronda4 import ronda_4
from Entidades.Ronda5 import ronda_5
from Entidades.Juego import juego
from Vista.ui import Interface


banco_preguntas = []

for Ronda1 in ronda_1:
     Ronda1_pregunta = Ronda1["question"]
     Ronda1_respuesta_correcta = Ronda1["correct_answer"]
     Ronda1_respuestas_incorrectas = Ronda1["incorrect_answers"]
     Ronda1_categoria = Ronda1["category"]
     Ronda1_dificultad = Ronda1["difficulty"]
     new_question = Pregunta(Ronda1_pregunta, Ronda1_respuesta_correcta, Ronda1_respuestas_incorrectas, Ronda1_categoria, Ronda1_dificultad)
     banco_preguntas.append(new_question)


for Ronda2 in ronda_2:
      Ronda2_pregunta = Ronda2["question"]
      Ronda2_respuesta_correcta = Ronda2["correct_answer"]
      Ronda2_respuestas_incorrectas = Ronda2["incorrect_answers"]
      Ronda2_categoria = Ronda2["category"]
      Ronda2_dificultad = Ronda2["difficulty"]
      new_question = Pregunta(Ronda2_pregunta, Ronda2_respuesta_correcta, Ronda2_respuestas_incorrectas, Ronda2_categoria, Ronda2_dificultad)
      banco_preguntas.append(new_question)

for Ronda3 in ronda_3:
      Ronda3_pregunta = Ronda3["question"]
      Ronda3_respuesta_correcta = Ronda3["correct_answer"]
      Ronda3_respuestas_incorrectas = Ronda3["incorrect_answers"]
      Ronda3_categoria = Ronda3["category"]
      Ronda3_dificultad = Ronda3["difficulty"]
      new_question = Pregunta(Ronda3_pregunta, Ronda3_respuesta_correcta, Ronda3_respuestas_incorrectas, Ronda3_categoria, Ronda3_dificultad)
      banco_preguntas.append(new_question)


for Ronda4 in ronda_4:
      Ronda4_pregunta = Ronda4["question"]
      Ronda4_respuesta_correcta = Ronda4["correct_answer"]
      Ronda4_respuestas_incorrectas = Ronda4["incorrect_answers"]
      Ronda4_categoria = Ronda4["category"]
      Ronda4_dificultad = Ronda4["difficulty"]
      new_question = Pregunta(Ronda4_pregunta, Ronda4_respuesta_correcta, Ronda4_respuestas_incorrectas, Ronda4_categoria, Ronda4_dificultad)
      banco_preguntas.append(new_question)

for Ronda5 in ronda_5:
      Ronda5_pregunta = Ronda5["question"]
      Ronda5_respuesta_correcta = Ronda5["correct_answer"]
      Ronda5_respuestas_incorrectas = Ronda5["incorrect_answers"]
      Ronda5_categoria = Ronda5["category"]
      Ronda5_dificultad = Ronda5["difficulty"]
      new_question = Pregunta(Ronda5_pregunta, Ronda5_respuesta_correcta, Ronda5_respuestas_incorrectas, Ronda5_categoria, Ronda5_dificultad)
      banco_preguntas.append(new_question)


juego = juego(banco_preguntas)
juego_ui = Interface(juego)

# while juego.todavia_tiene_preguntas():
#     juego.siguiente_pregunta()while juego.todavia_tiene_preguntas():
#     juego.siguiente_pregunta()

#print("Fin del Juego")
#print(f"Puntuacion final: {juego.score}/{juego.numero_pregunta}")


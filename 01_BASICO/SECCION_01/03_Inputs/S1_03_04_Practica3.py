'''
Crea un código que muestre en pantalla el nombre completo del usuario, permitiéndole ingresar su nombre y apellido con las siguientes instrucciones:

Escribe tu nombre:
Escribe tu apellido:
El código debe poder imprimir en pantalla el nombre y apellido del usuario, separados por un espacio.

Aclaración:

1. No deben imprimirse strings adicionales a la respuesta del usuario.

2. Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas".  Ya que el botón "Ecutar código" arrojará el siguiente error: "EOF when reading a line".

¿Aún tienes dudas acerca de por qué el módulo de evaluación no acepta tu respuesta? Hemos incluido al final de cada sección posibles respuestas a cada uno de los ejercicios. Confiamos en que puedas recurrir a ellas para detectar diferencias rápidamente, evitando que pierdas el tiempo o debas esperar por una respuesta a tu pregunta. Si aún así tienes dudas a resolver, puede ser una buena oportunidad para repasar la lección en cuestión, o utilizar el espacio de Preguntas y Respuestas que tienes a tu disposición. Muchos éxitos!
'''

nombre = input("Escribe tu nombre:")
apellido = input("Escribe tu apellido:")

print (f"{nombre} {apellido}")
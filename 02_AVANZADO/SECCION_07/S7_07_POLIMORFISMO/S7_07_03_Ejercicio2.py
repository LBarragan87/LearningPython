'''
Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
'''


import os
os.system("cls")

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
def ataque(personaje):
    personaje.atacar()
    
personaje_mago=Mago()
personaje_arquero=Arquero()
personaje_samurai=Samurai()

personajes = [personaje_arquero,personaje_mago,personaje_samurai]
for personaje in personajes:
    ataque(personaje)
'''
Crea una clase llamada Cubo, y asígnale el atributo de clase:

caras = 6

y el atributo de instancia:

color

Crea una instancia cubo_rojo, de dicho color.
'''

import os

os.system("cls")

class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo("rojo")

print (f"tengo un cubo color {cubo_rojo.color} y tiene {Cubo.caras} caras")
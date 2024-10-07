'''
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

especie = "Humano"

magico = True

edad = 17
'''

import os

os.system("cls")

class Personaje:
    real = False
    
    def __init__(self,especie, magico,edad,nombre):
        self.especie=especie
        self.magico=magico
        self.edad=edad
        self.nombre = nombre

harry_potter = Personaje("Humano",True,17,"Harry Potter")

print (f"{harry_potter.nombre} es un personage de raza {harry_potter.especie} magico: {harry_potter.magico}, de {harry_potter.edad} años")
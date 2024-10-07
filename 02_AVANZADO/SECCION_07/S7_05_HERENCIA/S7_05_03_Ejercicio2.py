#Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.

import os
os.system("cls")

class Mascota:
    def __init__(self,  edad, nombre,cantidad_patas):
        self.nombre = nombre
        self.edad = edad
        self.cantidad_patas=cantidad_patas

class Perro(Mascota):
    pass

kira = Perro(15,"kira",4)
print(f"{kira.nombre} tiene {kira.edad} años y tiene {kira.cantidad_patas} patas")
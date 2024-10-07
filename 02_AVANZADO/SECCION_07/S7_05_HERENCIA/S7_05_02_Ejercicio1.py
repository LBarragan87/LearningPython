#Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.
import os
os.system("cls")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

mi_alumno = Alumno("luis",15)
print (f"el alumno {mi_alumno.nombre} tiene {mi_alumno.edad} años")
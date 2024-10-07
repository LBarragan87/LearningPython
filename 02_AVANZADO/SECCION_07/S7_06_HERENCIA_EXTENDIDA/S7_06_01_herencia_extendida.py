'''
tipos de metodos heredados:
    * heredados
    * modificados
    * nuevos
    * heredar de muchos padres
    * transferir herencia
'''

import os
os.system("cls")

class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
        
    def nacer(self):
        print("este animal ha nacido")
        
    def hablar(self):
        print("este animal emite un sonido")
        
class Pajaro(Animal):
    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color) #permute usar self.edad y self.color de la herencia de "animal"
        self.altura=altura_vuelo
    
    def hablar(self):
        print("Pio")

    def volar(self,metros):
        print (f"el pajaro vuela {metros} mts")
        
        
piolin = Pajaro(3,"Amarillo",60)
piolin.nacer()
piolin.hablar()
piolin.volar(25)

nuevo_animal = Animal(23,"negro")

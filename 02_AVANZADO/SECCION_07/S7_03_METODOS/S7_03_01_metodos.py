'''
class Pajaro:
    def __init__(self,color,especie):
        self.color=color
        self.especia=especie
        
    *ejemplo 1 de un methodo en una clase
    def piar(self):
        print("pio")

    *ejemplo 2 de un methodo en una clase    
    def volar(self, metros):
        print(f"volo {metros} mts")
'''
import os
os.system("cls")
class Pajaro:
    def __init__(self,color,especie):
        self.color=color
        self.especia=especie
        
    def piar(self):
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print (f"el pajaro ha volado {metros} mts")

piolin = Pajaro("azul","canario")
piolin.piar()

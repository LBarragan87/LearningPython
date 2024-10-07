#Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

import os
os.system("cls")

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
        
kira=Mascota()
kira.respirar()
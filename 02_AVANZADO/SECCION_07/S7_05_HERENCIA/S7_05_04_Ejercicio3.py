#Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.

import os
os.system("cls")

class Vehiculo:
    def acelerar(self):
        print("el vehiculo ha acelerado")
    def frenar(self):
        print("el vehiculo ha frenado")

class Automovil(Vehiculo):
    pass

mi_carro = Automovil()
mi_carro.acelerar()
mi_carro.frenar()
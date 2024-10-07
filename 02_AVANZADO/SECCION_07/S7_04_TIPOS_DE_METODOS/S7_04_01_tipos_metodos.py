'''
decoradores:
    metodos de instancia -> def(self), pueden acceder y modificar atributos del objeto, acceder a otros metodos de la clase, y modificar estado de la clase
    
    metodos de clase -> @class method -> def (cls), no pueden modificar atributos de la instancia, pero si atributos de la clase
    
    metodos estaticos -> @static method
'''

import os
os.system("cls")

class Pajaro:
    
    alas=True
    
    def __init__(self,color,especie):
        self.color=color
        self.especia=especie
        
    def piar(self):
        print(f"pio, mi color es {self.color}")
        
    def volar(self, metros):
        print (f"el pajaro ha volado {metros} mts")
        #ejemplo de metodo accediendo a otros metodos
        self.piar()
        
    'ejemplo de metodo de instancia, modificando atributo del objeto'
    def pintar_negro(self):
        self.color="negro"
        print(f"ahora el pajaro es {self.color}")
        
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas=False

    @staticmethod
    def mirar():
        print("el pajaro mira")

piolin = Pajaro("azul","canario")
piolin.piar()
piolin.pintar_negro()
print(piolin.color)
piolin.volar(20)

#ejemplo de modificacion de parametro de clase que solo afecta a objeto
piolin.alas=False
print(piolin.alas)

nuevo_pajaro = Pajaro("Amarillo","cotorro")
print(nuevo_pajaro.alas)

#ejemplo de modificaciond e parametro de clase que afecta a todos los objetos de la clase
Pajaro.alas=False


avestruz=Pajaro("negro","avestruz")
print(f"avestruz tiene alas: {avestruz.alas}")
print(f"nuevo_pajaro tiene alas: {nuevo_pajaro.alas}")
print(f"piolin tiene alas: {piolin.alas}")
piolin.poner_huevos(7)

Pajaro.poner_huevos(5)
print(Pajaro.alas)
Pajaro.mirar()
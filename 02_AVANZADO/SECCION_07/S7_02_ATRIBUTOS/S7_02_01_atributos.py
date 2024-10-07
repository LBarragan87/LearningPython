import os

os.system("cls")

class Pajaro():
    
    #atributos de clase, se aplican a todos los objetos construidos, sin necesidad de especificarlo
    alas = True
    #aqui terminan los atributos de clase
    
    #atributos de instancia (varian de acuerdo a la construccion del objeto)
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie
    #aqui terminan los atributos de instancia

mi_pajaro = Pajaro("azul","tucan")
print(f"mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
print(mi_pajaro.alas)




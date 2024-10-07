import os
os.system("cls")

class Animal:
    def __init__(self, edad,color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print("este animal ha nacido")

class Pajaro(Animal):
    pass

print(Pajaro.__bases__)
print(Animal.__subclasses__())

piolin = Pajaro(12,"amarillo")
piolin.nacer()
print(f"piolin es un pajaro color {piolin.color}, y tiene {piolin.edad} años")
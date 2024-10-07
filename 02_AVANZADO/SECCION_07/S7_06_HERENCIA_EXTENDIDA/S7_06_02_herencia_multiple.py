import os
os.system("cls")

class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def reir(self):
        print("jajaja")

    def hablar(self):
        print("que tal")
class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__) # <- mro = method resolution order

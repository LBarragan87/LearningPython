import os
os.system("cls")

class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f"{self.nombre} dice 'muuuu'")
        
class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f"{self.nombre} dice 'beeee'")     
        
        
print ("---metodo desde objeto---")        
mi_vaca=Vaca("chencha")
mi_vaca.hablar()

mi_oveja=Oveja("lencha")
mi_oveja.hablar()

print ("---metodo desde objeto en loop---")  
animales =[mi_vaca,mi_oveja]
for animal in animales:
    animal.hablar()
    
def animal_habla(animal):
    animal.hablar()

print ("---metodo desde funcion en objeto---")  
animal_habla(mi_vaca)
animal_habla(mi_oveja)

print ("---metodo desde funcion en loop---")  
for animal in animales:
    animal_habla(mi_oveja)
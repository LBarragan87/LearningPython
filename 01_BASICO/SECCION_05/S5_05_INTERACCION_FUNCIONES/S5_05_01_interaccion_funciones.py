'''
---simular seleccion de palitos---
crear lista inicial
mezclar palitos
pedir intento
comprobar intento
'''

from random import shuffle

palitos=["-","--","---","----"]


def mezclar(lista):
    shuffle(lista)
    return lista

#print (mezclar(palitos))

def probar_suerte():
    intento=0 
    while intento not in [1,2,3,4]:
        intento=int(input("elige un numero del 1 al 4: "))
        if intento not in [1,2,3,4]:
            print("ingresa un numero Valido")
    return intento
        
    
#print (probar_suerte())

def chequear_intento(intento,lista):
    if lista[intento - 1]=="-":
        print("A lavar los platos!")
    else:
        print("te haz salvado")
    print(f"te ha tocado {lista[intento-1]}")
    

palitos_mezclados=mezclar(palitos)
print(palitos_mezclados)
chequear_intento(probar_suerte(),palitos_mezclados)
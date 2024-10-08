'''
Crea un Generador de nombre para tu cerveza
-interfaz debe preguntar:
    * Nombre de ciudad que te gustaria visitar
    * color favorito

- Programa debe responder con mensaje que concatene los datos ingresados:

'''
import os


def gen_nombre_cerveza(ciudad, color):
    '''
    mensaje que genera nombre de cerveza
    '''
    print((f"El nombre de tu cerveza es:{ciudad} {color}"))


def generador_nombre_cerveza():
    '''
    modulo que genera nombre de cerveza
    '''
    os.system("cls")
    get_ciudad = input("Que ciudad te gustaria visitar?: ")
    get_color = input("Cual es tu color favorito?: ")
    gen_nombre_cerveza(get_ciudad, get_color)


generador_nombre_cerveza()

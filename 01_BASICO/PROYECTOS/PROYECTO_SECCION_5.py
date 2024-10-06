'''
JUEGO DE AHORCADO
*crear lista de palabras secretas
mostrar a jugador serie de guines para representar cada letra
si la letra se encuentra entre la palabra secreta, mostrar actualizada la palabra secreta
si la letra no existe, el jugador pierde una vida
se tendran 6 vidas
si se terminan las vidas, el jugador pierde
si se descubre la palabra antes de perder las vidas el jugador gana

funciones requeridas:
choice para seleccionar palabra al azar
*funcion para pedir una letra
*validar la letra
*checar letra
*ver si gano
'''

'''
adicional se detecta si se intenta ingresar mas de 1 letra
se indica la cantidad de intentos para ganar el juego
'''
from random import choice

def palabra_juego(palabra_secreta):
    largo_palabra=len(palabra_secreta)
    x=1
    status_palabra=[]
    while x<=largo_palabra:
        status_palabra.append(" _ ")
        x+=1
    return(status_palabra)

def pide_letra():
    cantidad_letras=0
    while cantidad_letras != 1:
        ingreso_letra = input("ingresa una letra: ")
        cantidad_letras=len(ingreso_letra)
        if cantidad_letras>1:
            print("NO PUEDES INGRESAR MAS DE UNA LETRA, INTENTA NUEVAMENTE")
    return ingreso_letra.upper()


def validar_letra(letra,letras_ingresadas):
        if letra in letras_ingresadas:
            print("ya usaste esta letra, escoge otra")
            status=True
        else:
            letras_ingresadas.append(letra)
            #print(letras_ingresadas)
            status=False
        return status
        
def checar_letra(letra,palabra_secreta,vidas_actual):
    if letra in palabra_secreta:
        print (f"la letra {letra} es parte de la palabra secreta")
        vidas_actual=vidas_actual
    else:
        print (f"la letra {letra} NO es parte de la palabra secreta, te quedan {vidas_actual-1} vidas")
        vidas_actual-=1
    return vidas_actual

def palabra_desbloqueada(letra,palabra_secreta,status_palabra,letras_faltantes):
    actualizacion_status=status_palabra
    x=0
    for letra_secreta in palabra_secreta:
        if letra == letra_secreta:
            status_palabra[x] = letra
            letras_faltantes-=1
        else:
            status_palabra[x]=status_palabra[x]
            letras_faltantes=letras_faltantes
        x+=1
        
    print(actualizacion_status)
    return(actualizacion_status,letras_faltantes)
    
def ahorcado():
    vidas=6
    lista_palabras=["hola","mundo","jugar","python","avengers","anime","musica"]
    palabra_secreta=choice(lista_palabras).upper()
    #print(palabra_secreta)
    letras_pendientes=len(palabra_secreta)
    jugador=input("ingresa tu nombre: ")
    print(f"bienvenido {jugador}, intenta descubril la palabra secreta:")
    print(palabra_juego(palabra_secreta))
    lista_letras=[]
    status_palabra=palabra_juego(palabra_secreta)
    while vidas > 0:
        solicita_letra=pide_letra()
        status_letra=validar_letra(solicita_letra,lista_letras)
        while status_letra==True:
            solicita_letra=pide_letra()
            status_letra=validar_letra(solicita_letra,lista_letras)
        else: 
            resultado_vidas=checar_letra(solicita_letra,palabra_secreta,vidas)
            vidas=resultado_vidas
            status_juego=palabra_desbloqueada(solicita_letra,palabra_secreta,status_palabra,letras_pendientes)
            status_palabra=status_juego[0]
            letras_pendientes=status_juego[1]
            if letras_pendientes == 0:
                print(f"FELIZIDADES!, DESCIFRASTE LA PALABRA SECRETA '{palabra_secreta}' CON {len(lista_letras)} INTENTOS")
                break
    else:
        print("haz perdido!, ya no tienes vidas!")

ahorcado()
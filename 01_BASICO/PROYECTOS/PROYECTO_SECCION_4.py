'''
PROGRAMAR JUEGO "ADIVINA EL NUMERO"
pedir a usuario:
-nombre

imprimir:
-nombre de usuario
-avisar que se ha pensado en un numero entre 1-100 y tiene 8 intentos para adivinar
-avisar al usuario si se indico un numero fuera de rango (no quita vidas)
-con cada intento indicar si el numero dado es mayo o menor al numero pensado
-avisar que encontro el numero secreto, y cuantos intentos ha gastado
'''
import os

os.system("cls")
from random import randint

numero_menor=1
numero_mayor=100
numero_secreto=randint(numero_menor,numero_mayor)

usuario=input("ingresa tu nombre: ")
vidas_inicial=8
total_intentos=0
lista_intentos=[]
os.system("cls")
print(f"hola {usuario}, intenta adivinar el numero secreto (entre {numero_menor} y {numero_mayor}), tienes 8 intentos")
while vidas_inicial>0:
    valor_intento=int(input("ingresa un numero: "))
    if valor_intento in lista_intentos:
        print (f"ya intentaste con el numero {valor_intento}, selecciona otro numero")
    else:   
        lista_intentos.append(valor_intento) 
        if valor_intento<numero_menor or valor_intento>numero_mayor:
            print(f"el numero ingresado '{valor_intento}' esta fuera del rango")
        else:
            if valor_intento<numero_secreto:
                print(f"el numero ingresado '{valor_intento}' es menor al numero secreto, te quedan {vidas_inicial-1} intentos")
                vidas_inicial-=1
                total_intentos+=1

            elif valor_intento>numero_secreto:
                print(f"el numero ingresado '{valor_intento}' es mayor al numero secreto, te quedan {vidas_inicial-1} intentos")
                vidas_inicial-=1
                total_intentos+=1
            elif valor_intento==numero_secreto:
                total_intentos+=1
                os.system("cls")
                print(f"felicidades {usuario}, el numero secreto era '{valor_intento}', y lo descubriste en {total_intentos} intentos")
                break
else:
    os.system("cls")
    print(f"{usuario} no descubriste el numero secreto '{numero_secreto}', y te quedaste sin intentos")
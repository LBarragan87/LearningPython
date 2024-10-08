'''
calculo de comiciones de vendedores 13%
-interfaz debe preguntar:
    * Nombre
    * Ventas

- Programa debe responder con mensaje que indique:
    * Nombre
    * Monto correspondiente a las ventas
'''
import os


def calculo_comision(monto_ventas):
    '''
    calculo de comision
    '''
    return monto_ventas*0.13


def mensaje_comision(nombre, comision):
    '''
    mensaje de aviso a usuario por comision calculada
    '''
    print(f"Hola {nombre}, este mes ganaste $ {comision:,.2f}")
    return comision


def calcula_comision_vendedor():
    '''
    modulo que calcula comision de acuerdo a datos recibidos
    '''
    os.system("cls")
    get_nombre = input("Indica tu nombre: ")
    get_ventas = int(input("Indique monto de Ventas alcanzadas en el mes: "))
    comision = calculo_comision(get_ventas)
    mensaje_comision(get_nombre, comision)


calcula_comision_vendedor()

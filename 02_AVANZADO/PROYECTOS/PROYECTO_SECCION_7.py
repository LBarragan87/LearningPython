'''
PROGRAMAR CUENTA BANCARIA
CREAR CLASE PERSONA CON ATRIBUTOS:
    * NOMBRE Y APELLIDO

CLASE CLIENTE HEREDAR ATRITUBOS DE PERSONA, ADICINAL TENER ATRIBUTOS:
    * NUMERO DE CUENTA, BALANCE

CLASE CLIENTE DEBE TENER LOS SIGUIENTES METODOS:
    - IMPRIMIR: DATOS DE CLIENTE Y BALANCE DE CUENTA
    - DEPOSITAR
    - RETIRAR

INTERFAZ QUE PIDA:
    - IMPRIMIR DATOS
    - DEPOSITAR
    - RETIRAR
    - SALIR

FUNCIONES:
    - CREAR CLIENTE
    - INICIO
'''

import os
os.system("cls")


class Persona():
    '''
    templete para creacion de personas
    '''
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    '''
    templete para creacion de clientes
    '''
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir(self):
        '''
        se imprime informacion del estado de cuenta del cliente
        '''
        print(f"{self.nombre} {self.apellido}")
        print(f"numero de cuenta: {self.numero_cuenta}")
        print(f"balance: {self.balance}")

    def depositar(self, cantidad):
        '''
        se realiza transaccion de deposito
        '''
        print(f"se ha depositado la cantidad de {cantidad}, su saldo despues "
              "de la operacion es {self.balance+cantidad}")
        self.balance = self.balance+cantidad
        return self.balance

    def retirar(self, cantidad):
        '''
        se realiza transaccion de retiro
        '''
        print(f"se ha retirado la cantidad de {cantidad}, su saldo despues de "
              "la operacion es {self.balance-cantidad}")
        self.balance = self.balance-cantidad
        return self.balance


def inicio_banco():
    '''
    iniciar interfaz de banco
    '''
    seleccion = "a"
    while seleccion != "D":
        os.system("cls")

        print(f"Bienvenido {cliente_actual.nombre} {cliente_actual.apellido}")
        print("Que accion deceas Realizar?: ")
        print("A) Imprimir")
        print("B) Depositar")
        print("C) Retirar")
        print("D) Salir")

        seleccion = (input("indique la opcion deceada: ")).upper()
        os.system("cls")

        if seleccion == "A":
            cliente_actual.imprimir()
            continuar = (input("Regresar al menu anterior (Y/N)?: ")).upper()
            if continuar == "Y":
                seleccion = "A"
            else:
                seleccion = "D"
        elif seleccion == "B":
            cliente_actual.depositar(float(input("ingrese cantidad a "
                                                 "depositar: ")))
            continuar = (input("Regresar al menu anterior (Y/N)?: ")).upper()
            if continuar == "Y":
                seleccion = "A"
            else:
                seleccion = "D"
        elif seleccion == "C":
            balance = -1
            while balance < 0:
                deseado_retirar = float(input("ingrese monto a retirar: "))
                balance = cliente_actual.balance - deseado_retirar
                if cliente_actual.balance == 0:
                    print("no tienes fondo, tu saldo es "
                          "{cliente_actual.balance}")
                    continuar = (input("presione cualquier tecla para regresar"
                                       " al menu anterior: ")).upper()
                    inicio_banco()
                elif balance < 0:
                    print("fondos insuficientes, tu saldo es "
                          "{cliente_actual.balance}")
                else:

                    cliente_actual.retirar(deseado_retirar)

                    continuar = (input("Regresar al menu anterior "
                                       "(Y/N)?: ")).upper()
                    if continuar == "Y":
                        seleccion = "A"
                    else:
                        seleccion = "D"


cliente_actual = Cliente("Luis", "Barragan", "123123", 0)

inicio_banco()

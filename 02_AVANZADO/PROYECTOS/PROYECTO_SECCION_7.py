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
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance

    def imprimir(self):
        print(f"{self.nombre} {self.apellido}")
        print(f"numero de cuenta: {self.numero_cuenta}")
        print(f"balance: {self.balance}")
        
    def depositar(self,cantidad):
        print (f"se ha depositado la cantidad de {cantidad}, su saldo despues de la operacion es {self.balance+cantidad}")
        self.balance=self.balance+cantidad
        return self.balance
        
    def retirar(self,cantidad):
        print (f"se ha retirado la cantidad de {cantidad}, su saldo despues de la operacion es {self.balance-cantidad}")
        self.balance=self.balance-cantidad
        return self.balance


def crear_cliente():
    nombre=input("ingrese nombre cliente: ")
    apellido=input("ingrese apellido cliente: ")
    asignar_cuenta=input("asignar numero de cuenta: ")
    mi_cliente = Cliente(nombre,apellido,asignar_cuenta,0)

def interfaz_banco():
    seleccion = "a"
    while seleccion != "D":
        import os
        os.system("cls")
        
        print(f"Bienvenido {cliente_actual.nombre} {cliente_actual.apellido}")
        print(f"Que accion deceas Realizar?: ")
        print(f"A) Imprimir")
        print(f"B) Depositar")
        print(f"C) Retirar")
        print(f"D) Salir")
        
        seleccion = (input(f"indique la opcion deceada: ")).upper()
        os.system("cls")
        
        if seleccion == "A":
            cliente_actual.imprimir()
            continuar=(input("Regresar al menu anterior (Y/N)?: ")).upper()
            if continuar == "Y":
                seleccion = "A"
            else:
                seleccion = "D"
        elif seleccion == "B":
            cliente_actual.depositar(float(input("ingrese cantidad a depositar: ")))
            continuar=(input("Regresar al menu anterior (Y/N)?: ")).upper()
            if continuar == "Y":
                seleccion = "A"
            else:
                seleccion = "D"              
        elif seleccion == "C":
            balance = -1
            while balance<0:
                deseado_retirar=float(input("ingrese monto a retirar: "))
                balance = cliente_actual.balance - deseado_retirar
                if cliente_actual.balance==0:
                    print (f"no tienes fondo, tu saldo es {cliente_actual.balance}")
                    continuar=(input("presione cualquier tecla para regresar al menu anterior: ")).upper()
                    interfaz_banco()
                elif balance<0:
                    print (f"fondos insuficientes, tu saldo es {cliente_actual.balance}")
                else:
                        
                    cliente_actual.retirar(deseado_retirar)
            
                    continuar=(input("Regresar al menu anterior (Y/N)?: ")).upper()
                    if continuar == "Y":
                        seleccion = "A"
                    else:
                        seleccion = "D"        
                
                
                
                
            
            
    """  
          while
            respuesta=input(f"desea regresar al menu anterior (S/N)?: ")
            if respuesta == "S":
                interfaz_banco()
            elif respuesta == "N":
                break
            else:
                print() 
            """
  

    
#cliente_actual=crear_cliente()
cliente_actual=Cliente("Luis","Barragan","123123",0)

#aqui comienza la ejecucion del codigo
interfaz_banco()

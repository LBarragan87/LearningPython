''''
crear software que funcione como turnero de una farmacia
preguntar por area de servicio:
    * perfumeria
    * cosmetica
    * farmacia

salida de numero:
    "su turno es: "
    "X-00"
    "aguarde y sera atendido"
'''
import os


def select_funcion(seleccion):
    print("Su Turno es: ")
    if seleccion == "F":
        print(f"F - {next(f)}")
    elif seleccion == "C":
        print(f"C - {next(c)}")
    elif seleccion == "P":
        print(f"P - {next(p)}")
    print("Espere y sera atendido")


def gen_turno_farmacia():
    x = 0
    while True:
        x += 1
        yield x


def gen_turno_cosmetica():
    x = 0
    while True:
        x += 1
        yield x


def gen_turno_perfumeria():
    x = 0
    while True:
        x += 1
        yield x


def opciones():
    teclas_deseadas = ["F", "C", "P"]
    print("Bienvenido, a que area desea pasar:"
          "\nF) farmacia \nC) cosmetica\nP) perfumeria")

    valid_area = False
    while valid_area is False:
        select_area = (input("Seleccione Area Deseada: ")).upper()
        valid_area = select_area in teclas_deseadas
    return select_area


def siguiente():
    os.system("cls")


def turnero():
    turnero_encendido = True
    while turnero_encendido:
        select_area = opciones()
        select_funcion(select_area)
        turnero_encendido = input("Presione cualquier letra para generar"
                                  "nuevo turno:")
        if turnero_encendido == "Apagar":
            turnero_encendido = False
        os.system("cls")


f = gen_turno_farmacia()
c = gen_turno_cosmetica()
p = gen_turno_perfumeria()


os.system("cls")
turnero()

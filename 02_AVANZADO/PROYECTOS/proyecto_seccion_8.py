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
    '''impresion de turnos'''
    print("*"*25)
    print("Su Turno es: ")
    if seleccion == "F":
        print(f"F - {next(f)}")
    elif seleccion == "C":
        print(f"C - {next(c)}")
    elif seleccion == "P":
        print(f"P - {next(p)}")
    print("Espere y sera atendido")
    print("*"*25)


def gen_turno_farmacia():
    '''generador de turnos a farmacia'''
    x = 0
    while True:
        x += 1
        yield x


def gen_turno_cosmetica():
    '''generador de turnos a cosmetica'''
    x = 0
    while True:
        x += 1
        yield x


def gen_turno_perfumeria():
    '''generador de turnos a perfumeria'''
    x = 0
    while True:
        x += 1
        yield x


def opciones():
    '''genera opciones de turnero'''
    teclas_deseadas = ["F", "C", "P"]
    print("Bienvenido, a que area desea pasar:"
          "\nF) farmacia \nC) cosmetica\nP) perfumeria")

    valid_area = False
    while valid_area is False:
        select_area = (input("Seleccione Area Deseada: ")).upper()
        valid_area = select_area in teclas_deseadas
    return select_area


def turnero():
    '''aplicacion principal de turnero'''
    print("Bienvenido a Farmacias 'Lugan'")
    turnero_encendido = True
    while turnero_encendido:
        select_area = opciones()
        select_funcion(select_area)
        siguiente_apagar = (input("Regresar a menú anterior:")).upper()
        if siguiente_apagar == "APAGAR":
            turnero_encendido = False
        os.system("cls")


f = gen_turno_farmacia()
c = gen_turno_cosmetica()
p = gen_turno_perfumeria()


os.system("cls")
turnero()

'''ejercicio decoradores'''

'''
def cambiar_letras(tipo):
    def mayuscula(texto):


        print(texto.upper())

    def minuscula(texto):

        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


operacion = cambiar_letras("may")

operacion("palabra")
'''


def decorar_saludos(funcion):
    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion


@decorar_saludos
def mayusculas(texto):
    print(texto.upper())


@decorar_saludos
def minusculas(texto):
    print(texto.lower())


mayusculas("python")


mayuscula_decorada = decorar_saludos(mayusculas)
mayuscula_decorada("Luis")

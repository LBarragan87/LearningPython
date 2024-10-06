#al usar palabra clave en funcion, se convierte en un valor que se puede asignar a una variable

def multiplicar(numero1,numero2):
    return (numero1*numero2)

def multiplicar_sin_return(numero1,numero2):
    print (f"printed -> {numero1*numero2}")

x=multiplicar(4,5)
print(x)

y=multiplicar_sin_return(4,5)
print(f"returned -> {y}")
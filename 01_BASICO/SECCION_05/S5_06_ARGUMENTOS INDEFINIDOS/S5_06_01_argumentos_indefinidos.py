# *args y **kwargs
# numero indefinido de argumentos, la variable se puede renombrar, debe iniciar con *


def suma(*numeros):
    total = 0
    for numero in numeros:
        total+=numero
    return total

print(suma(3,4,7,15))
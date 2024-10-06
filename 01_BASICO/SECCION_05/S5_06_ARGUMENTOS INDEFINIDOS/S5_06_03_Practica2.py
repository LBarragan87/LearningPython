#Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*numeros):
    resultado=0
    for numero in numeros:
        resultado = resultado+(abs(numero))
    return resultado

print(suma_absolutos(2,-2))
def chequear_3cifras(numero):
    return numero in range (100,1000)

resultado=chequear_3cifras(5)
#print(resultado)

suma = 586+348
resultado=chequear_3cifras(suma)
#print(resultado)


def multi_chequeo_3_cifras(lista_numeros):
    chequeo=[]
    for n in lista_numeros:
        if n in range(100,1000):
            chequeo.append(True)
        else:
            chequeo.append(False)
    return (chequeo)

lista_numeros=[900,25,750,10000]
nuevo_resultado=multi_chequeo_3_cifras(lista_numeros)
print (nuevo_resultado)
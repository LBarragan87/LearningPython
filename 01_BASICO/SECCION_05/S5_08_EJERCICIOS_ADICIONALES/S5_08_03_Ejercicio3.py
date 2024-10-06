'''
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''

def cero_consecutivo(*numeros):
    index=0
    for numero in numeros:
        if index>0:
            if numeros[index] == 0 and numeros[index-1] == 0:
                consecutivo=True
                break
            else:
                consecutivo=False
        index+=1
            
    return (consecutivo)

print (cero_consecutivo(1,2,3,0,4,0,5,0,0))
#integers
edad = 45
poblacion = 45500
dias_restantes = 25
n_cliente = 563

#floats
grados = -3.5
valor = 65.71
altura = 1.76

mi_numero = 1
print (mi_numero)
print (type(mi_numero))

mi_numero = 1+7
print (mi_numero)
print (mi_numero + mi_numero)
print (type(mi_numero))

mi_numero = 4 + 7.15
print (mi_numero)
print (type(mi_numero))

edad = input("dime tu edad: ")
cast_edad = int(edad)

print (f"tu edad es {edad}")
print (type(edad))
print (type(cast_edad))

#suma1 = edad + 5 <- str + float no posible
años_transcurrir=5
suma2 = cast_edad + años_transcurrir

#print (suma1)
print (f"tu edad en {años_transcurrir} años sera {suma2} años")
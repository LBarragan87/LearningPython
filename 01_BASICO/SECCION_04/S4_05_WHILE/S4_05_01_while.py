"""
loom 'mientras que' -> palabra reservada while
se puede usar condicionate 'else'

break
continue
pass
"""

monedas = 25
while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas-=1
else:
    print (f"se acabaron las monedas")
    
x="hola mundo"
for letra in x:
    pass

#uso de break
nombre = input("tu nombre: ")
for letra in nombre:
    if letra == "r":
        break
    print(letra)
    
#uso de continue
nombre = input("tu nombre: ")
for letra in nombre:
    if letra == "r":
        continue
    print(letra)
    
    
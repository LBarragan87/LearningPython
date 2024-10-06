# **kwargs! -> argumentos, debe usarse **

def suma (**kwargs):
    #print (type(kwargs))
    total=0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total +=valor
    return total

print(suma(x=3,y=5,z=2))

def prueba(num1,num2,*args,**kwargs):
    print (f"el primer valor es {num1}")
    print (f"el segundo valor es {num2}")    
    
    for arg in args:
        print(f"arg = {arg}")
        
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

print(prueba(5,7,9,10,15,25,30,x=1,y=2,z=3))

def prueba2(sumar,doblar,elevar2):
    suma=0
    doblados=0
    cuadrados=0
    for elemento in sumar:
        suma+=elemento
    for elemento in doblar:
        doblados+=(elemento*2)
    for elemento in elevar2:
        cuadrados+=(elemento**2)
    print(f"total de suma de numeros naturales: {suma}")
    print(f"total de suma de numeros multiplicados x 2: {doblados}")
    print(f"total de suma de numeros elevados a la segunda potencia: {cuadrados}")

valores=[1,2,3]
prueba2(valores,valores,valores)
'''
Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
'''

def describir_persona(nombre,**descripciones):
    print(f"Características de {nombre}:")
    for nombre_argumento,valor_argumento in descripciones.items():
        print(f"{nombre_argumento}: {valor_argumento}")
        
describir_persona("María", color_ojos="azules", color_pelo="rubio", altura=1.80,peso=70)
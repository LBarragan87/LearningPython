'''
Hemos visto en la lección de qué manera se implementa el manejo de errores
habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré
que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado:
deberás implementarlo DENTRO de la función. En forma de comentario, verás un
ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la
que hemos visto en clase.

Implementa un manejador de errores dentro de la siguiente función,
abrir_archivo():

En caso de que el archivo que se intenta abrir no pueda ser hallado
(FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue
encontrado"

En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error
desconocido"

Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"

En todos los casos, al finalizar, imprimir: "Finalizando ejecución"
'''


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
        leer_archivo = archivo.readlines()
        print(leer_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except ValueError:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

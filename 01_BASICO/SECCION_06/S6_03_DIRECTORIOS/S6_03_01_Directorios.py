#navegar entre careptas
#importar pathlib
#importar OS
#getcwd - > get current worked directory
#chdir -> change directory
#makedirs -> crear directorio nuevo
#rmdir -> remove directory (no puede eliminar carpeta con archivos)
import os

ruta = os.getcwd()
print (f"la ruta actual es es -> {ruta}")

print("---abriendo archivo desde otro directorio---")
nueva_ruta = os.chdir("E:\\04-CURSOS_UDEMY\\PYTHON\\01_BASICO\\SECCION_06\\S6_03_DIRECTORIOS\\Directorio_nuevo")
ruta = os.getcwd()
print (f"la ruta nueva es -> {ruta}")
archivo = open("archivo.txt","r")
texto = archivo.readlines()
print(texto)

nueva_ruta = os.chdir("E:\\04-CURSOS_UDEMY\\PYTHON\\01_BASICO\\SECCION_06\\S6_03_DIRECTORIOS\\Directorio_nuevo")
ruta = os.getcwd()
nueva_carpeta="carpeta_creada"
#crear_carpeta = os.makedirs(f"{ruta}\\\\{nueva_carpeta}")
#nueva_ruta = os.chdir(f"{ruta}\\\\{nueva_carpeta}")

archivo = open("archivo_creado.txt","a")
print(f"se creo la carpeta '{nueva_carpeta}' en la ubicacion {ruta}")
#print (os.path.basename(nueva_ruta))

#eliminar carpeta
os.rmdir("E:\\04-CURSOS_UDEMY\\PYTHON\\01_BASICO\\SECCION_06\\S6_03_DIRECTORIOS\\Directorio_nuevo\\carpeta_creada")
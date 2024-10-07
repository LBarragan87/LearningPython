from pathlib import Path

base = Path.home()
guia=Path(base,"europa","españa",Path("Barcelona","sagrada_familia.txt"))
#guia2 = guia.with_name("la pedrera.txt")
#print(guia)
#print(guia2)
#print(base)
#print(guia.parent.parent.parent)

#obtener archivos inmediatos dentro de carpeta con terminacion especifica
carpeta_europa = Path("E:/04-CURSOS_UDEMY/PYTHON/01_BASICO/SECCION_06/S6_03_DIRECTORIOS/EUROPA")
for txt in carpeta_europa.glob("*.*"):
    print(txt)

#obtener archivos de todas las carpetas y subcarpetas
carpeta_europa = Path("E:/04-CURSOS_UDEMY/PYTHON/01_BASICO/SECCION_06/S6_03_DIRECTORIOS/EUROPA")
for txt in carpeta_europa.glob("**/*.*"):
    print(txt) #trae path hasta el archivo, incluyendo extencion
    print(txt.name) #extrae nombre del archivo incluyendo su extension
    print(txt.stem) #extrae nombre del archivo sin extension
    print(txt.suffix) #extrae la extension del archivo
    print(txt.parent) #extrae la ruta hasta la penultima parte del path, se puede utilizar multiples veces

#purewindowspath, convierte cualquier ruta en solo ruta de windows
from pathlib import Path,PureWindowsPath

carpeta = Path("E:/04-CURSOS_UDEMY/PYTHON/01_BASICO/SECCION_06/S6_03_DIRECTORIOS/Directorio_nuevo")
archivo = carpeta / "archivo.txt"

mi_archivo=open(archivo)
print(mi_archivo.read())
mi_archivo.close()

#se puede accesar archivo directo desde path
carpeta2=Path("E:/04-CURSOS_UDEMY/PYTHON/01_BASICO/SECCION_06/S6_03_DIRECTORIOS/Directorio_nuevo/archivo.txt")
print(carpeta2.read_text())
print(carpeta2.name)
print(carpeta2.suffix)

if not carpeta.exists:
    print("este archivo no existe")
else:
    print("genial, existe!")
    

ruta_windows=PureWindowsPath(carpeta2)
print(ruta_windows)
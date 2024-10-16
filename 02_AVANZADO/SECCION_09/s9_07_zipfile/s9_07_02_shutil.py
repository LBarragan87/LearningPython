import shutil

carpeta_origen = "E:\\04-CURSOS_UDEMY\\PYTHON"

archivo_destino = "todo_comprimido_2"
shutil.make_archive(archivo_destino, "zip", carpeta_origen)

shutil.unpack_archive("todo_comprimido_2.zip", "descomprimido", "zip")

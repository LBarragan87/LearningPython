'''
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando
sea invocada.
'''
import datetime

hoy = datetime.datetime.now().date()

print(hoy)

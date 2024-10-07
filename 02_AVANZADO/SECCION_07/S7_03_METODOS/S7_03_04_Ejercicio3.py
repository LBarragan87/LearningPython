'''
Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"
'''

import os
os.system("cls")

class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
mi_alarma = Alarma()
mi_alarma.postergar(15)
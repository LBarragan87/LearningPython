#Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.


import os
os.system("cls")

class Jugador:

    vivo=False

    @classmethod
    def revivir(cls):
        cls.vivo=True
        print(f"el jugador ha revivido")
        
mi_jugador = Jugador()
mi_jugador.revivir()
'''
Crea un generador que reste una a una las vidas de un personaje de videojuego,
y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida
'''


def vidas():
    x = 4
    while True:
        x -= 1
        if x > 0:
            yield f"Te quedan {x} vidas"
        else:
            yield "Game Over"


perder_vida = vidas()

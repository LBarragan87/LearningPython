import pygame

'''inicializar pygame'''
pygame.init()


'''crear pantalla'''
pantalla = pygame.display.set_mode((1600, 1200))


'''titulo e icono'''
pygame.display.set_caption("squirrel_attack")
icono = pygame.image.load("squirrell.png")
pygame.display.set_icon(icono)


'''jugador'''
img_jugador = pygame.image.load("squirrel_character.png")
pixeles_jugador = 128
jugador1_x = 800-(pixeles_jugador/2)
jugador1_y = 1200-pixeles_jugador
jugador1_x_cambio = 0
jugador1_y_cambio = 0


def jugador1(x, y):
    pantalla.blit(img_jugador, (x, y))


'''loop del juego'''
se_ejecuta = True
while se_ejecuta:
    '''fondo rgb'''
    pantalla.fill((205, 144, 228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador1_x_cambio = -0.1
            elif evento.key == pygame.K_RIGHT:
                jugador1_x_cambio = 0.1
            elif evento.key == pygame.K_UP:
                jugador1_y_cambio = -0.1
            elif evento.key == pygame.K_DOWN:
                jugador1_y_cambio = 0.1
        if evento.type == pygame.KEYUP:
            if (evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT
                    or evento.key == pygame.K_UP
                    or evento.key == pygame.K_DOWN):
                jugador1_x_cambio = 0
                jugador1_y_cambio = 0

    jugador1_x += jugador1_x_cambio
    jugador1_y += jugador1_y_cambio

    jugador1(jugador1_x, jugador1_y)

    pygame.display.update()

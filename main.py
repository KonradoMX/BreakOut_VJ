import sys
import pygame

from Bolita import Bolita
from Paleta import Paleta
from Muro import Muro

ANCHO = 640
ALTO = 480
color_azul = (0, 0, 64) #Color azul para el fondo.

#inicializando pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
#Configurar t+itulo de la ventana
pygame.display.set_caption("Juego de ladrillos")
#Crear el reloj.
reloj = pygame.time.Clock()
#Ajustar repetición de evento de tecla presionada.
pygame.key.set_repeat(30)
bolita = Bolita(ANCHO, ALTO)
jugador = Paleta(ANCHO, ALTO)
muro = Muro(50, ANCHO, ALTO)

while True:
    #Establecer FPS.
    reloj.tick(60)
    #Revisar los eventos.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        #Buscar eventos de teclado.
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)


    #Actualizar posición de la bolita.
    bolita.update()

    #Colisión entre bolita y jugador.
    if pygame.sprite.collide_rect(bolita, jugador):
        bolita.speed[1] = -bolita.speed[1]
    #Colisión de la bolita con el muro.
    lista = pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
    #Rellernar la pantalla.
    pantalla.fill(color_azul)
    #Dibujar bolita en la pantalla.
    pantalla.blit(bolita.imagen, bolita.rect)
    #Dibujar jugador
    pantalla.blit(jugador.imagen, jugador.rect)
    #Dibujar los ladrillos.
    muro.draw(pantalla)
    #Actualizar los elementos de la pantalla
    pygame.display.flip()

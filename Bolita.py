#Clase que creará la bola del juego.
import pygame.sprite

class Bolita(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        self.alto = alto
        self.ancho = ancho
        pygame.sprite.Sprite.__init__(self)
        #Cargar la imagen.
        self.imagen = pygame.image.load("./Imgs/bolita.png")
        #Obtener área de la imagen.
        self.rect = self.imagen.get_rect()
        #Posición inicial centrada en la pantalla.
        self.rect.centerx = ancho / 2
        self.rect.centery = alto / 2
        #Establecer velocidad inicial.
        self.speed = [3, 3]

    def update(self):
        #Evitar que salga por debajo.
        if self.rect.bottom >= self.alto or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= self.ancho or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)

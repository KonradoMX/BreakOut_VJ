import pygame.sprite
class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        #Cargar la imagen.
        self.image = pygame.image.load("./Imgs/ladrillo.png")
        #Obtener área de la imagen.
        self.rect = self.image.get_rect()
        #Posición inicial, provista externamente.
        self.rect.topleft = posicion
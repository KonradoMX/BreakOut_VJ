import pygame.sprite
from Ladrillo import Ladrillo

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos, ancho, alto):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)

            pos_x += ladrillo.rect.width
            if pos_x >= ancho:
                pos_x = 0
                pos_y += ladrillo.rect.height

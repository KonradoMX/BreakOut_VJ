import pygame.sprite
class Paleta(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        self.alto = alto
        self.ancho = ancho
        pygame.sprite.Sprite.__init__(self)
        #Cargar la imagen.
        self.imagen = pygame.image.load("./Imgs/paleta.png")
        #Obtener área de la imagen.
        self.rect = self.imagen.get_rect()
        #Posición inicial centrada en la pantalla.
        self.rect.midbottom = (self.ancho / 2, self.alto - 20)
        #Establecer velocidad inicial.
        self.speed = [0, 0]

    def update(self, evento):
        #Si se presiona felcha izquierda
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        #Si se presiona flecha derecha.
        elif evento.key == pygame.K_RIGHT and self.rect.right < self.ancho:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        #Moven en base a posición actual y velocidad.
        self.rect.move_ip(self.speed)
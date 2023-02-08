import pygame


class Pacman(pygame.sprite.Sprite):
    """Esta clase representa la barra inferior que controla el protagonista."""

    # Constructor function
    def __init__(self, x, y, sprite_path):
        #  Llama al constructor padre
        super().__init__()

        # Establecemos el alto y largo
        # self.image = pygame.Surface([15, 15])
        # self.image.fill(BLANCO)

        self.sprite_path = sprite_path

        self.image = pygame.image.load(self.sprite_path).convert_alpha()
        self.image = self.image.subsurface((853, 54, 35, 34))

        # Look
        self.look = True

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Establecemos el vector velocidad
        self.cambio_x = 0
        self.cambio_y = 0
        self.paredes = None

    def change_look(self):

        if self.cambio_x != 0 or self.cambio_y != 0:

            # self.image = self.image.subsurface((853,5,35,34))
            self.image = pygame.image.load(self.sprite_path).convert_alpha()
            # Right
            if self.cambio_x > 0 and self.cambio_y == 0:
                self.image = self.image.subsurface((853, 54, 35, 34))
            # Left
            elif self.cambio_x < 0 and self.cambio_y == 0:
                self.image = self.image.subsurface((853, 354, 35, 34))
            # Up
            elif self.cambio_x == 0 and self.cambio_y > 0:
                self.image = self.image.subsurface((853, 204, 35, 34))
            # Down
            elif self.cambio_x == 0 and self.cambio_y < 0:
                self.image = self.image.subsurface((853, 507, 35, 34))
            # Diagonal
            else:
                self.image = self.image.subsurface((853, 5, 35, 34))

    def cambiovelocidad(self, x, y):
        """Cambia la velocidad del protagonista."""
        self.cambio_x += x
        self.cambio_y += y

        self.change_look()

    def reset(self):
        self.rect.y = 554
        self.rect.x = 382

    def update(self):
        """Cambia la velocidad del protagonista."""
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x

        # Hemos chocado contra la pared después de esta actualización?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            else:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right

        # Desplazar arriba/izquierda
        self.rect.y += self.cambio_y

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:

            # Reseteamos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
            else:
                self.rect.top = bloque.rect.bottom

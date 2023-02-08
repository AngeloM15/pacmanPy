import pygame


class Wall(pygame.sprite.Sprite):
    """Pared con la que el protagonista puede encontrarse."""

    def __init__(self, x, y, largo, alto, color):
        """Constructor para la pared con la que el protagonista puede encontrarse"""
        #  Llama al constructor padre
        super().__init__()

        # Construye una pared azul con las dimensiones especificadas por los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Coin(pygame.sprite.Sprite):
    """Pared con la que el protagonista puede encontrarse."""

    def __init__(self, x, y, sprite_path):
        """Constructor para la pared con la que el protagonista puede encontrarse"""
        #  Llama al constructor padre
        super().__init__()

        # Construye una pared azul con las dimensiones especificadas por los parámetros
        # self.image = pygame.Surface([largo, alto])
        # self.image.fill(ROJO)

        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = self.image.subsurface((410, 312, 18, 18))

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.wall = None
        self.delete = False

    def check_position(self):
        superposition = pygame.sprite.spritecollide(self, self.wall, False)
        for i in superposition:
            self.delete = True


class Ghost(pygame.sprite.Sprite):
    def __init__(self, select, sprite_path):

        # Llama a la clase constructor padre (Sprite)
        super().__init__()

        self.image = pygame.image.load(sprite_path).convert_alpha()

        if select == 0:
            self.image = self.image.subsurface((649, 103, 38, 37))
        if select == 1:
            self.image = self.image.subsurface((700, 103, 37, 37))
        if select == 2:
            self.image = self.image.subsurface((750, 103, 38, 37))
        if select == 3:
            self.image = self.image.subsurface((150, 103, 36, 36))
        # Extraemos el objeto rectángulo que posee las dimensiones
        # de la imagen.
        # Estableciendo los valores para rect.x and rect.y actualizamos
        # la posición de este objeto.
        self.rect = self.image.get_rect()

        # Variables de instancia que controlan los bordes
        # donde rebotamos
        self.limite_izquierdo = 0
        self.limite_derecho = 0
        self.limite_superior = 0
        self.limite_inferior = 0

        # Variables de instancia que controlan nuestras
        # velocidades y dirección actuales
        self.cambio_x = 0
        self.cambio_y = 0

        self.paredes = None

    # Llamada para cada fotograma.
    def update(self):
        # ------------------------------------------------------------------#
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
            self.cambio_x *= -1

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
            self.cambio_y *= -1


class Stats(pygame.sprite.Sprite):
    def __init__(self, text, lives, points, actual_level, sprites_path):
        super().__init__()

        self.lives = lives
        self.points = points
        self.actual_level = actual_level
        self.text = text
        self.sprites_path = sprites_path

        # self.words()

        if isinstance(self.text, str):
            self.words()
        elif isinstance(self.text, int):
            self.numbers(self.text, "Level")

    def words(self):

        # Level
        if self.text == "Level":
            self.image = pygame.image.load(self.sprites_path).convert_alpha()
            self.image = self.image.subsurface((47, 103, 102, 26))
            self.rect = self.image.get_rect()
            self.rect.y = 100
            self.rect.x = 849

        # Points
        if self.text == "Points":
            self.image = pygame.image.load(self.sprites_path).convert_alpha()
            self.image = self.image.subsurface((47, 141, 120, 26))
            self.rect = self.image.get_rect()
            self.rect.y = 250
            self.rect.x = 840

        # Lives
        if self.text == "Lives":
            self.image = pygame.image.load(self.sprites_path).convert_alpha()
            self.image = self.image.subsurface((47, 179, 93, 25))
            self.rect = self.image.get_rect()
            self.rect.y = 400
            self.rect.x = 853

    def numbers(self, number, space):

        # Number 1
        if number == 1:
            self.image = pygame.image.load(self.sprites_path).convert_alpha()
            self.image = self.image.subsurface((13, 7, 22, 36))
            self.rect = self.image.get_rect()
        # Number 2
        elif number == 2:
            self.image = pygame.image.load(self.sprites_path).convert_alpha()
            self.image = self.image.subsurface((41, 7, 32, 36))
            self.rect = self.image.get_rect()
        # Number 3
        elif number == 3:
            self.image = pygame.image.load(self.sprites_path).convert_alpha()
            self.image = self.image.subsurface((79, 7, 32, 36))
            self.rect = self.image.get_rect()

        if space == "Level":
            self.rect.y = 150
            self.rect.x = 889

        elif space == "Points":
            self.rect.y = 300
            self.rect.x = 889

        elif space == "Lives":
            self.rect.y = 450
            self.rect.x = 889

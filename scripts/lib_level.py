import random

import character as ch
import lib_config
import objects as obj
import pygame


class Level(lib_config.Config):
    def __init__(self, actual_level):
        super().__init__()

        # Lista que almacena todos los sprites
        self.all_sprites = pygame.sprite.Group()

        # Construimos las paredes. (x_pos, y_pos, largo, alto)
        self.pared_list = pygame.sprite.Group()

        # Ghost list
        self.ghost_list = pygame.sprite.Group()

        # Coin list
        self.coin_list = pygame.sprite.Group()

        self.actual_level = actual_level

        self.set_stage()
        self.set_ghosts()
        self.set_stats()

    def set_stage(self):

        if self.actual_level == 1:
            color = self.blue

            # Block UR
            self.block = obj.Wall(600, 100, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR
            self.block = obj.Wall(680, 100, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = obj.Wall(100, 100, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = obj.Wall(120, 100, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = obj.Wall(600, 480, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = obj.Wall(680, 400, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL
            self.block = obj.Wall(100, 400, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL
            self.block = obj.Wall(120, 480, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = obj.Wall(380, 240, 40, 120, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = obj.Wall(340, 280, 120, 40, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

        elif self.actual_level == 2:
            color = self.green

            # Block UR
            self.block = obj.Wall(600, 100, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR
            self.block = obj.Wall(680, 100, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR_2
            self.block = obj.Wall(540, 160, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR_2
            self.block = obj.Wall(560, 240, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = obj.Wall(100, 100, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = obj.Wall(120, 100, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL_2
            self.block = obj.Wall(160, 240, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL_2
            self.block = obj.Wall(240, 160, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = obj.Wall(600, 480, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = obj.Wall(680, 400, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR_2
            self.block = obj.Wall(540, 360, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR_2
            self.block = obj.Wall(560, 360, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL
            self.block = obj.Wall(100, 400, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL
            self.block = obj.Wall(120, 480, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL_2
            self.block = obj.Wall(160, 360, 80, 20, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL_2
            self.block = obj.Wall(240, 360, 20, 100, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = obj.Wall(380, 240, 40, 120, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = obj.Wall(340, 280, 120, 40, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

        elif self.actual_level == 3:
            color = self.red
            # Block DL
            self.block = obj.Wall(100, 400, 80, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(125, 425, 30, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(125, 375, 30, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = obj.Wall(635, 400, 80, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(660, 425, 30, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(660, 375, 30, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DM
            self.block = obj.Wall(325, 350, 150, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block F
            self.block = obj.Wall(150, 100, 85, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(150, 125, 25, 125, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(175, 175, 25, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block I
            self.block = obj.Wall(320, 100, 25, 150, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block E1
            self.block = obj.Wall(440, 100, 25, 150, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(475, 100, 40, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(475, 225, 40, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(475, 163, 20, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block E2
            self.block = obj.Wall(595, 100, 25, 150, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(630, 100, 40, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(630, 225, 40, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = obj.Wall(630, 163, 20, 25, color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

        # Left wall
        self.pared = obj.Wall(0, 0, 10, 600, color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Right wall
        self.pared = obj.Wall(790, 0, 10, 600, color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Up wall
        self.pared = obj.Wall(10, 0, 790, 10, color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Down wall
        self.pared = obj.Wall(10, 590, 790, 10, color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Wall pacman
        self.pared = obj.Wall(340, 534, 120, 20, color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Coin
        for x in range(0, 800, 50):
            for y in range(0, 600, 50):

                self.coin = obj.Coin(x, y, self.group_1)
                self.coin.wall = self.pared_list
                self.coin.check_position()

                if self.coin.delete == True:
                    del self.coin
                else:
                    self.coin_list.add(self.coin)
                    self.all_sprites.add(self.coin)

    # Set ghosts depending of the dificulty
    def set_ghosts(self):

        if self.actual_level == 1:
            limits = 2
            ghost_quantity = 2
        elif self.actual_level == 2:
            limits = 4
            ghost_quantity = 3
        elif self.actual_level == 3:
            limits = 6
            ghost_quantity = 4

        for i in range(ghost_quantity):
            self.ghost = obj.Ghost(i, self.group_1)
            self.ghost.paredes = self.pared_list

            # Establece una ubicación aleatoria para el bloque
            # ghost.rect.x = random.randrange(10,LARGO_PANTALLA-10)
            # ghost.rect.y = random.randrange(10,ALTO_PANTALLA-10)

            self.ghost.rect.x = 400
            self.ghost.rect.y = 100

            self.ghost.cambio_x = random.randrange(-1 * limits, limits)
            while self.ghost.cambio_x == 0:
                self.ghost.cambio_x = random.randrange(-1 * limits, limits)

            self.ghost.cambio_y = random.randrange(-1 * limits, limits)
            while self.ghost.cambio_y == 0:
                self.ghost.cambio_y = random.randrange(-1 * limits, limits)

            self.ghost.limite_izquierdo = 10
            self.ghost.limite_superior = 10
            self.ghost.limite_derecho = 790
            self.ghost.limite_inferior = 590

            # Añade el bloque a la lista de objetos
            self.ghost_list.add(self.ghost)
            self.all_sprites.add(self.ghost)

        # --------------Stats-----------------#

    def set_stats(self):

        self.word1 = obj.Stats("Level", 0, 0, 0, self.group_2)
        self.all_sprites.add(self.word1)

        # self.word2 = Stats("Points",0,0,0)
        # self.all_sprites.add(self.word2)

        # self.word3 = Stats("Lives",0,0,0)
        # self.all_sprites.add(self.word3)

        # Stats
        self.stats = obj.Stats(
            self.actual_level, self.lives, 0, self.actual_level, self.group_2
        )
        self.all_sprites.add(self.stats)

        # ------------------------------------#

        # objeto pacman
        self.protagonista = ch.Pacman(382, 554, self.group_1)
        self.protagonista.paredes = self.pared_list

        self.all_sprites.add(self.protagonista)

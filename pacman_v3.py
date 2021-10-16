from typing import Text
import pygame
import random

"""
Global constants
"""
 
# Colores
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
BLUE = (20, 8, 137)
RED = (154,5,12)
GREEN = (8,137,44)

# Dimensiones de la pantalla
LARGO_PANTALLA  = 1000
ALTO_PANTALLA = 600

#----sprites------#
GAME_SPRITES = "E:/Apuntes/FIEE 2021-2/algoritmos/Scripts/Game/pacman.png"

STATS_SPRITES = "E:/Apuntes/FIEE 2021-2/algoritmos/Scripts/Game/stats.png"
#----------------#

class Pacman(pygame.sprite.Sprite):
    """ Esta clase representa la barra inferior que controla el protagonista. """
 
    # Función Constructor 
    def __init__(self, x, y):
        #  Llama al constructor padre
        super().__init__()
  
        # Establecemos el alto y largo
        # self.image = pygame.Surface([15, 15])
        # self.image.fill(BLANCO)
     
        self.image = pygame.image.load(GAME_SPRITES).convert_alpha()
        self.image = self.image.subsurface((853,54,35,34))

        #Look
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
            self.image = pygame.image.load(GAME_SPRITES).convert_alpha()
            # Right
            if self.cambio_x > 0 and self.cambio_y == 0:
                self.image = self.image.subsurface((853,54,35,34))
            # Left
            elif self.cambio_x < 0 and self.cambio_y == 0:
                self.image = self.image.subsurface((853,354,35,34))
            # Up
            elif self.cambio_x == 0 and self.cambio_y > 0:
                self.image = self.image.subsurface((853,204,35,34))    
            # Down
            elif self.cambio_x == 0 and self.cambio_y < 0:
                self.image = self.image.subsurface((853,507,35,34))
            # Diagonal
            else:
                self.image = self.image.subsurface((853,5,35,34))
            
    def cambiovelocidad(self, x, y):
        """ Cambia la velocidad del protagonista. """
        self.cambio_x += x
        self.cambio_y += y
        
        self.change_look()
    
    def reset(self):
        self.rect.y = 554
        self.rect.x = 382

    def update(self):
        """ Cambia la velocidad del protagonista. """
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
         
        # Hemos chocado contra la pared después de esta actualización?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:
            #Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
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
  

class Pared(pygame.sprite.Sprite):
    """ Pared con la que el protagonista puede encontrarse. """
    def __init__(self, x, y, largo, alto,color):
        """ Constructor para la pared con la que el protagonista puede encontrarse """
        #  Llama al constructor padre
        super().__init__()
 
        # Construye una pared azul con las dimensiones especificadas por los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
 
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Ghost(pygame.sprite.Sprite):  
    """
    Esta clase representa la pelota.        
    Deriva de la clase "Sprite" en Pygame
    """
     
    def __init__(self, select):
        """Constructor. Le pasa el color al bloque,
        así como la posición de x,y """
        # Llama a la clase constructor padre (Sprite)
        super().__init__()
 
        # Crea una imagen del bloque y lo rellena de color.
        # También podríamos usar una imagen guardada en disco.
        # self.image = pygame.Surface([width, height])
        # self.image.fill(color)

        self.image = pygame.image.load(GAME_SPRITES).convert_alpha()
        
        if select == 0:
            self.image = self.image.subsurface((649,103,38,37))
        if select == 1:
            self.image = self.image.subsurface((700,103,37,37))
        if select == 2:
            self.image = self.image.subsurface((750,103,38,37))
        if select == 3:
            self.image = self.image.subsurface((150,103,36,36))
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
        #------------------------------------------------------------------#
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
         
        # Hemos chocado contra la pared después de esta actualización?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:
            #Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
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


class Coin(pygame.sprite.Sprite):
    """ Pared con la que el protagonista puede encontrarse. """
    def __init__(self, x, y):
        """ Constructor para la pared con la que el protagonista puede encontrarse """
        #  Llama al constructor padre
        super().__init__()
 
        # Construye una pared azul con las dimensiones especificadas por los parámetros
        # self.image = pygame.Surface([largo, alto])
        # self.image.fill(ROJO)
 
        self.image = pygame.image.load(GAME_SPRITES).convert_alpha()
        self.image = self.image.subsurface((410,312,18,18))

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


class Level():
    def __init__(self,actual_level):
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
        
    

    def set_stage(self):

        if self.actual_level == 1:
            color = BLUE
            
            # Block UR
            self.block = Pared(600,100,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR
            self.block = Pared(680,100,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = Pared(100,100,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = Pared(120,100,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = Pared(600,480,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = Pared(680,400,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)
            
            # Block DL
            self.block = Pared(100,400,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL
            self.block = Pared(120,480,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = Pared(380,240,40,120,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = Pared(340,280,120,40,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)
            
        elif self.actual_level == 2:
            color = GREEN

            # Block UR
            self.block = Pared(600,100,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR
            self.block = Pared(680,100,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR_2
            self.block = Pared(540,160,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UR_2
            self.block = Pared(560,240,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = Pared(100,100,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL
            self.block = Pared(120,100,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL_2
            self.block = Pared(160,240,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block UL_2
            self.block = Pared(240,160,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = Pared(600,480,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR
            self.block = Pared(680,400,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR_2
            self.block = Pared(540,360,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DR_2
            self.block = Pared(560,360,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)
            
            # Block DL
            self.block = Pared(100,400,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL
            self.block = Pared(120,480,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL_2
            self.block = Pared(160,360,80,20,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DL_2
            self.block = Pared(240,360,20,100,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = Pared(380,240,40,120,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block C
            self.block = Pared(340,280,120,40,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

        elif self.actual_level == 3:
            color = RED
            # Block DL
            self.block = Pared(100,400,80,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)
  
            self.block = Pared(125,425,30,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(125,375,30,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)
            
            # Block DR
            self.block = Pared(635,400,80,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(660,425,30,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(660,375,30,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block DM
            self.block = Pared(325,350,150,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)
            
            # Block F
            self.block = Pared(150,100,85,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(150,125,25,125,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(175,175,25,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block I
            self.block = Pared(320,100,25,150,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block E1
            self.block = Pared(440,100,25,150,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(475,100,40,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(475,225,40,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(475,163,20,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            # Block E2
            self.block = Pared(595,100,25,150,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(630,100,40,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(630,225,40,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)

            self.block = Pared(630,163,20,25,color)
            self.pared_list.add(self.block)
            self.all_sprites.add(self.block)


        # Left wall
        self.pared = Pared(0,0,10,600,color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Right wall
        self.pared = Pared(790,0,10,600,color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Up wall
        self.pared = Pared(10,0,790,10,color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Down wall
        self.pared = Pared(10,590,790,10,color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Wall pacman
        self.pared = Pared(340,534,120,20,color)
        self.pared_list.add(self.pared)
        self.all_sprites.add(self.pared)

        # Coin
        for x in range(0,800,50):
            for y in range(0,600,50):

                self.coin = Coin(x,y)
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
            self.ghost = Ghost(i)
            self.ghost.paredes = self.pared_list

            # Establece una ubicación aleatoria para el bloque
            # ghost.rect.x = random.randrange(10,LARGO_PANTALLA-10)
            # ghost.rect.y = random.randrange(10,ALTO_PANTALLA-10)
            
            self.ghost.rect.x = 400
            self.ghost.rect.y = 100
                
            self.ghost.cambio_x = random.randrange(-1*limits,limits)
            while self.ghost.cambio_x == 0:
                self.ghost.cambio_x = random.randrange(-1*limits,limits)
                  
            self.ghost.cambio_y = random.randrange(-1*limits,limits)
            while self.ghost.cambio_y == 0:
                self.ghost.cambio_y = random.randrange(-1*limits,limits)

            self.ghost.limite_izquierdo = 10
            self.ghost.limite_superior = 10
            self.ghost.limite_derecho = 790
            self.ghost.limite_inferior = 590

            #Añade el bloque a la lista de objetos
            self.ghost_list.add(self.ghost)
            self.all_sprites.add(self.ghost)

        #--------------Stats-----------------#
        
        self.word1 = Stats("Level",0,0,0)
        self.all_sprites.add(self.word1)

        self.word2 = Stats("Points",0,0,0)
        self.all_sprites.add(self.word2)
        
        self.word3 = Stats("Lives",0,0,0)
        self.all_sprites.add(self.word3)

        # Stats
        self.stats = Stats(self.actual_level,3,0,self.actual_level)
        self.all_sprites.add(self.stats)
             
        #------------------------------------#
        
        # objeto pacman
        self.protagonista = Pacman(382, 554)
        self.protagonista.paredes = self.pared_list
            
        self.all_sprites.add(self.protagonista)


class Stats(pygame.sprite.Sprite):

    def __init__(self,text,lives,points, actual_level):
        super().__init__()

        self.lives = lives
        self.points = points
        self.actual_level = actual_level
        self.text = text

        # self.words()
        
        if isinstance(self.text, str):
            self.words()
        elif isinstance(self.text, int):
            self.numbers(self.text,"Level")

    def words(self):

        # Level
        if self.text == "Level":
            self.image = pygame.image.load(STATS_SPRITES).convert_alpha()
            self.image = self.image.subsurface((47,103,102,26))
            self.rect = self.image.get_rect()
            self.rect.y = 100
            self.rect.x = 849
    
        # Points
        if self.text == "Points":
            self.image = pygame.image.load(STATS_SPRITES).convert_alpha()
            self.image = self.image.subsurface((47,141,120,26))
            self.rect = self.image.get_rect()
            self.rect.y = 250
            self.rect.x = 840

        # Lives
        if self.text == "Lives":
            self.image = pygame.image.load(STATS_SPRITES).convert_alpha()
            self.image = self.image.subsurface((47,179,93,25))
            self.rect = self.image.get_rect()
            self.rect.y = 400
            self.rect.x = 853

    def numbers(self,number,space):
        
        # Number 1        
        if number == 1:
            self.image = pygame.image.load(STATS_SPRITES).convert_alpha()
            self.image = self.image.subsurface((13,7,22,36))
            self.rect = self.image.get_rect()
        # Number 2
        elif number == 2:
            self.image = pygame.image.load(STATS_SPRITES).convert_alpha()
            self.image = self.image.subsurface((41,7,32,36))
            self.rect = self.image.get_rect()
        # Number 3
        elif number == 3:
            self.image = pygame.image.load(STATS_SPRITES).convert_alpha()
            self.image = self.image.subsurface((79,7,32,36))
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

#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

# Llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
pygame.init()
 
# Creamos una pantalla de 800x600
screen = pygame.display.set_mode([LARGO_PANTALLA, ALTO_PANTALLA])
 
# Creamos el título de la ventana
pygame.display.set_caption('Pacman')
 
# Create level
level = Level(1)

reloj = pygame.time.Clock() 


pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1, 0.0)

hecho = False

while not hecho:
     
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
 
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                level.protagonista.cambiovelocidad(-3,0)
            elif evento.key == pygame.K_RIGHT:
                level.protagonista.cambiovelocidad(3,0)
            elif evento.key == pygame.K_UP:
                level.protagonista.cambiovelocidad(0,-3)
            elif evento.key == pygame.K_DOWN:
                level.protagonista.cambiovelocidad(0,3)
                 
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                level.protagonista.cambiovelocidad(3,0)
            elif evento.key == pygame.K_RIGHT:
                level.protagonista.cambiovelocidad(-3,0)
            elif evento.key == pygame.K_UP:
                level.protagonista.cambiovelocidad(0,3)
            elif evento.key == pygame.K_DOWN:
                level.protagonista.cambiovelocidad(0,-3)
  
    level.all_sprites.update()
     
    screen.fill(BLACK)
    
    # Desaparece fantasma
    ghost_hit_list = pygame.sprite.spritecollide(level.protagonista, level.ghost_list, False)
    
    # Lose lives
    for ghost in ghost_hit_list:
        level.stats.lives -= 1
        print("lives: " + str(level.stats.lives))
        level.protagonista.reset()

    # Game over
    if level.stats.lives == 0:

        del level
        level = Level(1)
        
        # level.stats.lives = 3
        print("lives: " + str(level.stats.lives))
        # level.stats.points = 0
        # level.stats.actual_level = 1
        print("level: " + str(level.stats.actual_level))

        pygame.event.clear()
    
    # Desaparece moneda
    get_coin_list = pygame.sprite.spritecollide(level.protagonista, level.coin_list, True)

    for coin in get_coin_list:
        level.stats.points += 1
        print("points: "+str(level.stats.points))

        if len(level.coin_list) == 0:
            # New level
            level.stats.actual_level +=1
            temp_lives = level.stats.lives +1
            temp_points = level.stats.points

            if level.stats.actual_level == 4:
                temp_level = 1
            else:    
                temp_level = level.stats.actual_level
            
            print("level: " + str(temp_level))
            
            del level
            level = Level(temp_level)
            level.stats.lives = temp_lives
            level.stats.points = temp_points

            print("lives: " + str(level.stats.lives))
            pygame.event.clear()


    level.all_sprites.draw(screen)

    pygame.display.flip()
 
    reloj.tick(60)

pygame.mixer.music.stop()
pygame.quit()
import lib_config
import lib_level
import pygame


def main():

    # Load configuration

    config = lib_config.Config()

    # Llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
    pygame.init()

    # Creamos una pantalla de 1000x600
    screen = pygame.display.set_mode([config.screen_length, config.screen_height])

    # Creamos el título de la ventana
    pygame.display.set_caption("Pacman")

    # Create level
    level = lib_level.Level(1)

    reloj = pygame.time.Clock()

    # Add music
    pygame.mixer.music.load("assets/music/background.mp3")
    pygame.mixer.music.play(-1, 0.0)

    done = False

    while not done:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                done = True

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    level.protagonista.cambiovelocidad(-3, 0)
                elif evento.key == pygame.K_RIGHT:
                    level.protagonista.cambiovelocidad(3, 0)
                elif evento.key == pygame.K_UP:
                    level.protagonista.cambiovelocidad(0, -3)
                elif evento.key == pygame.K_DOWN:
                    level.protagonista.cambiovelocidad(0, 3)

            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    level.protagonista.cambiovelocidad(3, 0)
                elif evento.key == pygame.K_RIGHT:
                    level.protagonista.cambiovelocidad(-3, 0)
                elif evento.key == pygame.K_UP:
                    level.protagonista.cambiovelocidad(0, 3)
                elif evento.key == pygame.K_DOWN:
                    level.protagonista.cambiovelocidad(0, -3)

        level.all_sprites.update()

        screen.fill(config.black)

        # Desaparece fantasma
        ghost_hit_list = pygame.sprite.spritecollide(
            level.protagonista, level.ghost_list, False
        )

        # Lose lives
        for ghost in ghost_hit_list:
            level.stats.lives -= 1
            print("lives: " + str(level.stats.lives))
            level.protagonista.reset()

        # Game over
        if level.stats.lives == 0:

            del level
            level = lib_level.Level(1)

            # level.stats.lives = 3
            print("lives: " + str(level.stats.lives))
            # level.stats.points = 0
            # level.stats.actual_level = 1
            print("level: " + str(level.stats.actual_level))

            pygame.event.clear()

        # Desaparece moneda
        get_coin_list = pygame.sprite.spritecollide(
            level.protagonista, level.coin_list, True
        )

        for coin in get_coin_list:
            level.stats.points += 1
            print("points: " + str(level.stats.points))

            if len(level.coin_list) == 0:
                # New level
                level.stats.actual_level += 1
                temp_lives = level.stats.lives + 1
                temp_points = level.stats.points

                if level.stats.actual_level == 4:
                    temp_level = 1
                else:
                    temp_level = level.stats.actual_level

                print("level: " + str(temp_level))

                del level
                level = lib_level.Level(temp_level)
                level.stats.lives = temp_lives
                level.stats.points = temp_points

                print("lives: " + str(level.stats.lives))
                pygame.event.clear()

        level.all_sprites.draw(screen)

        pygame.display.flip()

        reloj.tick(60)

    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    main()

import pygame
import settings
import func


pygame.init()
dt = 0
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
player = func.Player(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()
collide = None




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    food_pos, f_size = func.food(screen, collide)
    p_size = player.draw_p(screen)

    player.x_pos, player.y_pos = player.player_mvt()


    collide = func.collision(player.x_pos, player.y_pos, food_pos, p_size[0], f_size, reduction=10)

    pygame.display.flip()
    player.dt = clock.tick(settings.REFRESH_RATE) / 1000


pygame.quit()

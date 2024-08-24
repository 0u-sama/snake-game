import pygame
import settings
from func import Player


pygame.init()
dt = 0
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
player = Player(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")

    "pygame.draw.circle(screen, 'Black', player_pos, 20)"
    player.draw_p(screen)

    player.x_pos, player.y_pos = player.player_mvt()

    pygame.display.flip()
    player.dt = clock.tick(settings.REFRESH_RATE) / 1000


pygame.quit()

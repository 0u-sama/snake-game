import pygame
import settings
import func


pygame.init()
dt = 0
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
player = func.Player(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")

    player.draw_p(screen)

    player.x_pos, player.y_pos = player.player_mvt()
    func.food(screen)


    pygame.display.flip()
    player.dt = clock.tick(settings.REFRESH_RATE) / 1000


pygame.quit()

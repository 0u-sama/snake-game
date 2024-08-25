import math
import pygame


class Player:
    eye_offset_x = -5
    eye_offset_y = -2.5
    def __init__(self, x_pos, y_pos, tail = 1, delta_time = 60):
        self.dt = delta_time
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tail : int = tail
        self.last_x_in = None
        self.last_y_in = None
        self.x_speed = 0
        self.y_speed = 0
        self.angle = 0



    def player_mvt(self):


        keys = pygame.key.get_pressed()
        if (keys[pygame.K_z] or keys[pygame.K_UP]) and not self.last_y_in == 'down':
            self.y_speed = -100 * self.dt
            self.x_speed = 0
            self.last_y_in = 'up'
            self.last_x_in = None
            self.angle = 90
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and not self.last_y_in == 'up':
            self.y_speed = 100 * self.dt
            self.x_speed = 0
            self.last_y_in = 'down'
            self.last_x_in = None
            self.angle = -90

        if (keys[pygame.K_q] or keys[pygame.K_LEFT]) and not self.last_x_in == 'right':
            self.x_speed = -100 * self.dt
            self.y_speed = 0
            self.last_x_in = 'left'
            self.last_y_in = None
            self.angle = 0
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not self.last_x_in == 'left':
            self.x_speed = 100 * self.dt
            self.y_speed = 0
            self.last_x_in = 'right'
            self.last_y_in = None
            self.angle = 180

        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

        if self.x_pos <= 0:
            self.x_pos = 799
        elif self.x_pos >= 800:
            self.x_pos = 1
        if self.y_pos <= 0:
            self.y_pos = 599
        elif self.y_pos >= 600:
            self.y_pos = 1

        return self.x_pos, self.y_pos


    def draw_p(self, screen):
        global eye_offset_x, eye_offset_y
        snake = pygame.Surface((20, 10))
        snake.fill('Yellow')
        rotated_snake = pygame.transform.rotate(snake, self.angle)


        rect = rotated_snake.get_rect(center=(self.x_pos, self.y_pos))

        screen.blit(rotated_snake, rect)

        if self.angle == 180:
            eye_offset_x = -5
            eye_offset_y = 2.5
        elif self.angle == 0:
            eye_offset_x = -5
            eye_offset_y = 2.5
        elif self.angle == -90:
            eye_offset_x = -2.5
            eye_offset_y = 5
        elif self.angle == 90:
            eye_offset_x = -2.5
            eye_offset_y = 5


        eye_pos = self.rotate_point((self.x_pos, self.y_pos), (self.x_pos + eye_offset_x, self.y_pos + eye_offset_y), self.angle)
        pygame.draw.circle(screen, 'White', eye_pos, 5)




    def rotate_point(self, center, point, angle):
        ang_rad = math.radians(angle)
        temp_x = point[0] - center[0]
        temp_y = point[1] - center[1]

        rotated_x = temp_x * math.cos(ang_rad) - temp_y * math.sin(ang_rad)
        rotated_y = temp_y * math.cos(ang_rad) + temp_x * math.sin(ang_rad)

        return (center[0] + rotated_x, center[1] + rotated_y)





"""last_x_in = None
last_y_in = None
x_speed = 0
y_speed = 0



def player_mvt(x, y, delta_time=60):
    global last_y_in, last_x_in, x_speed, y_speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] or keys[pygame.K_UP]:
        y_speed = 60 * delta_time
        last_y_in = 'up'
        last_x_in = None
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y_speed = 60 * delta_time
        last_y_in = 'down'
        last_x_in = None

    elif keys[pygame.K_q] or keys[pygame.K_LEFT]:
        x_speed = 60 * delta_time
        last_x_in = 'left'
        last_y_in = None
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x_speed = 60 * delta_time
        last_x_in = 'right'
        last_y_in = None

    if last_x_in == 'left':
        x -= x_speed
        y_speed = 0
    elif last_x_in == 'right':
        x += x_speed
        y_speed = 0

    if last_y_in == 'up':
        y -= y_speed
        x_speed = 0
    elif last_y_in == 'down':
        y += y_speed
        x_speed = 0

    if x <= 0: x = 799
    elif x >= 800: x = 1
    if y <= 0: y = 599
    elif y >= 600: y = 1

    return x, y


def food(x, y):
    pass



"""


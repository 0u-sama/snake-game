import math, pygame, settings
from random import randint


food_position = (0, 0)
spawned_food = False


class Player:

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
        self.eye_offset_x = -5
        self.eye_offset_y = -2.5



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

        snake = pygame.Surface((20, 10))
        snake.fill('Yellow')
        rotated_snake = pygame.transform.rotate(snake, self.angle)


        rect = rotated_snake.get_rect(center=(self.x_pos, self.y_pos))

        screen.blit(rotated_snake, rect)

        if self.angle == 180:
            self.eye_offset_x = -5
            self.eye_offset_y = 2.5
        elif self.angle == 0:
            self.eye_offset_x = -5
            self.eye_offset_y = -2.5
        elif self.angle == -90:
            self.eye_offset_x = -2.5
            self.eye_offset_y = 5
        elif self.angle == 90:
            self.eye_offset_x = -2.5
            self.eye_offset_y = 5


        eye_pos = self.rotate_point((self.x_pos, self.y_pos), (self.x_pos + self.eye_offset_x, self.y_pos + self.eye_offset_y), self.angle)
        pygame.draw.circle(screen, 'White', eye_pos, 5)

        return rect.size




    @staticmethod
    def rotate_point(center, point, angle):
        ang_rad = math.radians(angle)
        temp_x = point[0] - center[0]
        temp_y = point[1] - center[1]

        rotated_x = temp_x * math.cos(ang_rad) - temp_y * math.sin(ang_rad)
        rotated_y = temp_y * math.cos(ang_rad) + temp_x * math.sin(ang_rad)

        return center[0] + rotated_x, center[1] + rotated_y


def food(surface, collided:bool=False):
    global food_position, spawned_food


    if collided:
        spawned_food = False
    if not spawned_food:
        fx = randint(1, settings.WIDTH)
        fy = randint(1, settings.HEIGHT)
        food_position = (fx, fy)
        spawned_food = True
    food_size = pygame.draw.circle(surface, 'red', food_position, 5)


    return food_position, food_size.width



def collision(x1, y1, position2, size1, size2, reduction=5) -> bool:
    x2, y2 = position2

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance < (size1 / 2 + size2) - reduction:
        print(f"{x1, y1}")
        return True
    else:
        return False







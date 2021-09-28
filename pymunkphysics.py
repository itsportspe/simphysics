import pygame
import pymunk
import sys


def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 54)
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surf.get_rect(center = (pos_x, pos_y))
        screen.blit(apple_surf, apple_rect)

def static_ball(space, pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (150, 30, 200), (pos_x, pos_y), 50)


pygame.init()  # initiate pygame
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 150)
apple_surface = pygame.image.load('apple_red.png')
apple_surf = pygame.transform.scale(apple_surface, (120, 120))

apples = []


balls = []
balls.append(static_ball(space, (500,500)))
balls.append(static_ball(space, (250,600)))

while True:  # Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                apples.append(create_apple(space, event.pos))
            if event.button == 3:
                balls.append(static_ball(space, event.pos))

    screen.fill((217, 217, 217))  # Background color
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1 / 50)
    pygame.display.update()  # render the frame
    clock.tick(120)  # fps limit

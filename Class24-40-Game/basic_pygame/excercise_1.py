#Draw a circle using pygame and move it around on surface
#https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
#use pygame.draw.circle(surface, color, center, radius)

# https://www.pygame.org/
##Basic Movement and Key Presses
#import pygame
import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Circle Game")

x = 200
y = 200
radius=50
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.circle(win, (128, 0, 128),(x,y),radius)
    pygame.display.update()

pygame.quit()
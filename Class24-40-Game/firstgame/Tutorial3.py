#Character animation & sprites
import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('pics/R1.png'), pygame.image.load('pics/R2.png'), pygame.image.load('pics/R3.png'), pygame.image.load('pics/R4.png'), pygame.image.load('pics/R5.png'), pygame.image.load('pics/R6.png'), pygame.image.load('pics/R7.png'), pygame.image.load('pics/R8.png'), pygame.image.load('pics/R9.png')]
walkLeft = [pygame.image.load('pics/L1.png'), pygame.image.load('pics/L2.png'), pygame.image.load('pics/L3.png'), pygame.image.load('pics/L4.png'), pygame.image.load('pics/L5.png'), pygame.image.load('pics/L6.png'), pygame.image.load('pics/L7.png'), pygame.image.load('pics/L8.png'), pygame.image.load('pics/L9.png')]

bg=pygame.image.load("pics/bg.jpg")
char=pygame.image.load("pics/standing.png")
clock=pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10
left=False
right=False
walkCount=0

def redrawGamewindow():
    global walkCount
    # win.fill((0, 0, 0))
    win.blit(bg,(0,0))
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    if walkCount>=27:
        walkCount=0
    elif left:
        win.blit(walkLeft[walkCount//3],(x,y))
        walkCount+=1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount+=1
    else:
        win.blit(char,(x,y))
    pygame.display.update()

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left=False
        right=True
    else:
        left=False
        right=False
        walkCount=0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    redrawGamewindow()

pygame.quit()

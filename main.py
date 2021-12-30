import pygame,sys,random

def createPipe():
	random_pipe_pos = random.randrange(100,600)
	bottom_pipe = pipe_img.get_rect(midtop = (700,random_pipe_pos))
	top_pipe = pipe_img.get_rect(midbottom = (700,random_pipe_pos - 135))
	return bottom_pipe,top_pipe

def movePipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def drawPipe():
    for pipe in pipe_list:
        if pipe.bottom >= 800:
            screen.blit(pipe_img,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flip_pipe, pipe)

def removePipe():
    for pipe in pipe_list:
        if pipe.centerx <= -300:
            pipe_list.remove(pipe)
    
def checkCollision():
    for pipe in pipe_list:
        if square.colliderect(pipe):
            print("collide")
        
    if square.bottom >= 900 or square.top <= -100:
        print("Collide")

def draw():
    screen.blit(background, (0,0))
    screen.blit(square_img, square)
    drawPipe()
    pygame.display.update()

pygame.init()

SWAPPIPE = pygame.USEREVENT

WIDTH,HEIGHT = 600,800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FULLMETAL SQUARE")

clock = pygame.time.Clock()

background = pygame.image.load("assests/images/background.png")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

square_img = pygame.image.load("assests/images/square128.png")
square = square_img.get_rect(center = (70,400))

pipe_img = pygame.image.load("assests/images/pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (150,700))
pipe_list = []

pygame.time.set_timer(SWAPPIPE, (2100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == SWAPPIPE:
            pipe_list.extend(createPipe())


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square.centery -= 7
    if keys[pygame.K_DOWN]:
        square.centery += 7  

    pipe_list = movePipe(pipe_list)
    removePipe()
    checkCollision()
    draw()
    clock.tick(120)



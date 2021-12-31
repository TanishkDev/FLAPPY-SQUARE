import pygame
import sys
import random


def createPipe():
    random_pipe_pos = random.randrange(100, 600)
    bottom_pipe = pipe_img.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_img.get_rect(midbottom=(700, random_pipe_pos - 135))
    return bottom_pipe, top_pipe


def movePipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 15
    return pipes


def drawPipe():
    for pipe in pipe_list:
        if pipe.bottom >= 800:
            screen.blit(pipe_img, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flip_pipe, pipe)


def removePipe(pipes):
    for pipe in pipes:
        if pipe.centerx <= -50:
            pipes.remove(pipe)
    return pipes


def checkCollision():
    for pipe in pipe_list:
        if square.colliderect(pipe):
            return False
    if square.bottom >= 900 or square.top <= -100:
        return False
    return True


def draw():
    screen.blit(background, (0, 0))
    score_display(1)
    screen.blit(square_img, square)
    drawPipe()


def score_display(gamestate, fontSize=30):
    if gamestate == 1:
        font = pygame.font.SysFont("firamono", fontSize)
        score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
        score_rect = score_surf.get_rect(center=(75, 25))
        screen.blit(score_surf, score_rect)
    if gamestate == 2:
        font = pygame.font.SysFont("firamono", 60)

        over_surf = font.render(f"GAME OVER", True, (255, 0, 0))
        over_rect = over_surf.get_rect(center=(WIDTH/2, HEIGHT/2))

        font = pygame.font.SysFont("firamono", 45)

        highscore = score
        score_surf = font.render(f"Score: {highscore}", True, (0, 0, 0))
        score_rect = score_surf.get_rect(center=(WIDTH/2, HEIGHT/2+40))

        text = font.render(f"Press 'r' to restart", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH/2, 600))

        screen.blit(over_surf, over_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(text, text_rect)


pygame.init()
pygame.font.init()

SWAPPIPE = pygame.USEREVENT
UPDATESCORE = pygame.USEREVENT

WIDTH, HEIGHT = 600, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY SQUARE")

clock = pygame.time.Clock()


game_active = True
score = 0

background = pygame.image.load("assests/images/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


square_img = pygame.image.load("assests/images/square.png")
square_img = pygame.transform.scale(square_img, (80, 80))
square = square_img.get_rect(center=(70, 400))

pipe_img = pygame.image.load("assests/images/pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (150, 700))
pipe_list = []

pygame.time.set_timer(SWAPPIPE, (1500))
pygame.time.set_timer(UPDATESCORE, (2200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SWAPPIPE:
            pipe_list.extend(createPipe())

        if event.type == UPDATESCORE:
            if game_active:
                score += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square.centery -= 8
    if keys[pygame.K_DOWN]:
        square.centery += 8

    if game_active == False:
        if keys[pygame.K_r]:
            square.center = (70, 400)
            pipe_list.clear()
            game_active = True
            score = 0

    if game_active:

        pipe_list = movePipe(pipe_list)
        pipe_list = removePipe(pipe_list)
        game_active = checkCollision()
        draw()

    else:
        screen.blit(background, (0, 0))
        score_display(2)

    pygame.display.flip()
    clock.tick()

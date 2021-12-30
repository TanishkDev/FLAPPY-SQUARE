import pygame
import sys
import random

# Constant Variables
WIDTH, HEIGHT = 600, 800

#Use for swapping pipe
SWAPPIPE = pygame.USEREVENT


class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("FULLMETAL SQUARE")

        # Game Variables
        self.gameON = True
        self.clock = pygame.time.Clock()
        self.gameActive = True

        # background
        self.background = pygame.image.load(
            "assests/images/background.png").convert()
        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT))

        # square
        self.square_img = pygame.image.load("assests/images/square.png")
        self.square_img = pygame.transform.scale(self.square_img, (150, 150))
        self.square = self.square_img.get_rect(center = (60,370))
        
        # Pipe
        self.pipe_img = pygame.image.load("assests/images/pipe.png")
        self.pipe_img = pygame.transform.scale(self.pipe_img, (150, 700))
        self.pipe_list = []

        pygame.time.set_timer(SWAPPIPE, (1200))

    def draw(self):
        self.screen.blit(self.background, (0, 0))#Draw Background
        self.screen.blit(self.square_img, self.square)#Draw square
        self.drawPipe()#Draw Pipe
        pygame.display.flip()

    def drawPipe(self):#draw pipe
        for pipe in self.pipe_list:
            if pipe.bottom >= 800:
                self.screen.blit(self.pipe_img, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_img,False,True)#flip pipe
                self.screen.blit(flip_pipe,pipe) 


    def movePipe(self):
        pipes = self.pipe_list
        for pipe in pipes:
            pipe.centerx -= 5# move pipes
            self.gameActive = self.checkCollison(pipe)
        return pipes

    def createPipe(self):
        pipe_height = random.randint(100,500)
        bottom_pipe = self.pipe_img.get_rect(midtop = (825,500))#down pipe
        top_pipe = self.pipe_img.get_rect(midbottom = (825,500-160))#top pipe
        return bottom_pipe,top_pipe
    
    def removePipe(self):
        for pipe in self.pipe_list:
            if pipe.centerx == -800:
                self.pipe_list.remove(pipe)

        return self.pipe_list   


    def checkCollison(self,pipe):
        # for pipe in self.pipe_list:
        if self.square.colliderect(pipe): #FIXME not working  
            print("damn")      
            return False
        if self.square.top <= -75 or self.square.bottom >= 875:
            return False
        
        return True



    #main game
    def mainGame(self):
        while self.gameON:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameON = False
                    pygame.quit()
                    sys.exit()

                if event.type == SWAPPIPE:#createPipe
                    self.pipe_list.extend(self.createPipe())

            #control movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.square.centery -= 4
            if keys[pygame.K_DOWN]:
                self.square.centery += 4

       
            
            self.pipe_list = self.movePipe()
            self.pipe_list = self.removePipe()

            self.draw()
            # if self.gameActive == False:
            #     print("game over")
        

            self.clock.tick(120)

if __name__ == "__main__":
    game = Game()
    game.mainGame()

#imports pygame & time
from multiprocessing.connection import wait
import pygame,time
pygame.init()

#sets window settings
size = width, height = 1920, 1080

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project SirGreyAlot")
bgrndclr = (0,0,0)

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#images
scale = 5 #size images will be scaled by

bgImg = pygame.image.load('./images/background.png').convert_alpha()
plrSprite = pygame.image.load('./images/CharSpreadSheet.png').convert_alpha()
treeSprite = pygame.image.load('./images/Tree.png').convert_alpha()

def get_image(sheet, frame, x, y):
    image = pygame.Surface((x, y), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * x),0, x, y))
    image = pygame.transform.scale_by(image, (scale, scale))

    return image

#background
def background(image, x, y):
    image = pygame.transform.scale_by(image, (scale, scale))
    image = screen.blit(image, (x ,y))

#elements
class Tree():
    def __init__(self, x, y):
        self.image = pygame.transform.scale_by(tree1Sprite, (scale, scale))
        self.posX = x
        self.posY = y

    def draw(self):
        screen.blit(self.image, (self.posX, self.posY))

#player class
class Player():
    def __init__(self, x, y):
        self.image = get_image(plrSprite, 0 , 30, 30)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)
        self.posX = x
        self.posY = y
        self.speed = 10
        self.flip = False

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def move(self):
        #reset variables
        dx = 0
        dy = 0

        #process keys
        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_w]:
            dy -= player.speed

        if keyPressed[pygame.K_a]:
            dx -= player.speed 
            self.flip = True
        
        if keyPressed[pygame.K_s]:
            dy += player.speed


        if keyPressed[pygame.K_d]:
            dx += player.speed 
            self.flip = False

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def idle(self):
        self.image = get_image(plrSprite, 0 , 30, 30)

    def walk(self):
        self.image = get_image(plrSprite, 1 , 30, 30)


player = Player(0, 0)
tree1 = Tree(250,250)

#game loop
run = True

while run:
    clock.tick(FPS)

    #BACKGROUND
    screen.fill(bgrndclr)
    bg = background(bgImg, 0, 0)

    #DRAW SPRITES
    player.draw()
    tree1.draw()

    #MOVEMENT
    player.move() 

    #for loop through the event queue
    for event in pygame.event.get():        
        #check for QUIT event
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
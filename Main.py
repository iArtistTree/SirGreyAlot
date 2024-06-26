#imports pygame & time
from multiprocessing.connection import wait
import pygame,time, random
pygame.init()

from scripts import * 
from scripts.classes import *


#sets window settings
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project SirGreyAlot")
bgclr = (50,50,50)

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#images
scale = 5 #size images will be scaled by

plrSprite = pygame.image.load('./images/CharSpreadSheet.png').convert_alpha()
treeSprite = pygame.image.load('./images/Tree.png').convert_alpha()
bgImg = pygame.image.load('./images/background.png').convert_alpha()

#sprites groups
allsprites = pygame.sprite.Group()
collisionSprites = pygame.sprite.Group()

cameraGroup = CameraGroup(bgImg)

#sprites
for tree in range(15):
    x = random.randint(0 ,4000)
    y = random.randint(0 ,2000)

    Tree(x,y, treeSprite, screen,[collisionSprites, allsprites, cameraGroup])


player = Player(width/2,height/2, plrSprite, screen, collisionSprites, [allsprites, cameraGroup])

#game loop
run = True

while run:
    clock.tick(FPS)
    #BACKGROUND

    screen.fill(bgclr)

    #DRAW SPRITES

    #CONTROLS
    cameraGroup.update()
    cameraGroup.custom_daw(player, screen)

    #for loop through the event queue
    for event in pygame.event.get():        
        #check for QUIT event
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
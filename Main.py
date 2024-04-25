#imports pygame & time
from multiprocessing.connection import wait
import pygame,time
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
trees = pygame.sprite.Group()

#sprites
player = Player(width/2,height/2, plrSprite, screen)
tree1 = Tree(250,250, treeSprite, screen)
tree1.add(trees)

#game loop
run = True

while run:
    clock.tick(FPS)

    #BACKGROUND
    screen.fill(bgclr)

    #DRAW SPRITES
    player.draw()
    tree1.draw()

    if pygame.sprite.spritecollide(player, trees, False):
        #process keys
        keyPressed = pygame.key.get_pressed()
        
        #up or down
        if keyPressed[pygame.K_w] or keyPressed[pygame.K_s]:
            print("STOP")
        
        #left or right
        if keyPressed[pygame.K_a] or keyPressed[pygame.K_d]:
            print("STOP 2")


    #CONTROLS
    player.move()

    #for loop through the event queue
    for event in pygame.event.get():        
        #check for QUIT event
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
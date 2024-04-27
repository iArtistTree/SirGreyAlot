from typing import Iterable
import pygame
from pygame.sprite import AbstractGroup

#classspritesheet
class SpriteSHeet():
    def __init__(self, image):
        self.sheet = image

    def get_image(sheet, frame, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width),0, width, height))
        image = pygame.transform.scale_by(image, (5, 5))

        return image
    
#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spriteSheet, sheet, obstacles, groups):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(groups)
        

        #Position
        self.pos = pygame.math.Vector2(x, y)

        #Speed
        self.speed = 10

        #direction
        self.dir = pygame.math.Vector2(0, 0)

        self.image = pygame.transform.scale_by(SpriteSHeet.get_image(spriteSheet, 0, 30, 30), (1,1))
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.rect.center = pygame.math.Vector2(x,y)

        self.oldRect = self.rect.copy()

        self.flip = False
        self.sheet = sheet

        self.obstacles = obstacles

    def draw(self):
        self.sheet.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))

    def move(self):
        #reset variables
        self.dir.x = 0
        self.dir.y = 0

        #process keys
        keyPressed = pygame.key.get_pressed()
        
        #up & down
        if keyPressed[pygame.K_w]:
            self.dir.y = -1
        elif keyPressed[pygame.K_s]:
           self.dir.y = 1
        else:
            self.dir.y = 0


        #left or right
        if keyPressed[pygame.K_a]:
            self.dir.x = -1
            self.flip = True
        elif keyPressed[pygame.K_d]:
            self.dir.x = 1
            self.flip = False
        else:
            self.dir.x = 0

    def collision(self, direction): 
        collisionSprites = pygame.sprite.spritecollide(self, self.obstacles, False)

        
        if collisionSprites:
            if direction == 'horizontal':
                for sprite in collisionSprites:
                    #collision on the right
                    if self.rect.right >= sprite.rect.left and self.oldRect.right <= sprite.oldRect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x

                    #collision on the left
                    if self.rect.left <= sprite.rect.right and self.oldRect.left >= sprite.oldRect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x

            if direction == 'vertical':
                for sprite in collisionSprites:
                    #collision on the top
                    if self.rect.bottom >= sprite.rect.top and self.oldRect.bottom <= sprite.oldRect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y

                    #collision on the bottom
                    if self.rect.top <= sprite.rect.bottom and self.oldRect.top >= sprite.oldRect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y

    def update(self):
        self.oldRect = self.rect.copy()
        self.move()

        #update rectangle position
        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()

        self.pos.x += self.dir.x*self.speed
        self.rect.x = round(self.pos.x)
        self.collision('horizontal')

        self.pos.y += self.dir.y*self.speed
        self.rect.y = round(self.pos.y)
        self.collision('vertical')

#Camera
class CameraGroup(pygame.sprite.Group):
    def __init__(self, bgImg):
        super().__init__()
        self.displaySurface = pygame.display.get_surface()

        #camera offset
        self.offset = pygame.math.Vector2()
        self.halfW = self.displaySurface.get_size()[0] // 2
        self.halfH = self.displaySurface.get_size()[1] // 2

        #ground
        self.groundSurf = pygame.transform.scale_by(bgImg, (5,5))
        self.groundRect = self.groundSurf.get_rect(topleft = (0,0))

    def centerTargetCam(self, target):
        self.offset.x = target.rect.centerx - self.halfW
        self.offset.y = target.rect.centery - self.halfH

    def custom_daw(self, player, sheet):
        self.centerTargetCam(player)

        #ground
        groundOffset = self.groundRect.topleft - self.offset
        self.displaySurface.blit(self.groundSurf,groundOffset)

        #active elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)
            
            pygame.draw.rect(sheet, (255,255,255), sprite.rect, 2)


#DECORATIONS

#Tree
class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, spriteSheet, sheet, groups):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(groups)

        self.image = pygame.transform.scale_by(SpriteSHeet.get_image(spriteSheet, 0, 60, 60), (1,1))
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.rect.center = pygame.math.Vector2(x,y)
        self.pos = pygame.math.Vector2(x,y)
        self.sheet = sheet

        self.oldRect = self.rect.copy()

    def draw(self):
        self.sheet.blit(self.image, (self.pos.x, self.pos.y))


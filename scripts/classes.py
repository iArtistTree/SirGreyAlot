import pygame

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
    def __init__(self, x, y, spriteSheet, sheet, obstacles):
        pygame.sprite.Sprite.__init__(self)
        
        #Size
        self.height = 130
        self.width = 85

        #Position
        self.pos = pygame.math.Vector2(x, y)

        #Speed
        self.speed = 10

        #direction
        self.dir = pygame.math.Vector2(0, 0)

        self.image = SpriteSHeet.get_image(spriteSheet, 0, 30, 30)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = pygame.math.Vector2(x,y)

        self.oldRect = self.rect.copy()

        self.flip = False
        self.sheet = sheet

        self.obstacles = obstacles

    def draw(self):
        self.sheet.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x-33, self.rect.y-12))
        pygame.draw.rect(self.sheet, (255,255,255), self.rect, 2)

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

        

#DECORATIONS

#Tree
class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, spriteSheet, sheet):
        pygame.sprite.Sprite.__init__(self)

        #Size
        self.height = 150
        self.width = 125

        self.image = SpriteSHeet.get_image(spriteSheet, 0, 60, 60)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = pygame.math.Vector2(x,y)
        self.pos = pygame.math.Vector2(x,y)
        self.sheet = sheet

        self.oldRect = self.rect.copy()

    def draw(self):
        self.sheet.blit(self.image, (self.pos.x-150, self.pos.y-175))
        pygame.draw.rect(self.sheet, (255,255,255), self.rect, 2)


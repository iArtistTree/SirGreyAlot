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
    def __init__(self, x, y, spriteSheet, sheet):
        pygame.sprite.Sprite.__init__(self)
        
        #Size
        self.height = 130
        self.width = 85

        #Position
        self.posX = x
        self.posY = y

        #Velocity
        self.velX = 10
        self.velY = 10

        self.image = SpriteSHeet.get_image(spriteSheet, 0, 30, 30)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x,y)

        self.flip = False
        self.sheet = sheet

    def draw(self):
        self.sheet.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x-33, self.rect.y-12))
        pygame.draw.rect(self.sheet, (255,255,255), self.rect)

    def move(self):
        #reset variables
        dx = 0
        dy = 0

        #process keys
        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_w]:
            dy -= self.velY

        if keyPressed[pygame.K_a]:
            dx -= self.velX 
            self.flip = True
        
        if keyPressed[pygame.K_s]:
            dy += self.velY


        if keyPressed[pygame.K_d]:
            dx += self.velX 
            self.flip = False

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

#DECORATIONS

#Tree
class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, spriteSheet, sheet):
        self.image = SpriteSHeet.get_image(spriteSheet, 0, 60, 60)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.posX = x
        self.posY = y
        self.sheet = sheet

    def draw(self):
        self.sheet.blit(self.image, (self.posX, self.posY))


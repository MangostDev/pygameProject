import pygame
import sys
import random

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.color = "Blue"
        self.files = "player_car.png"
        self.index = 0
        self.images = pygame.image.load("player_car.png").convert_alpha()
        self.image = self.images
        self.rect = self.image.get_rect(center = (400,580))

    def collide(self):
        hit = pygame.sprite.spritecollide(self,enemies, False)
        if hit:
            self.kill()


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Car,self).__init__()
        self.index = random.randint(0,2)
        self.files = ["enemy_car1.png","enemy_car2.png","enemy_car3.png"]
        self.images = [pygame.image.load(filename).convert_alpha() for filename in self.files]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (x,y))

    def move(self):
        self.rect.centery += 7
        if self.rect.centery >= 800:
            self.kill()

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Background, self).__init__()
        self.files = ["enemy_car1.png","enemy_car2.png","enemy_car3.png"]
        self.images = [pygame.image.load(filename).convert_alpha() for filename in self.files]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (x,y))

# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create clock to later control frame rate
clock = pygame.time.Clock()

road = pygame.Surface((400,600))
road.fill("#333333")

grass = pygame.Surface((200,600))
grass.fill("#09B009")

player = Player()

enemies = pygame.sprite.Group()
enemies.add(Car(random.choice([210,230,250,270,290,310,330,350,370,390,410,430,450,470,490,510,530,550,570,590]),0))

objects = pygame.sprite.Group()
objects.add(player)

font = pygame.font.Font(None,100)
text_surface = font.render("Game Over", False,"Red")


# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)

    screen.blit(road,(200,0))
    screen.blit(grass,(0,0))
    screen.blit(grass,(600,0))

    if random.randint(1,10) == 1:
        enemies.add(Car(random.randint(210,590),0))
        objects.add(enemies)


    for car in enemies:
        car.move()

    player.collide()

    objects.draw(screen)

    if pygame.sprite.Sprite.alive(player) == False:
        screen.blit(text_surface,(200,250))


    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)



# Quit Pygame properly
pygame.quit()
sys.exit()

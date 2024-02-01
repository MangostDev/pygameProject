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
        if hit or self.rect.centerx < 200 or self.rect.centerx > 600:
            self.kill()


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Car,self).__init__()
        self.index = random.randint(0,2)
        self.files = ["enemy_car1.png","enemy_car2.png","enemy_car3.png"]
        self.images = [pygame.image.load(filename).convert_alpha() for filename in self.files]
        self.image = self.images[self.index]
        self.speed = random.randint(5,10)
        self.rect = self.image.get_rect(center = (x,y))

    def move(self):
        self.rect.centery += self.speed
        if self.rect.centery >= 600:
            self.kill()

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Background, self).__init__()
        self.index = random.randint(0,5)
        self.files = ["blue_flower.png","orange_flower.png","pink_flower.png","purple_flower.png","red_flower.png","yellow_flower.png"]
        self.images = [pygame.image.load(filename).convert_alpha() for filename in self.files]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (x,y))

    def move(self):
        self.rect.centery += 7
        if self.rect.centery >= 600:
            self.kill()

# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

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
enemies.add(Car(random.choice([210,250,290,330,370,410,450,490,530,570]),0))

flowers = pygame.sprite.Group()
flowers.add(Background(random.choice([random.randint(0,200),random.randint(600,800)]),0))

objects = pygame.sprite.Group()
objects.add(player)

font = pygame.font.Font(None,100)
text_surface = font.render("Game Over", False,"Red")
text_surface_two = font.render("You Win!", False,"Green")


# Main game loop
count = 0
running = True
while running:
    count += 1
    # Event handling

    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)

    screen.blit(road,(200,0))
    screen.blit(grass,(0,0))
    screen.blit(grass,(600,0))

    if random.randint(1,10) == 1 and count < 1000:
        enemies.add(Car(random.choice([210,250,290,330,370,410,450,490,530,570]),0))
        objects.add(enemies)

    if random.randint(1,5):
        flowers.add(Background(random.choice([random.randint(0,200),random.randint(600,800)]),0))
    objects.add(flowers)


    for car in enemies:
        car.move()

    for flower in flowers:
        flower.move()

    player.collide()

    objects.draw(screen)

    if pygame.sprite.Sprite.alive(player) == False:
        screen.blit(text_surface,(200,250))

    if len(enemies.sprites()) == 0:
        screen.blit(text_surface_two,(300,250))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.centerx -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.centerx += 5
    if keys[pygame.K_UP] and player.rect.centery > 10:
        player.rect.centery -= 5
    if keys[pygame.K_DOWN] and player.rect.centery < 590:
        player.rect.centery += 5


    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)



# Quit Pygame properly
pygame.quit()
sys.exit()

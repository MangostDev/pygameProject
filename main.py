import pygame
import sys

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.color = "Blue"

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super(Car,self).__init__()

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

    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
FLOWER_COLOR = (255, 0, 0)
FLOWER_CENTER = (WIDTH // 2, HEIGHT // 2)
PETAL_RADIUS = 50

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flower Animation")

# Main loop
angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    # Calculate the position of the petals
    x = FLOWER_CENTER[0] + PETAL_RADIUS * math.cos(math.radians(angle))
    y = FLOWER_CENTER[1] + PETAL_RADIUS * math.sin(math.radians(angle))

    # Draw the petals
    pygame.draw.circle(screen, FLOWER_COLOR, (int(x), int(y)), 10)

    angle += 2  # Adjust the rotation speed

    pygame.display.update()
    clock.tick(60)
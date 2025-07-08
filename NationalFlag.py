import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Scale factor
scale_factor = 30

# Take input for start point
x1 = int(input("Enter the start x-coordinate of the flag: "))
y1 = int(input("Enter the start y-coordinate of the flag: "))

# Calculate end points (width:height = 10:6)
flag_width = 10 * scale_factor
flag_height = 6 * scale_factor
x2 = x1 + flag_width
y2 = y1 + flag_height

# Window size large enough to fit flag and handle
win_width = max(800, x2 + 100)
win_height = max(600, y2 * 2 + 100)
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Bangladesh Flag")

# Colors
GREEN = (0, 106, 78)
RED = (244, 42, 65)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)  # Background
TREE_TRUNK_COLOR = (139, 69, 19)  # Brown for tree trunks
TREE_FOLIAGE_COLOR = (34, 139, 34)  # Green for leaves
LIGHT_GREEN = (60, 179, 113)  # A lighter shade of green for more depth in foliage
MUD_COLOR = (205, 133, 63)  # Lighter brown for the mud

# Fill background with sky blue
screen.fill(SKY_BLUE)

# Draw the ground (mud and trees)
# Drawing the mud section at the bottom part of the screen
mud_height = int(win_height * 0.2)
pygame.draw.rect(screen, MUD_COLOR, (0, win_height - mud_height, win_width, mud_height))

# Adding beautiful trees
def draw_tree(x, y, trunk_height, trunk_width, crown_radius):
    # Draw tree trunk
    pygame.draw.rect(screen, TREE_TRUNK_COLOR, (x - trunk_width // 2, y, trunk_width, trunk_height))
    
    # Draw multiple layers of tree foliage (circular shape for leaves)
    for i in range(3):
        pygame.draw.circle(screen, TREE_FOLIAGE_COLOR, (x, y - trunk_height - i * crown_radius // 2), crown_radius + i * 5)
        pygame.draw.circle(screen, LIGHT_GREEN, (x, y - trunk_height - (i + 1) * crown_radius // 2), crown_radius + (i + 1) * 5)

# Adding multiple trees with random positions and sizes
for _ in range(8):  # Number of trees
    tree_x = random.randint(50, win_width - 50)
    tree_y = random.randint(win_height - mud_height - 100, win_height - mud_height - 20)
    trunk_height = random.randint(40, 60)
    trunk_width = random.randint(10, 15)
    crown_radius = random.randint(20, 30)

    draw_tree(tree_x, tree_y, trunk_height, trunk_width, crown_radius)

# Draw green rectangle (flag)
pygame.draw.rect(screen, GREEN, (x1, y1, flag_width, flag_height))

# Draw red circle (sun)
circle_radius = 2 * scale_factor
circle_x = x1 + int(0.45 * flag_width)
circle_y = y1 + int(0.5 * flag_height)
pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

# Draw black handle (flag pole)
pole_width = max(scale_factor // 3, 10)
pygame.draw.rect(screen, BLACK, (x1 - pole_width, y1, pole_width, 2 * flag_height))

# Update the display
pygame.display.update()

# Wait until the user closes the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

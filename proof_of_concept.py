# Created by Yaseen Alkhafaji <yaseen@mit.edu>
# using the pygame library (pygame.org)
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hope you enjoy my Mondrian masterpiece!")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#Drawing code goes here:

# Clear the screen and set the screen background
screen.fill(WHITE)

# Draw the vertical Lines
pygame.draw.line(screen, BLACK, [112, 0], [112, 400], 5)
pygame.draw.line(screen, BLACK, [316, 0], [316, 400], 5)
pygame.draw.line(screen, BLACK, [211, 311], [211, 400], 5)

# Draw the horizontal Lines
pygame.draw.line(screen, BLACK, [0, 57], [400, 57], 5)
pygame.draw.line(screen, BLACK, [0, 218], [400, 218], 5)
pygame.draw.line(screen, BLACK, [0, 308], [400, 308], 5)
pygame.draw.line(screen, BLACK, [115, 167], [400, 167], 5)

# Draw the rectangles
pygame.draw.rect(screen, YELLOW, [115, 0, abs(313 - 115 + 1), abs(54 - 0 + 1)], 0)
pygame.draw.rect(screen, BLACK, [115, 60, abs(313 - 115 + 1), abs(164 - 60 + 1)], 0)
pygame.draw.rect(screen, RED, [319, 60, abs(400 - 319 + 1), abs(164 - 60 + 1)], 0)
pygame.draw.rect(screen, BLUE, [319, 170, abs(400 - 319 + 1), abs(215 - 170 + 1)], 0)
pygame.draw.rect(screen, RED, [0, 221, abs(109 - 0 + 1), abs(305 - 221 + 1)], 0)
pygame.draw.rect(screen, BLUE, [115, 311, abs(208 - 115 + 1), abs(400 - 311 + 1)], 0)
pygame.draw.rect(screen, BLACK, [319, 311, abs(400 - 319 + 1), abs(400 - 311 + 1)], 0)

# Go ahead and update the screen with what we've drawn.
# This MUST happen after all the other drawing commands.
pygame.display.flip()

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop


# Be IDLE friendly
pygame.quit()
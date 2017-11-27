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

# list of lines, defined as a pair of points (start, end)
line_list = [[[112, 0], [112, 400]], [[316, 0], [316, 400]], [[211, 311], [211, 400]], [[0, 57], [400, 57]], [[0, 218], [400, 218]], [[0, 308], [400, 308]], [[115, 167], [400, 167]]]

# list of rectangles, defined as a color appended to a list of points (color, top-left, bottom-right)
rectangle_list = [[YELLOW, [(115, 0), (313, 54)]],
                  [BLACK, [(115, 60), (323, 164)]],
                  [RED, [(319, 60), (400, 164)]],
                  [BLUE, [(319, 170), (400, 215)]],
                  [RED, [(0, 221), (109, 305)]],
                  [BLUE, [(115, 311), (208, 400)]],
                  [BLACK, [(319, 311), (400, 400)]]]


def generate_outline():
    pass


def generate_rectangles():
    pass


def draw_outline():
    for pair in line_list:
        pygame.draw.line(screen, BLACK, pair[0], pair[1], 5)


def draw_rectangles():
    for rect in rectangle_list:
        color = rect[0]
        top_left_x, top_left_y = rect[1][0]
        bottom_right_x, bottom_right_y = rect[1][1]
        width = abs(top_left_x - bottom_right_x) + 1
        height = abs(top_left_y - bottom_right_y) + 1
        pygame.draw.rect(screen, color, [top_left_x, top_left_y, width, height], 0)


# Drawing code goes here:
screen.fill(WHITE)

generate_outline()
generate_rectangles()
draw_outline()
draw_rectangles()

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
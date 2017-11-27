# Created by Yaseen Alkhafaji <yaseen@mit.edu>
# using the pygame library (pygame.org)
import pygame, random

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

fl_x_coords = []
fl_y_coords = []

# list of rectangles, with each rectangle defined as a color and a pair of points (color, (top-left, bottom-right))
rectangle_list = [[YELLOW, [(115, 0), (313, 54)]],
                  [BLACK, [(115, 60), (323, 164)]],
                  [RED, [(319, 60), (400, 164)]],
                  [BLUE, [(319, 170), (400, 215)]],
                  [RED, [(0, 221), (109, 305)]],
                  [BLUE, [(115, 311), (208, 400)]],
                  [BLACK, [(319, 311), (400, 400)]]]

MIN_SPACE_BETWEEN_LINES = 80

def gen_full_length_lines(vertical):
    if vertical:
        # first, 2 - 4 "random" vertical lines, positioned by dividing width into equal quadrants and placing a single line randomly within each quadrant
        num_lines = random.randint(2, 4)
        quadrant_width = size[0]/num_lines
        x_coordinates = []
        points = []
        for i in range(0, num_lines):
            min_range = int(quadrant_width * i)
            if i > 0:
                if (quadrant_width*i - x_coordinates[len(x_coordinates) - 1]) < MIN_SPACE_BETWEEN_LINES:
                    min_range = x_coordinates[len(x_coordinates) - 1] + MIN_SPACE_BETWEEN_LINES
            else:
                min_range = MIN_SPACE_BETWEEN_LINES
            if i == num_lines - 1:
                if (size[0] - MIN_SPACE_BETWEEN_LINES) - min_range < MIN_SPACE_BETWEEN_LINES:
                    break
                else:
                    x_coord = random.randrange(min_range, size[0] - MIN_SPACE_BETWEEN_LINES)
            else:
                x_coord = random.randrange(min_range, int(quadrant_width*(i+1)))
            x_coordinates.append(x_coord)
            points.append([[x_coord, 0], [x_coord, 400]])
        fl_x_coords.extend(x_coordinates)
    else:
        num_lines = random.randint(2, 4)
        quadrant_height = size[1] / num_lines
        y_coordinates = []
        points = []
        for i in range(0, num_lines):
            min_range = int(quadrant_height * i)
            if i > 0:
                if (quadrant_height * i - y_coordinates[len(y_coordinates) - 1]) < MIN_SPACE_BETWEEN_LINES:
                    min_range = y_coordinates[len(y_coordinates) - 1] + MIN_SPACE_BETWEEN_LINES
            else:
                min_range = MIN_SPACE_BETWEEN_LINES
            if i == num_lines - 1:
                if (size[1] - MIN_SPACE_BETWEEN_LINES) - min_range < MIN_SPACE_BETWEEN_LINES:
                    break
                else:
                    y_coord = random.randrange(min_range, size[1] - MIN_SPACE_BETWEEN_LINES)
            else:
                y_coord = random.randrange(min_range, int(quadrant_height * (i + 1)))
            y_coordinates.append(y_coord)
            points.append([[0, y_coord], [400, y_coord]])
        fl_y_coords.extend(y_coordinates)
    return points


def gen_partial_lines(vertical):
    if vertical:
        x_possibilities = [0] + fl_x_coords + [400]
        points = []
        for i in range(0, len(x_possibilities) - 1):
            if (x_possibilities[i+1] - x_possibilities[i] > 90) and len(fl_y_coords) > 1:
                min_range = x_possibilities[i]+40
                max_range = x_possibilities[i+1]-40
                x_coord = random.randint(min_range, max_range)

                y_possibilities = [0] + fl_y_coords + [400]
                min_y = random.randrange(0, len(y_possibilities) - 1)

                # ensures that this doesn't randomly create a full-length line
                if min_y == 0:
                    max_y = random.randrange(min_y + 1, len(y_possibilities) - 1)
                else:
                    if min_y + 1 == len(y_possibilities) - 1:
                        max_y = len(y_possibilities) - 1
                    else:
                        max_y = random.randrange(min_y + 1, len(y_possibilities))

                points.append([[x_coord, y_possibilities[min_y]], [x_coord, y_possibilities[max_y]]])
        return points
    else:
        y_possibilities = [0] + fl_y_coords + [400]
        points = []
        for i in range(0, len(y_possibilities) - 1):
            if (y_possibilities[i + 1] - y_possibilities[i] > 90) and len(fl_x_coords) > 1:
                min_range = y_possibilities[i] + 40
                max_range = y_possibilities[i + 1] - 40
                y_coord = random.randint(min_range, max_range)

                x_possibilities = [0] + fl_x_coords + [400]
                min_x = random.randrange(0, len(x_possibilities) - 1)

                # ensures that this doesn't randomly create a full-length line
                if min_x == 0:
                    max_x = random.randrange(min_x + 1, len(x_possibilities) - 1)
                else:
                    if min_x + 1 == len(x_possibilities) - 1:
                        max_x = len(x_possibilities) - 1
                    else:
                        max_x = random.randrange(min_x + 1, len(x_possibilities))

                points.append([[x_possibilities[min_x], y_coord], [x_possibilities[max_x], y_coord]])
        return points


def generate_outline():
    line_list.clear()
    line_list.extend(gen_full_length_lines(True))   # generates full length vertical lines
    line_list.extend(gen_full_length_lines(False))  # generates full length horizontal lines
    line_list.extend(gen_partial_lines(True))       # generates partial-length vertical lines
    line_list.extend(gen_partial_lines(False))      # generates partial-length horizontal lines


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
#draw_rectangles()

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
import pygame
import time
import random


# set up pygame window
WIDTH = 802
HEIGHT = 802
FPS = 30

WHITE = (236, 240, 241)
GREEN = (46, 204, 113)
BLUE = (41, 128, 185)
YELLOW = (243, 156, 18)

# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()


# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 40                   # width of cell
grid = []
visited = []
stack = []
solution = {}

def build_grid(x,y,w):
    for i in range(1,21):
        x = 0                                                             # set x coordinate to start position
        y = y + 40                                                        # start a new row
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left of cell
            grid.append((x,y))                                            # add cell to grid list
            x = x + 40   
            time.sleep(.1)                                                 # move cell to new position
            pygame.display.update() 




x, y = 0, 0                     # starting position of grid
build_grid(0, 0, 40)            # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
import pygame
import numpy as np
pygame.init()

BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREY = (105, 105, 105)

# Open a new window

cellsize = 10
WIDTH = 800
HEIGHT = 800
cell_x = WIDTH // cellsize
cell_y = HEIGHT // cellsize
size = (WIDTH, HEIGHT)
cellnum = cell_x * cell_y
cells = np.zeros((cell_x, cell_y), dtype=bool)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")



def drawWindow(cellArr):
    screen.fill(WHITE)
    for i in range(cell_x):
        for k in range(cell_y):
            if (cellArr[i][k] == True):
                pygame.draw.rect(screen, BLACK, [k*cellsize, i*cellsize, cellsize, cellsize])  
    for j in range(cell_x):
        pygame.draw.line(screen, GREY, (j*cellsize, 0), (j*cellsize, WIDTH))
    for l in range(cell_y):          
        pygame.draw.line(screen, GREY, (0, l*cellsize), (HEIGHT, l*cellsize)) 


# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
runSim = False
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_r]:
                cells = np.zeros((cell_x, cell_y), dtype=bool)    
            else:
                if runSim:
                    runSim = False
                else:
                    runSim = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            x = mousepos[1]//cellsize
            y = mousepos[0]//cellsize
            if cells[x][y]:
                cells[x][y] = False
            else:
                cells[x][y] = True
          

     # --- Game logic
    if runSim:
        tempcells = np.zeros((cell_x, cell_y), dtype=bool)
        for i in range(cell_x):
            for s in range(cell_y): # for every cell in cells
                neighborcount = 0
                cell_alive = cells[s][i]
                for x in range(3):
                    for y in range(3):
                        xval = s+x-1
                        yval = i+y-1
                        if (xval >= 0) and (yval >= 0) and (xval < cell_x) and (yval < cell_y):
                            if cells[xval][yval] == True:
                                neighborcount = neighborcount + 1
                if cell_alive:
                    neighborcount = neighborcount - 1
                if ((cell_alive) and (neighborcount<4) and (neighborcount>1)):
                    tempcells[s][i] = True
                elif ((not cell_alive) and (neighborcount == 3)):
                    tempcells[s][i] = True
                else:
                    tempcells[s][i] = False
        cells = tempcells

         
 
     # --- Drawing code
    drawWindow(cells)
 
 
     # --- Update the screen
    pygame.display.flip()
     
     # --- Limit to 10 frames per second
    clock.tick(10)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()

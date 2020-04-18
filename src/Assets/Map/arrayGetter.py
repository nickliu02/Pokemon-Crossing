from pygame import *

# Pygame Window
size = width, height = 5760, 5760
screen = display.set_mode(size)
init()

# Constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

myClock = time.Clock()
pic = image.load("C:\\Users\\nickl\\Desktop\\Com Sci\\Pokemon Crossing\\Assets\\Map\\PC Mask.png")

grid = [[None for i in range(94)] for j in range(85)]

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    screen.blit(pic, (0,0))
    
    for i in range(94):
        for j in range(85):
            if screen.get_at((i*60+30, j*60+30)) == (255, 255, 255):
                grid[j][i] = "1"
            else:
                grid[j][i] = "0"
    

   
    
   
    
    display.flip()
    myClock.tick(60)
    running = False
    


file = open("map.txt", "w")

for i in range(85):
    file.write(" ".join(grid[i])+"\n")
file.close()

print("done")
quit()
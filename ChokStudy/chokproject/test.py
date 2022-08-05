import pygame as pyg
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)

C1_BLUE = (204, 204, 255) # Custom blue color 1

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN,K_b:BLUE,K_y:YELLOW,K_w:WHITE}
print(key_dict)


screen = pyg.display.set_mode((800,600))
bgColor = C1_BLUE
caption = 'BG Color : ' + str(bgColor)
pyg.display.set_caption(caption)
screen.fill(bgColor)
pyg.display.update()

pyg.init()

running = True
while running:
    for pyEvent in pyg.event.get():
        if pyEvent.type == KEYDOWN:
            if pyEvent.key in key_dict:
                bgColor = key_dict[pyEvent.key]
                caption = 'BG Color : ' + str(bgColor)
                pyg.display.set_caption(caption)
            else:
                bgColor = C1_BLUE
                
        if pyEvent.type == pyg.QUIT:
            running = False
        screen.fill(bgColor)
        pyg.display.update()

pyg.quit()
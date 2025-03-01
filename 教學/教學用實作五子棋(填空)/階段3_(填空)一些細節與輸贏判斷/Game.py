#
#    本文件相對上階段並無改動
#

import pygame
from Setting import *
from Pieces import PiecesGroup
import math
#---------------------<初始設定>---------------------
#========>物件<========
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIN_WIDTH_HEIGHT,WIN_WIDTH_HEIGHT))
pygame.display.set_caption("五子棋") 
piecegroup = PiecesGroup()

#---------------------<DEF>---------------------
def get_mouse_coordinate() -> tuple:
    mouse_pos = pygame.mouse.get_pos() 
    x = math.floor(mouse_pos[0]/UNIT_LENGTH-0.5)
    y = math.floor(mouse_pos[1]/UNIT_LENGTH-0.5)
    return (x,y)
def draw_background(surface:pygame.surface.Surface) -> None:
    surface.fill(WIN_BACKGROUND_COLOR)

    width = 1
    for i in range(WAY):
        start_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH)
        end_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH*WAY)
        pygame.draw.line(surface,BLACK,start_pos,end_pos,width)
        start_pos = (UNIT_LENGTH,UNIT_LENGTH*(i+1))
        end_pos = (UNIT_LENGTH*WAY,UNIT_LENGTH*(i+1))
        pygame.draw.line(surface,BLACK,start_pos,end_pos,width)
    pygame.draw.circle(surface ,BLACK ,(UNIT_LENGTH*( ((WAY-1)/2) +1), UNIT_LENGTH*( ((WAY-1)/2) +1)) , 5)
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*(3+1), UNIT_LENGTH*(3+1))) , 5)
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*(3+1), UNIT_LENGTH*((WAY-1-3) + 1))) , 5)            
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*((WAY-1-3) + 1), UNIT_LENGTH*(3+1))) , 5)            
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*((WAY-1-3) + 1), UNIT_LENGTH*((WAY-1-3) + 1))) , 5)  

#--------------------<Main>---------------------
def main() -> None:
    global piecegroup
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if piecegroup.winner == 0:
                    pos = get_mouse_coordinate()
                    if((pos[0]>=0) and (pos[0]<WAY and (pos[1]>=0) and (pos[1]<WAY))):
                        piecegroup.move(pos[0],pos[1])
        #更新遊戲update
        #畫面顯示render
        draw_background(win)
        piecegroup.draw(win)
        pygame.display.update()
#---------------------<     >---------------------
if(__name__ == "__main__"):
    pygame.init()
    main()
    pygame.quit()

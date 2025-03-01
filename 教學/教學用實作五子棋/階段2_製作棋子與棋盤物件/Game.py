import pygame
from Setting import *
from Pieces import PiecesGroup
import math
#---------------------<初始設定>---------------------
#========>物件<========
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIN_WIDTH_HEIGHT,WIN_WIDTH_HEIGHT))
pygame.display.set_caption("五子棋")
#PieceGroup
piecegroup = PiecesGroup()

#---------------------<DEF>---------------------
def get_mouse_coordinate() -> tuple:
    mouse_pos = pygame.mouse.get_pos()  #獲得滑鼠位置
    x = math.floor(mouse_pos[0]/UNIT_LENGTH-0.5)    #無條件捨去
    y = math.floor(mouse_pos[1]/UNIT_LENGTH-0.5)    #無條件捨去
    return (x,y)
    #--------------------------------------------------------------------------------------------#
    #  讓我們在螢幕座標空間中思考這個指令
    #  math.floor(mouse_pos[0]/UNIT_LENGTH)
    #  mouse_pos[0] 是滑鼠在螢幕座標中的水平分量(x方向)
    #
    #  我們現在假設滑鼠在這個位置
    #  (0,0) ---- (1,0) ---- (2,0) ----
    #    |          |          |
    #  (0,1) ---- (1,1) ---- (2,1) ---- 
    #    |          |   滑鼠   |
    #  (0,2) ---- (1,2) ---- (2,2) ----
    #    |          |          |
    #  那麼 mouse_pos[0]/UNIT_LENGTH == 1.多 ， mouse_pos[1]/UNIT_LENGTH == 1.多
    #  將他們無條件捨去就會得到 1,1
    #
    #  math.floor(mouse_pos[0]/UNIT_LENGTH)
    #  math.floor(mouse_pos[1]/UNIT_LENGTH)
    #  如果夠仔細思考的話，你會發現在(1,1),(2,1),(2,2),(1,2)這四點中的矩形區域出來的結果都會是 1,1
    #  為了讓判斷的格子變成以線條交會點為中心
    #  或們可以簡單的透過減掉 0.5 將整個矩形區域往左上移到正確的區域
    #--------------------------------------------------------------------------------------------#


def draw_background(surface:pygame.surface.Surface) -> None:    #這個函式相對上階段無任何改動
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
        #取得輸入input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :  #滑鼠按下    #為了讓我們放置棋子
                if piecegroup.winner == 0:  #若產生贏家就停下來
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

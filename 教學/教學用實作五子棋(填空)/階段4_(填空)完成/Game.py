import pygame
from Setting import *
from Pieces import PiecesGroup
import math
import os

#
#   按住 CTRL + F 搜尋 ___請填空___
#

word = os.path.join("img" , "font.ttf")
#---------------------<初始設定>---------------------
#========>物件<========
#Clock
clock = pygame.time.Clock()
#Screen
win = pygame.display.set_mode((WIN_WIDTH_HEIGHT,WIN_WIDTH_HEIGHT))    #Build a screen  
pygame.display.set_caption("五子棋")  #Screen Title
#image
white_img = pygame.image.load(os.path.join("img","White.png")).convert_alpha()
white_img = pygame.transform.scale(white_img,(UNIT_LENGTH-3,UNIT_LENGTH-3)) #縮放
black_img = pygame.image.load(os.path.join("img","Black.png")).convert_alpha()
black_img = pygame.transform.scale(black_img,(UNIT_LENGTH-3,UNIT_LENGTH-3)) #縮放 
#PieceGroup
piecegroup = PiecesGroup()

#---------------------<DEF>---------------------
def get_mouse_coordinate() -> tuple:
    mouse_pos = pygame.mouse.get_pos()  #獲得滑鼠位置
    x = math.floor(mouse_pos[0]/UNIT_LENGTH-0.5)    #無條件捨去
    y = math.floor(mouse_pos[1]/UNIT_LENGTH-0.5)    #無條件捨去
    return (x,y)

def draw_text(surface:pygame.surface.Surface,text:str,size:int,x:float,y:float,color:tuple) -> None:
    font = pygame.font.___請填空___( word , size )
    text_surface = font.___請填空___( text , True , color ) 
    text_rect = text_surface.___請填空___()
    text_rect.centerx = x 
    text_rect.centery = y 
    surface.blit(text_surface , text_rect)

def draw_background(surface:pygame.surface.Surface) -> None:
    #背景顏色
    surface.fill(WIN_BACKGROUND_COLOR)

    width = 1
    #畫直線
    for i in range(WAY):
        start_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH)
        end_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH*WAY)
        pygame.draw.line(surface,BLACK,start_pos,end_pos,width)
    #畫橫線
        start_pos = (UNIT_LENGTH,UNIT_LENGTH*(i+1))
        end_pos = (UNIT_LENGTH*WAY,UNIT_LENGTH*(i+1))
        pygame.draw.line(surface,BLACK,start_pos,end_pos,width)
    #天元(中心點)            #備註: 棋盤上座標(x,y)轉換為螢幕座標公式: (UNIT_LENGTH*(x+1) , UNIT_LENGTH*(y+1))
    pygame.draw.circle(surface ,BLACK ,(UNIT_LENGTH*( ((WAY-1)/2) +1), UNIT_LENGTH*( ((WAY-1)/2) +1)) , 5)
    #四角落                 #備註: 棋盤上座標(x,y)轉換為螢幕座標公式: (UNIT_LENGTH*(x+1) , UNIT_LENGTH*(y+1))
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*(3+1), UNIT_LENGTH*(3+1))) , 5)                      #左上角
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*(3+1), UNIT_LENGTH*((WAY-1-3) + 1))) , 5)            #左下角
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*((WAY-1-3) + 1), UNIT_LENGTH*(3+1))) , 5)            #右上角
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*((WAY-1-3) + 1), UNIT_LENGTH*((WAY-1-3) + 1))) , 5)  #右下角
    #劃出誰拿黑誰拿白
    draw_text(surface , "玩家1" , 30 , 80 , 725 , BLACK)
    draw_text(surface , "玩家2" , 30 , 670 , 725 , BLACK )
    surface.blit(white_img , (580 , 705))
    surface.blit(black_img , (130 , 705))

def draw_win(surface:pygame.surface.Surface) -> None:
    if(piecegroup.winner != 0): #要先有贏家
        color = (255,0,0)   #red
        start_pos = (UNIT_LENGTH*(piecegroup.win_start[0]+1) ,UNIT_LENGTH*(piecegroup.win_start[1]+1))
        end_pos =   (UNIT_LENGTH*(piecegroup.win_end[0]+1)   ,UNIT_LENGTH*(piecegroup.win_end[1]+1))
        width = 5
        pygame.draw.line(surface,color,start_pos,end_pos,width)
        #畫出勝利者的圖示
        draw_text(surface , f"玩家{piecegroup.winner} is winner!!" , 50 , 375 , 375 , (66,124,206))

#--------------------<Main>---------------------
def main() -> None:
    global piecegroup
    running = True
    while running:
        clock.tick(FPS) #畫面更新頻率
        #取得輸入input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #若是關閉按鈕
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :  #滑鼠按下
                if piecegroup.winner == 0:  #若產生贏家就停下來
                    pos = get_mouse_coordinate()
                    if((pos[0]>=0) and (pos[0]<WAY and (pos[1]>=0) and (pos[1]<WAY))):
                        piecegroup.move(pos[0],pos[1])
        #更新遊戲update
        #畫面顯示render
        draw_background(win)
        piecegroup.draw(win)
        draw_win(win)
        pygame.display.update() #Update Screen

#---------------------<     >---------------------
if(__name__ == "__main__"):
    pygame.init()
    main()
    pygame.quit()

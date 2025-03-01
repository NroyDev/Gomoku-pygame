from Pieces import PiecesGroup
from GameSetting import *
from Network import Network     ######
import pygame
import math
import socket

#---------------------<初始設定>---------------------
#========>物件<========
#Clock
clock = pygame.time.Clock()
#Screen
win = pygame.display.set_mode((WIN_WIDTH_HEIGHT,WIN_WIDTH_HEIGHT))    #Build a screen
pygame.display.set_caption("五子棋")  #Screen Title
#PieceGroup
piecegroup = PiecesGroup()
#---------------------<DEF>---------------------
def get_mouse_coordinate() -> tuple:
    mouse_pos = pygame.mouse.get_pos()  #獲得滑鼠位置
    x = math.floor(mouse_pos[0]/UNIT_LENGTH-0.5)    #無條件捨去
    y = math.floor(mouse_pos[1]/UNIT_LENGTH-0.5)    #無條件捨去
    return (x,y)


def draw_background(surface:pygame.surface.Surface) -> None:
    #背景顏色
    surface.fill(WIN_BACKGROUND_COLOR)
    
    color = (0,0,0) #Black
    width = 1
    #畫直線
    for i in range(WAY):
        start_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH)
        end_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH*WAY)
        pygame.draw.line(surface,color,start_pos,end_pos,width)
    #畫橫線
    for i in range(WAY):
        start_pos = (UNIT_LENGTH,UNIT_LENGTH*(i+1))
        end_pos = (UNIT_LENGTH*WAY,UNIT_LENGTH*(i+1))
        pygame.draw.line(surface,color,start_pos,end_pos,width)

def draw_win(surface:pygame.surface.Surface) -> None:
    if(piecegroup.winner != 0): #要先有贏家
        color = (255,0,0)   #red
        start_pos = (UNIT_LENGTH*(piecegroup.win_start[0]+1),UNIT_LENGTH*(piecegroup.win_start[1]+1))
        end_pos = (UNIT_LENGTH*(piecegroup.win_end[0]+1),UNIT_LENGTH*(piecegroup.win_end[1]+1))
        width = 5
        pygame.draw.line(surface,color,start_pos,end_pos,width)

def main() -> None:
    global piecegroup
    running = True
    n = Network()       ######
    while running:
        clock.tick(FPS) #畫面更新頻率
        
        #取得輸入input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #若是關閉按鈕
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  #滑鼠按下
                if piecegroup.winner == 0 and piecegroup.turn == n.id and n.ready:  #沒有贏家 且 是我方回合 且 雙方就緒 ######
                    pos = get_mouse_coordinate()
                    if((pos[0]>=0) and (pos[0]<WAY and (pos[1]>=0) and (pos[1]<WAY))):
                        n.send(pos[0],pos[1])      ######
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:  #按鈕按下 且 按下的是R鍵
                if piecegroup.winner != 0:  #產生贏家才可以開新的一局
                    #piecegroup = PiecesGroup()
                    piecegroup.reset()
                        
        #更新遊戲update     ######
        if n.ready:
            try:
                pos = n.client.recv(2048).decode().split(",")
                piecegroup.move(int(pos[0]),int(pos[1]))
                if piecegroup.winner != 0:
                    print("Winner is",piecegroup.winner)
            except socket.timeout:
                pass
        else:
            try:
                ready = n.client.recv(2048).decode()
                if ready == "1":
                    n.ready = True
            except socket.timeout:
                pass
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
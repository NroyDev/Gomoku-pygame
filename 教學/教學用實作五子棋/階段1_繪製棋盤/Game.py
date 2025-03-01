import pygame
from Setting import *
#---------------------<初始設定>---------------------
#========>物件<========
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIN_WIDTH_HEIGHT,WIN_WIDTH_HEIGHT))
pygame.display.set_caption("五子棋")

#---------------------<DEF>---------------------
def draw_background(surface:pygame.surface.Surface) -> None:
    #背景顏色
    surface.fill(WIN_BACKGROUND_COLOR)

    width = 1
    #畫直線     簡報18~22頁
    for i in range(WAY):
        start_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH)
        end_pos = (UNIT_LENGTH*(i+1),UNIT_LENGTH*WAY)
        pygame.draw.line(surface,BLACK,start_pos,end_pos,width)
    #畫橫線     簡報18~22頁
        start_pos = (UNIT_LENGTH,UNIT_LENGTH*(i+1))
        end_pos = (UNIT_LENGTH*WAY,UNIT_LENGTH*(i+1))
        pygame.draw.line(surface,BLACK,start_pos,end_pos,width)
    #天元(中心點)            #備註: 棋盤上座標(x,y)轉換為螢幕座標公式: (UNIT_LENGTH*(x+1) , UNIT_LENGTH*(y+1))  #推導過程類似於 簡報16~18頁
    pygame.draw.circle(surface ,BLACK ,(UNIT_LENGTH*( ((WAY-1)/2) +1), UNIT_LENGTH*( ((WAY-1)/2) +1)) , 5)
    #四角落                 #備註: 棋盤上座標(x,y)轉換為螢幕座標公式: (UNIT_LENGTH*(x+1) , UNIT_LENGTH*(y+1))   #推導過程類似於 簡報16~18頁
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*(3+1), UNIT_LENGTH*(3+1))) , 5)                      #左上角
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*(3+1), UNIT_LENGTH*((WAY-1-3) + 1))) , 5)            #左下角
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*((WAY-1-3) + 1), UNIT_LENGTH*(3+1))) , 5)            #右上角
    pygame.draw.circle(surface , BLACK , ((UNIT_LENGTH*((WAY-1-3) + 1), UNIT_LENGTH*((WAY-1-3) + 1))) , 5)  #右下角

    #-------------------------------------------------------------#
    # UNIT_LENNGTH 就是棋盤中每一格的長度(也是寬度) (螢幕座標中)
    # 螢幕邊緣到棋盤的線條邊緣也是 1 個 UNIT_LENGTH
    # 我們定義一個新的座標系:棋盤座標
    #   棋盤座標以棋盤線條的交點作為"格子點"            (格子點的數學定義:https://www.ehanlin.com.tw/app/keyword/%E9%AB%98%E4%B8%AD/%E6%95%B8%E5%AD%B8/%E6%A0%BC%E5%AD%90%E9%BB%9E.html)
    #   棋盤座標的左上角必為(0,0)，向右為正，向下為正
    # 我們大致可以對此棋盤坐標系理解成:
    #  (0,0) ---- (1,0) ---- (2,0) ---- ......
    #    |          |          |
    #  (0,1) ---- (1,1) ---- (2,1) ---- ......
    #    |          |          |
    #  (0,2) ---- (1,2) ---- (2,2) ---- ......
    #    |          |          |
    #   以下省略.................................
    #
    # 因為 "螢幕邊緣到棋盤的線條邊緣也是 1 個 UNIT_LENGTH"
    # 所以對於棋盤座標中 (x,y) 的點 他在螢幕座標的點就會是 (UNIT_LENGTH*(x+1) , UNIT_LENGTH*(y+1))
    #--------------------------------------------------------------#

#--------------------<Main>---------------------
def main() -> None:
    running = True
    while running:
        clock.tick(FPS)
        #取得輸入input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #更新遊戲update
        #畫面顯示render
        draw_background(win)
        pygame.display.update()

#---------------------<     >---------------------
if(__name__ == "__main__"):
    pygame.init()
    main()
    pygame.quit()

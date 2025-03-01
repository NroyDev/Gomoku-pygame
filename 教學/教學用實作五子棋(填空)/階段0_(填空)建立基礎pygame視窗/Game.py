import pygame
from Setting import *

#
#   按住 CTRL + F 搜尋 ___請填空___
#

#---------------------<初始設定>---------------------
#========>物件<========
#Clock
clock = pygame.time.___請填空___()
#Screen
win = pygame.display.set_mode((WIN_WIDTH_HEIGHT,WIN_WIDTH_HEIGHT))    #Build a screen  
pygame.display.___請填空___("五子棋")  #Screen Title

#--------------------<Main>---------------------
def main() -> None:
    running = True
    while running:
        clock.tick(FPS) #畫面更新頻率
        #取得輸入input
        for event in pygame.event.get():
            if event.type == pygame.___請填空___:   #若是關閉按鈕
                running = False
        #更新遊戲update
        #畫面顯示render
        pygame.display.___請填空___() #Update Screen

#---------------------<     >---------------------
if(__name__ == "__main__"):
    pygame.init()
    main()
    pygame.quit()

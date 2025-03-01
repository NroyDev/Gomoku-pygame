from Setting import UNIT_LENGTH,WAY
import pygame
import os

#
#   按住 CTRL + F 搜尋 ___請填空___
#


pygame.mixer.init()
put_sound = pygame.mixer.Sound(os.path.join("sound" , "put.wav"))
class Pieces(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int,type:int) -> None:
        """
        type=1 =>Black    /    type=2 =>White
        xy: 在棋盤上的座標
        """
        super().__init__()
        white_img = pygame.image.load(os.path.join("img","White.png")).convert_alpha()
        white_img = pygame.transform.scale(white_img,(UNIT_LENGTH,UNIT_LENGTH))
        black_img = pygame.image.load(os.path.join("img","Black.png")).convert_alpha()
        black_img = pygame.transform.scale(black_img,(UNIT_LENGTH,UNIT_LENGTH))
        self.type = type
        if type == 1:
            self.image = black_img
        elif type == 2:
            self.image = white_img
        self.rect = self.image.get_rect()
        self.rect.topleft = ((x+1-0.5)*UNIT_LENGTH,(y+1-0.5)*UNIT_LENGTH)

class PiecesGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__() 
        self.winner = 0 
        self.turn = 1
        self.lastmove = (-1,-1) #存上一步的位置

        self.map = []
        for i in range(WAY):
            temp = []
            for j in range(WAY):
                temp.append(0)
            self.map.append(temp)

    def draw(self,surface:pygame.surface.Surface) -> None:
        """
        畫出棋子
        畫出上一步 棋子被下下的位置
        """
        pygame.sprite.Group.draw(self,surface)  #繼承
        if(self.lastmove != (-1,-1)):   #確定動過了
            #1 is Black, 2 is White
            color = (255,0,0)
            x ,y = self.lastmove
            scale = 1.1
            rect = (round((x+1-scale/2)*UNIT_LENGTH),round((y+1-scale/2)*UNIT_LENGTH),UNIT_LENGTH*scale,UNIT_LENGTH*scale)
            pygame.___請填空___.___請填空___(surface,color,rect,width=1)    #畫出紅框框

    def check(self,x:int,y:int) -> bool:
        """
        回傳該位置可否放置
        """
        if self.map[x][y] == 0:
            return True
        else:
            return False
        
    def judge(self,x:int,y:int) -> None:
        #橫線判斷
        count = 0
        for i in range(1,4+1):#1~4  #往左判斷
            if(x-i>=0):
                if(self.map[x-i][y] == self.turn):
                    count += 1
                else:
                    break
            else:
                break
        for i in range(1,4+1):#1~4  #往右判斷
            if(x+i<WAY):
                if(self.map[x+i][y] == self.turn):
                    count += 1
                else:
                    break
            else:
                break
        if count >= 4:  #不包括自己
            self.winner = self.turn
            return

        #直線判斷
        count = 0
        for i in range(1,4+1):#1~4  #往上判斷
            if(y-i>=0):
                if(self.map[x][y-i] == self.turn):
                    count += 1
                else:
                    break
            else:
                break
        for i in range(1,4+1):#1~4  #往下判斷
            if(y+i<WAY):
                if(self.map[x][y+i] == self.turn):
                    count += 1
                else:
                    break
            else:
                break
        if count >= 4:  #不包括自己
            self.winner = self.turn
            return
        
        #左上右下判斷
        count = 0
        for i in range(1,4+1):#1~4  #往左上判斷
            if(x-i>=0 and y-i>=0):
                if(self.map[x-i][y-i] == self.turn):
                    count +=1
                else:
                    break
            else:
                break
        for i in range(1,4+1):#1~4  #往右下判斷
            if(x+i<WAY and y+i<WAY):
                if(self.map[x+i][y+i] == self.turn):
                    count +=1
                else:
                    break
            else:
                break
        if count >= 4:  #不包括自己
            self.winner = self.turn
            return
        
        
        #左下右上判斷
        count = 0
        for i in range(1,4+1):#1~4  #往左下判斷
            if(x-i>=0 and y+i<WAY):
                if(self.map[x-i][y+i] == self.turn):
                    count +=1
                else:
                    break
            else:
                break
        for i in range(1,4+1):#1~4  #往右上判斷
            if(x+i<WAY and y-i>=0):
                if(self.map[x+i][y-i] == self.turn):
                    count +=1
                else:
                    break
            else:
                break
        if count >= 4:  #不包括自己
            self.winner = self.turn
            return
        
    def move(self,x:int,y:int) -> bool:
        """
        xy: 在棋盤上的座標
        回傳False代表失敗 回傳True成功
        """
        if((x>=0) and (x<WAY) and (y>=0) and (y<WAY)): 
            if self.check(x,y) == True: 
                new_piece = Pieces(x,y,self.turn)
                self.add(new_piece)
                self.map[x][y] = self.turn

                self.lastmove = (x,y)   #更新上一步
                self.judge(x,y) #判斷勝負
                put_sound.___請填空___()    #播放聲音
                if self.turn == 1:  #換人下
                    self.turn = 2
                else:
                    self.turn = 1
                return True       
            else:
                return False       
        else:
            print("3")
            return False         


from GameSetting import UNIT_LENGTH,WAY
import pygame

class Pieces(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int,type:int) -> None:
        """
        type=1 =>Black    /    type=2 =>White
        xy: 在棋盤上的座標
        """
        pygame.sprite.Sprite.__init__(self) #init
        #black and white
        white_img = pygame.image.load(".\\img\\White.png").convert_alpha()
        white_img = pygame.transform.scale(white_img,(UNIT_LENGTH,UNIT_LENGTH)) #縮放
        black_img = pygame.image.load(".\\img\\Black.png").convert_alpha()
        black_img = pygame.transform.scale(black_img,(UNIT_LENGTH,UNIT_LENGTH)) #縮放
        self.type = type
        #img
        if type == 1:   #Black
            self.image = black_img
        elif type == 2: #White
            self.image = white_img
        #rect
        self.rect = self.image.get_rect()
        self.rect.center = ((x+1)*UNIT_LENGTH,(y+1)*UNIT_LENGTH)

class PiecesGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        pygame.sprite.Group.__init__(self)  #init
        self.winner = 0 #贏家
        self.turn = 1   #黑棋先下

        self.pieceslist = []
        self.map = []
        for i in range(WAY):
            temp = []
            for j in range(WAY):
                temp.append(0)
            self.map.append(temp)
    
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
        if((x>=0) and (x<WAY) and (y>=0) and (y<WAY)):  #確認正確
            if self.check(x,y) == True: #可放置
                new_piece = Pieces(x,y,self.turn)
                self.add(new_piece)
                self.pieceslist.append(new_piece)
                self.map[x][y] = self.turn

                self.judge(x,y) #判斷勝負

                if self.turn == 1:  #換人下
                    self.turn = 2
                else:
                    self.turn = 1
                return True
            else:
                return False
        else:
            return False
        
    
from Setting import UNIT_LENGTH,WAY
import pygame
import os

class Pieces(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int,type:int) -> None:
        """
        type=1 =>Black    /    type=2 =>White
        xy: 在棋盤上的座標
        """
        super().__init__() #init
        #black and white
        white_img = pygame.image.load(os.path.join("img","White.png")).convert_alpha()
        white_img = pygame.transform.scale(white_img,(UNIT_LENGTH,UNIT_LENGTH)) #縮放
        black_img = pygame.image.load(os.path.join("img","Black.png")).convert_alpha()
        black_img = pygame.transform.scale(black_img,(UNIT_LENGTH,UNIT_LENGTH)) #縮放 
        self.type = type        #註:到時候，這個type會從在建立物件時，我們給予的參數得到
        #img                    #註:我們設定type是1 就是黑子，type是2 就是白子，在往後的例子中type的規則就是這樣!
        if type == 1:   #Black          
            self.image = black_img
        elif type == 2: #White
            self.image = white_img
        #rect
        self.rect = self.image.get_rect()   #註:這步有點類似去設定我們sprite在螢幕中的大小，將其設定為圖片大小
        self.rect.topleft = ((x+1-0.5)*UNIT_LENGTH,(y+1-0.5)*UNIT_LENGTH)

class PiecesGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()  #init
        self.winner = 0 #贏家 初始化為0代表沒有贏家
        self.turn = 1   #黑棋先下

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
        
    def move(self,x:int,y:int) -> bool:
        """
        xy: 在棋盤上的座標
        回傳False代表失敗 回傳True成功
        """
        if((x>=0) and (x<WAY) and (y>=0) and (y<WAY)):  #確認正確(是否超出邊界)
            if self.check(x,y) == True: #可放置
                new_piece = Pieces(x,y,self.turn)
                self.add(new_piece)
                self.map[x][y] = self.turn

                if self.turn == 1:  #換人下
                    self.turn = 2
                else:
                    self.turn = 1
                return True         #成功放置=>回傳True
            else:
                return False        #想放置在已放置過的位置=>回傳False
        else:
            print("3")
            return False            #超出邊界=>回傳False


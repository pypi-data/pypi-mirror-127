import pygame
import time
import random
"""
明白需求
1.有哪些类 2.不同的类别所具备的一些功能
    1.主逻辑类
        开始游戏
        结束游戏
    2.坦克类（1.我方坦克 2.敌方坦克）
        移动
        射击
        展示坦克
    3.子弹类
        移动
        展示子弹
    4.爆炸效果类
        展示爆炸效果
    5.墙壁类
        属性：是否可以通过
    6.音效类
        播放音乐
"""
"""
事件处理：
    点击关闭按钮，退出程序的事件
    方向控制，子弹发射
"""

"""
新增功能：
    实现左上角问题提示内容
"""

"""
新增功能：
    加载我方坦克
"""

"""
新增功能：
    1.坦克类新增speed属性，用来控制坦克移动快慢
    2.事件处理：
        改变坦克方向
        修改坦克的位置
            取决于坦克的速度
"""

"""
优化功能：
    bug:坦克能够移除边界
"""

"""
优化功能：
    优化坦克移动方式：
        1.按下方向键，坦克持续移动
        2.松开方向键，坦克停下来
"""

"""
新增功能：
    新增敌方坦克
        1.完善敌方坦克类
        2.创建敌方坦克，将敌方坦克展示到窗口中
"""

"""
优化功能：
    1.优化坦克剩余数量提示：
    2.实现敌方坦克的移动
        随机移动（在某一个方向移动一定距离的啥时候，随机更改移动方向）
"""
"""
新增功能：完善子弹类的封装
"""
"""
新增功能：完善子弹类的发射功能
        tank 发射子弹->产生一颗子弹
"""
"""
新增功能：实现子弹的移动
"""
"""
优化功能：
        1.子弹碰撞到墙壁的时候，直接消除，而不是粘在墙上
        2.解决我方坦克可以无限发射子弹的问题（最多3发子弹）
"""
"""
新增功能：
        让敌方坦克可以发射子弹
"""
"""
新增功能：
        实现我方子弹与敌方坦克的碰撞
        使用精灵类中的碰撞
            使用Bullet,Tank继承精灵类
"""
"""
新增功能：
        1.完成爆炸效果的实现
        2.在窗口中展示爆炸效果
"""
"""
新增功能：
        1.敌方子弹与我方坦克的碰撞
        2.我方坦克爆炸效果的实现
"""
"""
新增功能：
        1.死亡之后点击ESC按键重生
"""
"""
新增功能：
        1.实现墙壁类
        2.将随机创建的墙壁对象，加入到窗口中
        创建墙壁对象，加入到墙壁列表中
"""
"""
新增功能：
        1.实现子弹不可以穿墙
"""
"""
新增功能：
        1.实现坦克与墙壁的碰撞检测（坦克不能撞墙）
"""
"""
新增功能：
        1.实现坦克之间的碰撞检测
            1.1我方坦克主动碰撞到敌方坦克
                我方坦克停下来stay()
            1.2敌方坦克主动碰撞到我方坦克
                敌方坦克要停下来stay()
"""
class MainGame():
    #游戏主窗口
    window=None
    Screen_width=1200
    Screen_height=800
    #创建我方坦克
    TANK_P1=None
    #存储所有敌方坦克
    EnemyTank_list=[]
    #要创建的地方坦克数量
    EnemyTank_count=5
    #存储我方子弹的列表
    Bullet_list=[]
    #存储敌方子弹的列表
    Enemy_bullet_list=[]
    #爆炸效果列表
    Explode_List=[]
    #墙壁列表
    wall_list=[]
    #开始游戏方法
    def StartGame(self):
        pygame.display.init()
        #创建窗口加载窗口
        MainGame.window=pygame.display.set_mode([MainGame.Screen_width,MainGame.Screen_height])
        #创建我方坦克方法
        self.creatMyTank()
        #创建敌方坦克
        self.creatEnemyTank()
        self.creatWalls()
        #设置一下游戏标题
        pygame.display.set_caption("坦克大战")
        while True:
            #给窗口完成一个填充颜色
            MainGame.window.fill(pygame.Color(0,0,0))
            #再循环中持续完成事件的获取
            self.getEvent()
            #将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆"%len(MainGame.EnemyTank_list)),(5,5))
            #调用展示墙壁的方法
            self.blitWalls()
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                #将我方坦克加入到窗口中
                MainGame.TANK_P1.displayTank()
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1=None
            #循环展示敌方坦克
            self.blitEnemyTank()
            #根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                #调用碰撞墙壁的方法
                MainGame.TANK_P1.hitWalls()
                #调用碰撞敌方坦克的方法
                MainGame.TANK_P1.hitEnemyTank()
            time.sleep(0.02)
            # self.getTextSurface()
            #调用渲染子弹列表的一个方法
            self.blitBullet()
            #调用渲染敌方子弹列表的一个方法
            self.blitEnemyBullet()
            #调用显示爆炸效果的方法
            self.displayExplodes()
            #窗口的刷新
            pygame.display.update()
    #创建我方坦克方法
    def creatMyTank(self):
        MainGame.TANK_P1 = MyTank(500, 600)
        #创建音乐对象
        # music=Music('img/start.wav')
        # #调用播放音乐的方法
        # music.play()
    #创建敌方坦克
    def creatEnemyTank(self):
        top=100
        for i in range(MainGame.EnemyTank_count):
            speed = random.randint(3, 6)
            left = random.randint(1, 7)
            eTank=EnemyTank(left*100,top,speed)
            MainGame.EnemyTank_list.append(eTank)
    #创建墙壁的方法
    def creatWalls(self):
        for i in range(1,6):
            wall=Wall(190*i,400)
            MainGame.wall_list.append(wall)
    def blitWalls(self):
        for wall in MainGame.wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.wall_list.remove(wall)
    #将敌方坦克加入到窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayTank()
                #调用坦克的移动方法
                eTank.randMove()
                #调用敌方坦克与墙壁的碰撞方法
                eTank.hitWalls()
                #敌方坦克是否撞到我方坦克
                eTank.hitMyTank()
                #调用敌方坦克的射击
                eBullet=eTank.shot()
                #如果子弹为None，不加入到列表
                if eBullet:
                    #将子弹存储敌方子弹列表
                    MainGame.Enemy_bullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)
    #将我方子弹加入到窗口中
    def blitBullet(self):
        for Bullet in MainGame.Bullet_list:
            #如果子弹还活着，绘制出来，否则，直接从列表中移除该子弹
            if Bullet.live:
                Bullet.displayBullet()
                #让子弹移动
                Bullet.bulletMove()
                #调用我方子弹与敌方坦克的碰撞方法
                Bullet.hitEnemyTank()
                #调用判断我方子弹是否碰撞到墙壁的方法
                Bullet.hitWalls()
            else:
                MainGame.Bullet_list.remove(Bullet)
    # 将敌方子弹加入到窗口中
    def blitEnemyBullet(self):
        for eBullet in MainGame.Enemy_bullet_list:
            # 如果子弹还活着，绘制出来，否则，直接从列表中移除该子弹
            if eBullet.live:
                eBullet.displayBullet()
                #调用是否碰撞到墙壁的方法
                eBullet.hitWalls()
                # 让子弹移动
                eBullet.bulletMove()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    eBullet.hitMyTank()
            else:
                MainGame.Enemy_bullet_list.remove(eBullet)
    #新增方法：展示爆炸效果列表
    def displayExplodes(self):
        for explode in MainGame.Explode_List:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_List.remove(explode)
    #获取程序期间所有事件（鼠标事件、键盘事件）
    def getEvent(self):
        #1.获取所有事件
        eventList=pygame.event.get()
        #2.对事件进行判断处理（1.点击关闭按钮2.按下键盘上的某个按键）
        for event in eventList:
            #判断event.type是否退出，如果退出的话，直接调用程序结束方法
            if event.type==pygame.QUIT:
                self.EndGame()
            #判断事件类型是否为按键按下，如果是，继续判断按键是哪一个按键，来进行对应的处理
            if event.type==pygame.KEYDOWN:
                #点击ESC按键，让我方坦克重生
                if event.key==pygame.K_ESCAPE and not MainGame.TANK_P1:
                    #调用创建我方坦克的方法
                    self.creatMyTank()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    #具体是哪一个按键的处理
                    if event.key==pygame.K_LEFT:
                        print("坦克向左调头，移动")
                        #修改坦克方向
                        MainGame.TANK_P1.direction='L'
                        # MainGame.TANK_P1.move()
                        MainGame.TANK_P1.stop=False
                    elif event.key == pygame.K_RIGHT:
                        print("坦克向右调头，移动")
                        MainGame.TANK_P1.direction='R'
                        # MainGame.TANK_P1.move()
                        MainGame.TANK_P1.stop=False
                    elif event.key == pygame.K_UP:
                        print("坦克向上调头，移动")
                        MainGame.TANK_P1.direction='U'
                        # MainGame.TANK_P1.move()
                        MainGame.TANK_P1.stop=False
                    elif event.key == pygame.K_DOWN:
                        print("坦克向下调头，移动")
                        MainGame.TANK_P1.direction='D'
                        # MainGame.TANK_P1.move()
                        MainGame.TANK_P1.stop=False
                    elif event.key == pygame.K_SPACE:
                        print("发射子弹")
                        if len(MainGame.Bullet_list)<3:
                            #产生一颗子弹
                            m=Bullet(MainGame.TANK_P1)
                            #将子弹加入到子弹列表
                            MainGame.Bullet_list.append(m)
                            # music=Music('img/fire.wav')
                            # music.play()
                        else:
                            print("子弹数量不足")
                        print("当前屏幕中的子弹数量为：%d"%len(MainGame.Bullet_list))
            #结束游戏方法
            if event.type==pygame.KEYUP:
                #松开的如果是方向键，才更改移动开关状态
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                        #修改坦克的移动状态
                        MainGame.TANK_P1.stop=True
    #左上角文字绘制的功能
    def getTextSurface(self,text):
        #初始化字体模块
        pygame.font.init()

        #查看系统支持的所有字体
        # fontlist=pygame.font.get_fonts()
        # print(fontlist)
        # 选中一个合适的字体
        font=pygame.font.SysFont('华文宋体',18)
        #使用对应的字符完成相关内容的绘制
        textSurface=font.render(text,True,pygame.Color(255,0,0))
        return textSurface
    def EndGame(self):
        print("谢谢，再见")
        #结束python解释器
        exit()
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Tank(BaseItem):
    def __init__(self,left,top):
        self.images={
            'U':pygame.image.load('img/MyTankU.jpg'),
            'D':pygame.image.load('img/MyTankD.jpg'),
            'L':pygame.image.load('img/MyTankL.jpg'),
            'R':pygame.image.load('img/MyTankR.jpg')
        }
        self.direction='U'
        self.image=self.images[self.direction]
        #坦克所在的区域 Rect->
        self.rect=self.image.get_rect()
        #指定坦克初始化位置，分别距x、y轴的位置
        self.rect.left=left
        self.rect.top=top
        #新增速度属性
        self.speed=5
        #新增属性：坦克的移动开关
        self.stop=True
        self.live=True
        #新增属性：用来记录坦克移动之前的坐标（用于坐标还原时使用）
        self.oldLeft=self.rect.left
        self.oldTop=self.rect.top
    def move(self):
        #先记录移动之前的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        if self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
        elif self.direction=='R':
            if self.rect.left<MainGame.Screen_width-self.rect.width:
                self.rect.left+=self.speed
        elif self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
        elif self.direction=='D':
            if self.rect.top<MainGame.Screen_height-self.rect.height:
                self.rect.top+=self.speed
    def stay(self):
        self.rect.left=self.oldLeft
        self.rect.top=self.oldTop
    #新增碰撞墙壁的方法
    def hitWalls(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.stay()
    def shot(self):
        return Bullet(self)
    #展示坦克（将坦克这个surface绘制到窗口中，blit()）
    def displayTank(self):
        #1.重新设置坦克的图像
        self.image=self.images[self.direction]
        #2.将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)
    #新增主动碰撞到敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank,self):
                self.stay()
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        super(EnemyTank,self).__init__(left,top)
        #图片集
        self.images={
            'U':pygame.image.load('img/enemyU.png'),
            'D':pygame.image.load('img/enemyD.jpg'),
            'L':pygame.image.load('img/enemyL.png'),
            'R':pygame.image.load('img/enemyR.png')
        }
        self.direction=self.randDirection()
        self.image=self.images[self.direction]
        #坦克所在的区域 Rect->
        self.rect=self.image.get_rect()
        #指定坦克初始化位置，分别距x、y轴的位置
        self.rect.left=left
        self.rect.top=top
        #新增速度属性
        self.speed=speed
        #新增属性：坦克的移动开关
        self.stop=True
        #新增步数属性，用来控制敌方坦克随机移动
        self.step=50
        #新增属性 live 用来记录，坦克是否活着
        self.live=True
    def randDirection(self):
        num=random.randint(1,4)
        if num==1:
            return 'U'
        elif num==2:
            return 'D'
        elif num==3:
            return 'L'
        elif num==4:
            return 'R'
    def randMove(self):
        if self.step==0:
            self.direction=self.randDirection()
            self.step=50
        else:
            self.move()
            self.step-=1
    def shot(self):
        num=random.randint(1,1000)
        if num<=18:
            return Bullet(self)
    def hitMyTank(self):
        if MainGame.TANK_P1 and MainGame.TANK_P1.live:
            if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
                #让敌方坦克停下来
                self.stay()
class Bullet(BaseItem):
    def __init__(self,tank):
        #图片
        self.image=pygame.image.load('img/bullet.png')
        #方向
        self.direction=tank.direction
        #位置
        self.rect=self.image.get_rect()
        if self.direction=='U':
            self.rect.left=tank.rect.left+tank.rect.width/2-self.rect.width/2
            self.rect.top=tank.rect.top-self.rect.height
        elif self.direction=='D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction=='L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top+tank.rect.width/2 - self.rect.width/2
        elif self.direction=='R':
            self.rect.left=tank.rect.left+tank.rect.width
            self.rect.top=tank.rect.top+tank.rect.width/2-self.rect.width/2
        #速度
        self.speed=7
        #用来记录子弹是否碰撞
        self.live=True
    #子弹的移动方法
    def bulletMove(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                #修改状态值
                self.live=False
        elif self.direction == 'R':
            if self.rect.left < MainGame.Screen_width - self.rect.width:
                self.rect.left += self.speed
            else:
                self.live=False
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live=False
        elif self.direction == 'D':
            if self.rect.top < MainGame.Screen_height - self.rect.height:
                self.rect.top += self.speed
            else:
                self.live=False
    #显示子弹的方法
    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)
    #新增我方子弹碰撞敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank,self):
                #产生一个爆炸效果
                explode=Explode(eTank)
                #将爆炸效果加入到爆炸效果列表
                MainGame.Explode_List.append(explode)
                self.live = False
                eTank.live = False
    # 新增敌方子弹碰撞我方坦克的方法
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
            #产生爆炸效果，并加入到爆炸效果列表中
            explode=Explode(MainGame.TANK_P1)
            MainGame.Explode_List.append(explode)
            #修改子弹状态
            self.live=False
            #修改我方坦克状态
            MainGame.TANK_P1.live=False
    #新增子弹与墙壁的碰撞
    def hitWalls(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(wall,self):
                #修改子弹的属性
                self.live=False
                wall.hp-=1
                if wall.hp<=0:
                    wall.live=False
class Explode():
    def __init__(self,tank):
        self.rect=tank.rect
        self.step=0
        self.images=[
            pygame.image.load('img/explode1.jpg'),
            pygame.image.load('img/explode2.jpg'),
            pygame.image.load('img/explode3.jpg'),
            pygame.image.load('img/explode4.jpg')
        ]
        self.image=self.images[self.step]
        self.live=True
    #显示爆炸效果
    def displayExplode(self):
        if self.step<len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step+=1
        else:
            self.live=False
            self.step=0
class Wall():
    def __init__(self,left,top):
        self.image=pygame.image.load('img/steels.png')
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        #用来判断墙壁是否应该在窗口中显示
        self.live=True
        #用来记录墙壁的生命值
        self.hp=3
    #展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)
class Music():
    def __init__(self,fileName):
        self.fileName=fileName
        #先初始化混音器
        pygame.mixer.init()
        pygame.mixer.music.load(self.fileName)
    def play(self):
        pygame.mixer.music.play()
p = MainGame()
p.StartGame()
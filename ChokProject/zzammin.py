from select import select
import pygame
import time
import sys
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK =(0, 0, 0)

# 콘솔 창
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 시작 화면 이미지
background_img = pygame.image.load("이미지/backgroundimg.png")
start_img = pygame.image.load("이미지/startimg.png")

# com 이미지
com1=pygame.image.load("이미지/c1.png")
com1=pygame.transform.scale(com1,(120,120))
com2=pygame.image.load("이미지/c2.png")
com2=pygame.transform.scale(com2,(120,120))
com3=pygame.image.load("이미지/c3.png")
com3=pygame.transform.scale(com3,(120,120))

# 잔 고르기 이미지
water=pygame.image.load("이미지/water.jpg")
water=pygame.transform.scale(water,(150,150))
juice=pygame.image.load("이미지/juice.jpg")
juice=pygame.transform.scale(juice,(150,150))
beer=pygame.image.load("이미지/beer.png")
beer=pygame.transform.scale(beer,(150,150))
soju=pygame.image.load("이미지/soju.jpg")
soju=pygame.transform.scale(soju,(150,150))

# 테이블 이미지
table_image = pygame.image.load("이미지/table.jpg")
table_image = pygame.transform.scale(table_image,(screen_width, screen_height)) # 테이블 배경용

# 테이블에서의 행동들에 대한 버튼
move= pygame.image.load("이미지/move.png") # 다른 장소로 이동 이미지
move=pygame.transform.scale(move,(120,150))
food = pygame.image.load("이미지/food.jpg") # 안주 먹기 이미지
food=pygame.transform.scale(food,(150,150))
cheers=pygame.image.load("이미지/cheers.png") # 짠(건배) 이미지
cheers=pygame.transform.scale(cheers,(150,150))
close2=pygame.image.load("이미지/close2.png") # 안하기 버튼 이미지
close2=pygame.transform.scale(close2,(120,120))

# 테이블 행동(다른 장소로 이동)에 대한 버튼
toilet=pygame.image.load("이미지/toilet.jpg") # 화장실 이미지
toilet=pygame.transform.scale(toilet,(150,150))
store=pygame.image.load("이미지/store.png") # 편의점 이미지
store=pygame.transform.scale(store,(150,150))
close=pygame.image.load("이미지/close.png") # 편의점 한 번 가고 난 다음 또 가는 것 금지
close=pygame.transform.scale(close,(150,150))
smoking=pygame.image.load("이미지/smoking.png") # 흡연장 이미지
smoking=pygame.transform.scale(smoking,(150,150))
table_b=pygame.transform.scale(table_image,(150,150)) # 테이블 버튼용

# 편의점에서의 행동들에 대한 버튼
table_button=pygame.transform.scale(table_image,(150,150)) # 테이블 버튼용
ice=pygame.image.load("이미지/ice.jpg") # 아이스크림 이미지
ice=pygame.transform.scale(ice,(150,150))
condition=pygame.image.load("이미지/condition.jpg") # 상쾌환 이미지
condition=pygame.transform.scale(condition,(150,150))

# 쓰이는 폰트들
font=pygame.font.Font("이미지/양진체v0.9_ttf.ttf", 80) # 장소 이름을 위한 폰트
font2=pygame.font.Font("이미지/양진체v0.9_ttf.ttf", 50) # 안내문을 위한 폰트
font3=pygame.font.Font("이미지/양진체v0.9_ttf.ttf", 25) # 안내문을 위한 폰트 2

# 게임에서 쓸 변수들
turn = 1  # 턴 수
chance = 0  # 랜덤 이벤트 발생할때 쓸 변수

select_size = start_img.get_rect().size
w = select_size[0]
h = select_size[1]

clock = pygame.time.Clock()

# 글씨쓰기
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# 플레이어 정보 및 체력
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((0,0))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (0,0))
        #full
        self.current_full = 20
        self.target_full = 50
        self.max_full = 100
        self.full_bar_length = 200
        self.full_ratio = self.max_full / self.full_bar_length
        #drunk
        self.current_drunk = 20
        self.target_drunk = 50
        self.max_drunk = 100
        self.drunk_bar_length = 200
        self.drunk_ratio = self.max_drunk / self.drunk_bar_length
        
        self.health_change_speed = 5 #고정

    def get_full_down(self,amount): #full 하락
        if self.target_full > 0:
            self.target_full -= amount
        if self.target_full < 0:
            self.target_full = 0

    def get_full_up(self,amount): #full 상승
        if self.target_full < self.max_full:
            self.target_full += amount
        if self.target_full > self.max_full:
            self.target_full = self.max_full

    def get_drunk_down(self,amount): #drunk 하락
        if self.target_drunk > 0:
            self.target_drunk -= amount
        if self.target_drunk < 0:
            self.target_drunk = 0

    def get_drunk_up(self,amount): #drunk 상승
        if self.target_drunk < self.max_drunk:
            self.target_drunk += amount
        if self.target_drunk > self.max_drunk:
            self.target_drunk = self.max_drunk    

    def update(self):
        self.alcohol()
        self.full()
		
    def alcohol(self):
        transition_width = 0
        transition_color = (255,0,0)
        if self.current_drunk < self.target_drunk:
            self.current_drunk += self.health_change_speed
            transition_width = int((self.target_drunk - self.current_drunk) / self.drunk_ratio)
            transition_color = (0,255,0)

        if self.current_drunk > self.target_drunk:
            self.current_drunk -= self.health_change_speed 
            transition_width = int((self.target_drunk - self.current_drunk) / self.drunk_ratio)
            transition_color = (255,255,0)

        health_bar_width = int(self.current_drunk / self.drunk_ratio)
        health_bar = pygame.Rect(70,15,health_bar_width,25)
        transition_bar = pygame.Rect(health_bar.right,15,transition_width,25)
        draw_text('Drunk', 30, WHITE, 30, 18)
        pygame.draw.rect(screen,(255,0,0),health_bar)
        pygame.draw.rect(screen,transition_color,transition_bar)
        pygame.draw.rect(screen,(255,255,255),(70,15,self.drunk_bar_length,25),4)

    def full(self):
        transition_width = 0
        transition_color = (255,0,0)

        if self.current_full < self.target_full:
            self.current_full += self.health_change_speed
            transition_width = int((self.target_full - self.current_full) / self.full_ratio)
            transition_color = (0,255,0)

        if self.current_full > self.target_full:
            self.current_full -= self.health_change_speed 
            transition_width = int((self.target_full - self.current_full) / self.full_ratio)
            transition_color = (255,255,0)
        

        health_bar_width = int(self.current_full / self.full_ratio)
        health_bar = pygame.Rect(70,45,health_bar_width,25)
        transition_bar = pygame.Rect(health_bar.right,45,transition_width,25)
        draw_text('Full', 30, WHITE, 30,50)
        pygame.draw.rect(screen,(255,0,0),health_bar)
        pygame.draw.rect(screen,transition_color,transition_bar)	
        pygame.draw.rect(screen,(255,255,255),(70,45,self.full_bar_length,25),4)

# 플레이어 변수 선언
p = pygame.sprite.GroupSingle(Player())

# 버튼
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.bigimage = pygame.transform.scale(image, (int(w*1.5),int(h*1.5)))
        self.tempimage = image

    def draw(self):
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos): # self.rect 즉 버튼크기의 좌표 위로 마우스 좌표가 겹쳐지면
            self.image = self.bigimage # 마우스가 버튼위로 올라왔을때 빅 이미지로 바꾸며 버튼이 커지는 이펙트 부여

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # 0은 좌클릭 , 1은 휭클릭 2는 우클릭
                self.clicked = True
                action = True # 눌리면 트루값 반납
                pygame.time.delay(500) # 버튼 누르고 바로 다음 버튼 눌림을 방지하기 위한 딜레이

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False # 마우스를 떼는 순간 클릭은 거짓으로 바뀐다
        else:
            self.image = self.tempimage # 마우스 커서가 버튼 밖으로 나간다면 원래크기로 돌아간다

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

pygame.display.set_caption("술자리 시뮬레이션")   #이 줄 기점으로 위에는 기본 설정. 밑은 장소별 함수 입니다.

#시작화면
def mainmenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        screen.blit(background_img, (100, 90))
        start_button = Button(800, 500, start_img)

        if start_button.draw() == True:
            table()

        pygame.display.update()
        clock.tick(30)

# 컴퓨터들의 게이지
global com1_g
com1_g=0
global com2_g
com2_g=0
global com3_g
com3_g=0

# 짠에서 컴퓨터들이 마신 음료 여부 (True: 채워져 있음, False: 비워져 있음)
# com1 여부
global com1_water
com1_water=True
global com1_juice
com1_juice=True
global com1_beer
com1_beer=True
global com1_soju
com1_soju=True
# com2 여부
global com2_water
com2_water=True
global com2_juice
com2_juice=True
global com2_beer
com2_beer=True
global com2_soju
com2_soju=True
# com3 여부
global com3_water
com3_water=True
global com3_juice
com3_juice=True
global com3_beer
com3_beer=True
global com3_soju
com3_soju=True

# 짠할 때 com들에게 미치는 영향
def computer(com_num):
    global com1_water
    global com1_juice
    global com1_beer
    global com1_soju

    global com2_water
    global com2_juice
    global com2_beer
    global com2_soju

    global com3_water
    global com3_juice
    global com3_beer
    global com3_soju

    global com1_g
    global com2_g
    global com3_g

    # 난수 생성 (짠할 때 각각의 com들이 마실 음료들)
    num=random.randrange(1,4)
    # com1 일 때
    if com_num==1:
        if num==1: # num==1 은 물
            com1_g=com1_g-2
            com1_water=False
        elif num==2: # num==2 는 주스
            com1_g=com1_g-1
            com1_juice=False
        elif num==3: # num==3 은 맥주
            com1_g=com1_g+1
            com1_beer=False
        elif num==4: # num==4 는 소주
            com1_g=com1_g+2
            com1_soju=False
    # com2 일 때
    elif com_num==2: # com1 일 때
        if num==1: # num==1 은 물
            com2_g=com2_g-2
            com2_water=False
        elif num==2: # num==2 는 주스
            com2_g=com2_g-1
            com2_juice=False
        elif num==3: # num==3 은 맥주
            com2_g=com2_g+1
            com2_beer=False
        elif num==4: # num==4 는 소주
            com2_g=com2_g+2
            com2_soju=False
    # com3 일 때
    elif com_num==3:
        if num==1: # num==1 은 물
            com3_g=com3_g-2
            com3_water=False
        elif num==2: # num==2 는 주스
            com3_g=com3_g-1
            com3_juice=False
        elif num==3: # num==3 은 맥주
            com3_g=com3_g+1
            com3_beer=False
        elif num==4: # num==4 는 소주
            com3_g=com3_g+2
            com3_soju=False

    pygame.display.update()
    clock.tick(30)

# 테이블 버튼
move_b = Button(150, screen_height-230, move)
food_b = Button(460, screen_height-230, food)
cheers_b = Button(screen_width-280, screen_height-230, cheers)

# 포만도가 다 차있는지 판단
global food_max
food_max=False

# 테이블 함수
def table():
    global food_max
    pygame.display.set_caption("테이블")
    place_table = font.render("테이블", True,  WHITE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        screen.blit(table_image, (0, 0))
        screen.blit(place_table, (screen_width-260,30))
        
        table_mv=font3.render("다른 장소로 가기",True,WHITE)
        screen.blit(table_mv, (130,screen_height-60))

        table_fd=font3.render("안주 먹기",True,WHITE)
        screen.blit(table_fd, (490,screen_height-60))

        table_ch=font3.render("짠",True,WHITE)
        screen.blit(table_ch, (screen_width-220,screen_height-60))

        p.draw(screen)
        p.update()

        # 다른 장소 가기
        if move_b.draw():
            print("다른 장소로 갑니다")
            at_table(1) # 다른 장소로 가는 화면 전환

        # 포만도가 다 차면 안주 못먹음
        if p.sprite.target_full==p.sprite.max_full:
            food_max=True

        # 안주 먹기
        if food_b.draw():
            if food_max==False: # 포만도가 다 안차있으면 실행
                print("안주를 먹습니다") # 안주 먹기(취기 - 포만도 ++ )
                p.sprite.get_drunk_down(10)
                p.sprite.get_full_up(30)
                at_table(2) # 안주를 먹는 화면 전환
        
        # 짠
        if cheers_b.draw():
            print("짠")
            at_table(3) # 짠(건배) 화면 전환

        pygame.display.update()
        clock.tick(30)
    pygame.display.update()

# 테이블 전용 화면 전환 버튼
table_b=Button(screen_width/2-60,400,table_b) # 테이블로 가는 버튼
toilet_b=Button(150, screen_height-230,toilet) # 화장실로 가는 버튼
store_b=Button(460, screen_height-230,store) # 편의점으로 가는 버튼
smoking_b=Button(screen_width-280, screen_height-230,smoking) # 흡연장으로 가는 버튼
close_st=Button(460, screen_height-230,close) # 편의점 또 못가는 걸 표시해줌

# 짠할 때 마실 음료 버튼
water_b=Button(90,screen_height-230,water)
juice_b=Button(335,screen_height-230,juice)
beer_b=Button(590,screen_height-230,beer)
soju_b=Button(840,screen_height-230,soju)

# 짠했을 때 마신 음료 판단
global water_full
water_bool=True
global juice_full
juice_full=True
global beer_full
beer_full=True
global soju_full
soju_full=True

# 편의점에 간 적이 있는지 판단
global try_store
try_store=False

# 테이블에서의 행동 함수
def at_table(click_number):
    global try_store # 여기서 False 를 해버리면 함수가 실행될 때마다 False가 되니까 밖에서 False라고 선언
    global water_full # 같은 이유
    global juice_full # 같은 이유
    global beer_full # 같은 이유
    global soju_full # 같은 이유

    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: # 아예 창이 닫혀야 함
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE) # 하얀색 배경
        
        # 다른 장소로 가는 버튼을 눌렀을 때
        if click_number==1: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() # 아예 창이 닫혀야 함

            text_s1 = font2.render("다른 장소로 갑니다...", True, (255,0,0))
            screen.blit(text_s1, (screen_width/2-200,180))

            # 화장실로 가는 버튼 부분
            text_t=font3.render("화장실",True,BLACK)
            screen.blit(text_t, (190,screen_height-60))
            toilet_b.draw()
            # if toilet_b.draw()
                # toilet_f 함수 실행

            # 편의점으로 가는 버튼 부분
            text_st=font3.render("편의점",True,BLACK)
            screen.blit(text_st, (500,screen_height-60))
            if store_b.draw() and try_store==False: # 편의점 버튼 눌렀을 때
                try_store=True # 편의점 한번 갔으니까 try_store를 True로 바꿈
                store_f() # 편의점 함수 실행
            if try_store==True:
                close_st.draw()

            # 흡연장으로 가는 버튼 부분
            text_sm=font3.render("흡연장",True,BLACK)
            screen.blit(text_sm, (screen_width-235,screen_height-60))
            smoking_b.draw()
            # if smoking_b.draw()
                # smoking_f 함수 실행
            pygame.display.update()

        # 안주를 먹는 버튼을 눌렀을 때
        if click_number==2: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() # 아예 창이 닫혀야 함

            text_s2 = font3.render("안주를 맛있게 먹습니다... 취기 하락,포만도 크게 증가", True, (255,0,0))
            screen.blit(text_s2, (screen_width/2-250,180))

            # 테이블로 가는 버튼 부분
            text_tb=font3.render("테이블로 돌아가기",True,BLACK)
            screen.blit(text_tb, (screen_width/2-75,screen_height-70))
            if table_b.draw(): # 테이블 버튼 누르면 돌아가자
                table()
            pygame.display.update()
        
        # 짠 버튼을 눌렀을 때
        if click_number==3:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() # 아예 창이 닫혀야 함

            text_s4 = font2.render("무슨 음료로 짠을 하시겠습니까?", True, (255,0,0))
            screen.blit(text_s4, (230,180))

            # 짠으로 마실 음료를 고르는 부분
            if water_b.draw(): # 물을 마실 때
                water_full=False
                check_glass()
            if juice_b.draw(): # 주스를 마실 때
                juice_full=False
                check_glass()
            if beer_b.draw(): # 맥주를 마실 때
                beer_full=False
                p.sprite.get_drunk_up(10)
                check_glass()
            if soju_b.draw(): # 소주를 마실 때
                soju_full=False
                p.sprite.get_drunk_up(20)
                check_glass()

            # com들이 마실 음료 정하기
            computer(1)
            computer(2)
            computer(3)

            # 음료 안내문
            water_f=font3.render("물",True,WHITE)
            screen.blit(water_f, (150,screen_height-60))
            juice_f=font3.render("주스",True,WHITE)
            screen.blit(juice_f, (390,screen_height-60))
            beer_f=font3.render("맥주",True,WHITE)
            screen.blit(beer_f, (640,screen_height-60))
            soju_f=font3.render("소주",True,WHITE)
            screen.blit(soju_f, (895,screen_height-60))

            pygame.display.update()

    pygame.display.update()

# com 버튼
com1_b=Button(90, screen_height-230,com1)
com2_b=Button(335, screen_height-230,com2)
com3_b=Button(590, screen_height-230,com3)
close_ch=Button(840, screen_height-230,close2)

# 잔 확인 화면 전환 함수
def check_glass():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() # 아예 창이 닫혀야 함

        screen.fill(WHITE)

        text_cg = font2.render("누구의 잔을 확인하시겠습니까?", True, (255,0,0))
        screen.blit(text_cg, (240,180))
        
        text_ch1=font3.render("com1", True, (255,0,0))
        screen.blit(text_ch1, (110,screen_height-60))
        text_ch2=font3.render("com2", True, (255,0,0))
        screen.blit(text_ch2, (355,screen_height-60))
        text_ch3=font3.render("com3", True, (255,0,0))
        screen.blit(text_ch3, (615,screen_height-60))
        text_ch4=font3.render("확인 안하기", True, (255,0,0))
        screen.blit(text_ch4, (845,screen_height-60))

        # 잔 확인을 할 com 고르기 버튼
        if com1_b.draw():
            com_check(1)
        elif com2_b.draw():
            com_check(2)
        elif com3_b.draw():
            com_check(3)

        # 잔 확인을 안할 선택지
        if close_ch.draw():
            gensei()

        pygame.display.update()
        clock.tick(30)
    pygame.display.update()

# com 잔 확인 버튼
water_c=Button(90,screen_height-230,water)
juice_c=Button(335,screen_height-230,juice)
beer_c=Button(590,screen_height-230,beer)
soju_c=Button(840,screen_height-230,soju)

# com 잔 확인 함수
def com_check(com_glass):
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() # 아예 창이 닫혀야 함

        screen.fill(WHITE)

        if com_glass==1:
            text_cg1 = font2.render("COM1", True, (255,0,0))
            screen.blit(text_cg1, (480,180))
        elif com_glass==2:
            text_cg2 = font2.render("COM2", True, (255,0,0))
            screen.blit(text_cg2, (480,180))
        elif com_glass==3:
            text_cg3 = font2.render("COM3", True, (255,0,0))
            screen.blit(text_cg3, (480,180))

        if water_c.draw():
            # com1 일 때 물,음료,소주,맥주 버튼 눌러서 그 음료에 맞는 True,False 값 확인,판단
            if com_glass==1:
                if com1_water==True:
                    com_result(True)
                elif com1_water==False:
                    com_result(False)
            # com2 일 때 물,음료,소주,맥주 버튼 눌러서 그 음료에 맞는 True,False 값 확인,판단
            elif com_glass==2: 
                if com2_water==True:
                    com_result(True)
                elif com2_water==False:
                    com_result(False)
            # com3 일 때 물,음료,소주,맥주 버튼 눌러서 그 음료에 맞는 True,False 값 확인,판단
            elif com_glass==3: 
                if com3_water==True:
                    com_result(True)
                elif com3_water==False:
                    com_result(False)

        elif juice_c.draw():
            if com_glass==1:
                if com1_juice==True:
                    com_result(True)
                elif com1_juice==False:
                    com_result(False)
            elif com_glass==2: 
                if com2_juice==True:
                    com_result(True)
                elif com2_juice==False:
                    com_result(False)
            elif com_glass==3: 
                if com3_juice==True:
                    com_result(True)
                elif com3_juice==False:
                    com_result(False)

        elif beer_c.draw():
            if com_glass==1:
                if com1_beer==True:
                    com_result(True)
                elif com1_beer==False:
                    com_result(False)
            elif com_glass==2: 
                if com2_beer==True:
                    com_result(True)
                elif com2_beer==False:
                    com_result(False)
            elif com_glass==3: 
                if com3_beer==True:
                    com_result(True)
                elif com3_beer==False:
                    com_result(False)

        elif soju_c.draw():
            if com_glass==1:
                if com1_soju==True:
                    com_result(True)
                elif com1_soju==False:
                   com_result(False)
            elif com_glass==2: 
                if com2_soju==True:
                    com_result(True)
                elif com2_soju==False:
                    com_result(False)
            elif com_glass==3: 
                if com3_soju==True:
                    com_result(True)
                elif com3_soju==False:
                    com_result(False)

        pygame.display.update()
        clock.tick(30)
    pygame.display.update()

# com 잔 확인 결과 화면 전환 함수
def com_result(t_or_f):
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() # 아예 창이 닫혀야 함

        screen.fill(WHITE)
        
        # com 잔 확인 결과에 따라 달라지는 화면 전환 
        if t_or_f==True: # 잔이 채워져 있을 때
            text_t = font2.render("잔이 채워져 있습니다!", True, (255,0,0))
            screen.blit(text_t, (screen_width/2-240,180))
            gensei()
        elif t_or_f==False: # 잔이 비워져 있을 때
            text_f = font2.render("잔이 비어있습니다!", True, (255,0,0))
            screen.blit(text_f, (screen_width/2-220,180))
            gensei()

        pygame.display.update()
        clock.tick(30)
    pygame.display.update()

# 겐세이 화면 com 버튼
com1_gs = Button(90, screen_height-230 , com1)
com2_gs = Button(335, screen_height-230, com2)
com3_gs = Button(590, screen_height-230, com3)
close_gs = Button(840, screen_height-230, close2)

# 겐세이 함수
def gensei():
    global com1_g
    global com2_g
    global com3_g

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() # 아예 창이 닫혀야 함
        
        screen.fill(WHITE)

        text_cg = font2.render("누구에게 겐세이를 하시겠습니까?", True, (255,0,0))
        screen.blit(text_cg, (220,180))
        
        text_gs1=font3.render("com1", True, (255,0,0))
        screen.blit(text_gs1, (110,screen_height-60))
        text_gs2=font3.render("com2", True, (255,0,0))
        screen.blit(text_gs2, (355,screen_height-60))
        text_gs3=font3.render("com3", True, (255,0,0))
        screen.blit(text_gs3, (615,screen_height-60))
        text_cgs=font3.render("겐세이 안하기", True, (255,0,0))
        screen.blit(text_cgs, (835,screen_height-60))

        # com1 겐세이
        if com1_gs.draw():
            if com1_beer==True or com1_soju==True: # com1이 술을 마시지 않았다면? -> 겐세이 성공 -> com 게이지 증가
                print("겐세이 성공!")
                com1_g=com1_g+3
                table()
            elif com1_beer==False or com1_soju==False: # com1이 술을 마셨다면? -> 겐세이 실패 -> 플레이어 취기 증가
                print("겐세이 실패!")
                p.sprite.get_drunk_up(30)
                table()

        # com2 겐세이
        if com2_gs.draw():
            if com2_beer==True or com2_soju==True: # com2이 술을 마시지 않았다면? -> 겐세이 성공 -> com 게이지 증가
                print("겐세이 성공!")
                com2_g=com2_g+3
                table()
            elif com2_beer==False or com2_soju==False: # com2이 술을 마셨다면? -> 겐세이 실패 -> 플레이어 취기 증가
                print("겐세이 실패!")
                p.sprite.get_drunk_up(30)
                table()

        # com3 겐세이
        if com3_gs.draw():
            if com3_beer==True or com3_soju==True: # com3이 술을 마시지 않았다면? -> 겐세이 성공 -> com 게이지 증가
                print("겐세이 성공!")
                com3_g=com3_g+3
                table()
            elif com3_beer==False or com3_soju==False: # com3이 술을 마셨다면? -> 겐세이 실패 -> 플레이어 취기 증가
                print("겐세이 실패!")
                p.sprite.get_drunk_up(30)
                table()

        # 겐세이를 하지 않을 때
        if close_gs.draw():
            print("겐세이를 하지 않습니다")
            table()
            
        pygame.display.update()
        clock.tick(30)
    pygame.display.update()

# 편의점에서 하는 행동 버튼
table_button=Button(150, screen_height-230, table_button) # 테이블로 돌아가기
ice=Button(460, screen_height-230, ice) # 아이스크림
condition=Button(screen_width-280, screen_height-230, condition) # 숙취해소제

# 편의점 함수 (store 변수랑 다르게 함수 이름 선언해야 됨 !)
def store_f():
    store_back=pygame.image.load("이미지/store_f.jpg")
    store_back=pygame.transform.scale(store_back,(screen_width, screen_height))
    place_store = font.render("편의점", True, WHITE)
    pygame.display.set_caption("편의점")

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(store_back,(0,0))
        screen.blit(place_store, (screen_width-260,30))

        store_tb=font3.render("테이블로 돌아가기",True,WHITE)
        screen.blit(store_tb, (135,screen_height-60))

        store_ice=font3.render("아이스크림 먹기",True,WHITE)
        screen.blit(store_ice, (455,screen_height-60))

        store_con=font3.render("숙취해소제 먹기",True,WHITE)
        screen.blit(store_con, (screen_width-285,screen_height-60))

        p.draw(screen)
        p.update()

        # 테이블로 돌아가기
        if table_button.draw():
            print("테이블로 돌아갑니다")
            table()
        
        # 아이스크림 먹기 (턴 +1 , 취기 -1 , 포만도 +1)
        if ice.draw():
            print("아이스크림을 먹습니다")
            p.sprite.get_drunk_down(20)
            p.sprite.get_full_up(20)
        
        # 숙취해소제 먹기
        if condition.draw(): # (턴 +2 , 취기 -2)
            print("숙취해소제를 먹습니다")
            p.sprite.get_drunk_down(40)

        pygame.display.update()
        clock.tick(30)
    pygame.display.update()

#화면전환(게임오버) -> if 문 써서 게이지가 다 차서 게임오버되면 gameover() 실행
def gameover():
    g_o = True
    while g_o:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0, 0, 0))
        draw_text('Game Over', 100, WHITE, 500, 300)
        restart_button = Button(500, 500, start_img)

        if restart_button.draw() == True:
            mainmenu()

        pygame.display.update()
        clock.tick(30)

mainmenu()

pygame.quit()
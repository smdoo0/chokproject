from select import select
import pygame
import time
import sys

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
glass = pygame.image.load("이미지/glass.jpg") # 잔 확인 이미지
glass=pygame.transform.scale(glass,(150,150))
cheers=pygame.image.load("이미지/cheers.png") # 짠(건배) 이미지
cheers=pygame.transform.scale(cheers,(150,150))

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
font = pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 80) # 장소 이름을 위한 폰트
font2=pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 50) # 안내문을 위한 폰트
font3=pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 25) # 안내문을 위한 폰트 2

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
            choose_drink()

        pygame.display.update()
        clock.tick(30)

# 음료 버튼
water_b=Button(90,screen_height-230,water)
juice_b=Button(335,screen_height-230,juice)
beer_b=Button(590,screen_height-230,beer)
soju_b=Button(840,screen_height-230,soju)

# 잔에 들어있는 음료의 종류를 저장하기 위한 리스트
drink_array=[]

# 맨 처음 시작할 때 마실 것 정하기 (음료 종류가 4개) => 4개의 잔 정하기
def choose_drink():
    pygame.display.set_caption("음료 정하기")
    drink = 0 # 잔의 개수

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        text_s1 = font2.render("음료를 선택하세요", True, (255,100,0))
        screen.blit(text_s1, (screen_width/2-170,180))

        # 음료 선택 (버튼을 누를 때 마다 그 버튼의 음료가 리스트에 추가됨)
        if water_b.draw():
            drink_array.append(["water"])
            drink=drink+1
        elif juice_b.draw():
            drink_array.append(["juice"])
            drink=drink+1
        elif beer_b.draw():
            drink_array.append(["beer"])
            drink=drink+1
        elif soju_b.draw():
            drink_array.append(["soju"])
            drink=drink+1
        
        # 4개의 잔을 모두 선택하면 테이블로 넘어감
        if drink==4:
            print(drink_array)

        # 음료 안내문
        water_f=font3.render("물",True,WHITE)
        screen.blit(water_f, (150,screen_height-60))
        juice_f=font3.render("주스",True,WHITE)
        screen.blit(juice_f, (390,screen_height-60))
        beer_f=font3.render("맥주",True,WHITE)
        screen.blit(beer_f, (640,screen_height-60))
        soju_f=font3.render("소주",True,WHITE)
        screen.blit(soju_f, (895,screen_height-60))

        # 음료를 선택한 횟수를 알려줌
        drink_num=font3.render("선택한 음료의 개수 : {}".format(drink),True, WHITE)
        screen.blit(drink_num,(10,5))

        pygame.display.update()
        clock.tick(30)

mainmenu()
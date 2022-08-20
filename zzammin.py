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
background_img = pygame.image.load("이미지\\backgroundimg.png")
start_img = pygame.image.load("이미지\startimg.png")

# 테이블 이미지
table_image = pygame.image.load("이미지/table.jpg")
table_image = pygame.transform.scale(table_image,(screen_width, screen_height)) # 테이블 배경용

# 테이블에서의 행동들에 대한 버튼
select1_image = pygame.image.load("이미지/move.png")
select1_image=pygame.transform.scale(select1_image,(120,150))
select2_image = pygame.image.load("이미지/food.jpg")
select2_image=pygame.transform.scale(select2_image,(150,150))
select3_image = pygame.image.load("이미지/glass.jpg")
select3_image=pygame.transform.scale(select3_image,(150,150))

# 테이블 행동(다른 장소로 이동)에 대한 버튼
toilet=pygame.image.load("이미지/toilet.jpg") # 화장실 이미지
toilet=pygame.transform.scale(toilet,(150,150))
store=pygame.image.load("이미지/store.png") # 편의점 이미지
store=pygame.transform.scale(store,(150,150))
smoking=pygame.image.load("이미지/smoking.png") # 흡연장 이미지
smoking=pygame.transform.scale(smoking,(150,150))
table_b=pygame.transform.scale(table_image,(150,150)) # 테이블 버튼용

# 편의점에서의 행동들에 대한 버튼
table_button=pygame.transform.scale(table_image,(150,150)) # 테이블 버튼용
ice=pygame.image.load("이미지/ice.jpg")
ice=pygame.transform.scale(ice,(150,150))
condition=pygame.image.load("이미지/condition.jpg")
condition=pygame.transform.scale(condition,(150,150))

# 쓰이는 폰트들
font = pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 80) # 장소 이름을 위한 폰트
font2=pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 50) # 안내문을 위한 폰트
font3=pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 25) # 안내문을 위한 폰트 2

clock = pygame.time.Clock()

# 게임에서 쓸 변수들
drunk = 0  # 취기
full = 0  # 포만감
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

        screen.fill((0, 0, 0))
        screen.blit(background_img, (100, 90))
        start_button = Button(800, 500, start_img)

        if start_button.draw() == True:
            table()

        pygame.display.update()
        clock.tick(30)

# 테이블 버튼
select1_image = Button(150, screen_height-230, select1_image)
select2_image = Button(460, screen_height-230, select2_image)
select3_image = Button(screen_width-280, screen_height-230, select3_image)

# 테이블 함수
def table():
    drunk = 0  # 플레이어 취기
    turn = 0  # 턴 수
    full = 0  # 포만감
    chance = 0  # 랜덤 이벤트 발생할때 쓸 변수

    pygame.display.set_caption("테이블")
    place_table = font.render("테이블", True,  WHITE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.blit(table_image, (0, 0))
        screen.blit(place_table, (screen_width-260,30))
        
        table_mv=font3.render("다른 장소로 가기",True,WHITE)
        screen.blit(table_mv, (130,screen_height-60))

        table_fd=font3.render("안주 먹기",True,WHITE)
        screen.blit(table_fd, (488,screen_height-60))

        table_gl=font3.render("자리에 없는 사람 잔 확인",True,WHITE)
        screen.blit(table_gl, (screen_width-325,screen_height-60))

        p.draw(screen)
        p.update()

        # 다른 장소 가기
        if select1_image.draw():
            print("다른 장소로 갑니다")
            turn += 1  # 다른 장소로 가는 것도 턴 소비하는 것..?
            change_table(1) # 다른 장소로 가는 화면 전환

        # 안주 먹기
        if select2_image.draw():
            print("안주를 먹습니다") # 안주 먹기(취기 - 포만도 ++ )
            p.sprite.get_drunk_down(20)
            p.sprite.get_full_up(40)
            change_table(2) # 안주를 먹는 화면 전환
        
        # 자리에 없는 사람 잔 확인
        if select3_image.draw():
            print("자리에 없는 사람의 잔을 확인합니다")
            change_table(3) # 자리에 없는 사람의 잔을 확인하는 화면 전환

        pygame.display.update()
        clock.tick(30)

        pygame.display.update()
    pygame.display.update()

# 테이블 전용 화면 전환 버튼
table_b=Button(screen_width/2-60,400,table_b) # 테이블로 가는 버튼
toilet_b=Button(150, screen_height-230,toilet) # 화장실로 가는 버튼
store_b=Button(460, screen_height-230,store) # 편의점으로 가는 버튼
smoking_b=Button(screen_width-280, screen_height-230,smoking) # 흡연장으로 가는 버튼

global try_store
try_store=False # 편의점에 간 적이 있는지 판단하는 변수

# 테이블 전용 화면 전환 함수
def change_table(click_number):
    running = True
    global try_store
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
            # toilet=Button(100,500,toilet) -> local variable 'toilet' referenced before assignment 라는 에러 발생
            # store=Button(330,500,store)
            # smoking=Button(580,500,smoking)

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
            

            # 흡연장으로 가는 버튼 부분
            text_sm=font3.render("흡연장",True,BLACK)
            screen.blit(text_sm, (screen_width-235,screen_height-60))
            smoking_b.draw()
            # if smoking_b.draw()
                # smoking_f 함수 실행

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
        
        # 자리에 없는 사람 잔 확인 버튼을 눌렀을 때
        if click_number==3: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() # 아예 창이 닫혀야 함

            text_s3 = font3.render("자리에 없는 사람의 잔을 확인합니다...", True, (255,0,0))
            screen.blit(text_s3, (screen_width/2-170,180))

            # 테이블로 가는 버튼 부분
            text_tb=font3.render("테이블로 돌아가기",True,BLACK)
            screen.blit(text_tb, (screen_width/2-75,screen_height-70))
            if table_b.draw(): # 테이블 버튼 누르면 돌아가자
                table()
            pygame.display.update()

        pygame.display.update()
    pygame.display.update()

# 편의점 버튼
table_button=Button(150, screen_height-230, table_button)
ice=Button(460, screen_height-230, ice) # 아이스크림
condition=Button(screen_width-280, screen_height-230, condition) # 숙취해소제

# 편의점 함수 (store 변수랑 다르게 함수 이름 선언해야 됨 !)
def store_f(): 
    drunk = 0  # 플레이어 취기
    turn = 0  # 턴 수
    full = 0  # 포만감
    chance = 0  # 랜덤 이벤트 발생할때 쓸 변수

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

        # 테이블로 돌아가기
        if table_button.draw():
            print("테이블로 돌아갑니다")
            table() 
        
        # 아이스크림 먹기
        if ice.draw():
            print("아이스크림을 먹습니다")
            turn+=1
            drunk-=1
            full+=1
        
        # 숙취해소제 먹기
        if condition.draw():
            print("숙취해소제를 먹습니다")
            turn+=2
            drunk-=2

        pygame.display.update()
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
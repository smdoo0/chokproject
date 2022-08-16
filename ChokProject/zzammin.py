# 테이블 : 다른 장소 가기, 안주 먹기, 자리에 없는사람 잔 확인(4개의 잔 중 하나만 확인 가능)
# 편의점 : 테이블로 돌아가기, 아이스크림(1턴, 취기 - 포만도 + ), 숙취해소제(2턴, 취기 -- )

import pygame
import time

pygame.init()

# 게임 내내 쓸 변수들 
# 얘네는 각각의 함수 안에서 선언해줘야 됨..?
drunk = 0  # 플레이어 취기
turn = 0  # 턴 수
full = 0  # 포만감
chance = 0  # 랜덤 이벤트 발생할때 쓸 변수

screen_w = 800
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("테이블")
table_image = pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/table.jpg")
table_image = pygame.transform.scale(table_image,(screen_w, screen_h)) # 테이블 배경용

select1_image = pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/move.png")
select1_image=pygame.transform.scale(select1_image,(120,150))

select2_image = pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/food.jpg")
select2_image=pygame.transform.scale(select2_image,(150,150))

select3_image = pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/glass.jpg")
select3_image=pygame.transform.scale(select3_image,(150,150))
select_size = select1_image.get_rect().size
w = select_size[0]
h = select_size[1]

black=(0,0,0)
white=(255,255,255)

font = pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 80) # 장소 이름을 위한 폰트
font2=pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 50) # 안내문을 위한 폰트
font3=pygame.font.Font("C:/Users/woals/AppData/Local/Microsoft/Windows/Fonts/양진체v0.9_ttf.ttf", 25) # 안내문을 위한 폰트 2

toilet=pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/toilet.jpg")
toilet=pygame.transform.scale(toilet,(150,150))
store=pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/store.png")
store=pygame.transform.scale(store,(150,150))
smoking=pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/smoking.png")
smoking=pygame.transform.scale(smoking,(150,150))

table_button=pygame.transform.scale(table_image,(150,150)) # 테이블 버튼용
ice=pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/ice.jpg")
ice=pygame.transform.scale(ice,(150,150))
condition=pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/condition.jpg")
condition=pygame.transform.scale(condition,(150,150))

table_b=pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/table.jpg")
table_b=pygame.transform.scale(table_b,(150,150)) # 테이블 버튼용

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # def put_img(self,address): # 이미지 로드
    #     self.image=pygame.image.load(address)
    
    # def change_size(self,x,y): # 이미지 크기 변환
    #     self.image=pygame.transform.scale(self.image,(x,y))

    def draw(self):
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                pygame.time.delay(500) # 누른 뒤 0.5초의 텀을 주기 위해서 (안그러면 바로 다른 버튼이 눌림)

            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

select1_image = Button(100, 550, select1_image)
select2_image = Button(330, 550, select2_image)
select3_image = Button(580, 550, select3_image)

def table(): # 테이블 함수
    drunk = 0  # 플레이어 취기
    turn = 0  # 턴 수
    full = 0  # 포만감
    chance = 0  # 랜덤 이벤트 발생할때 쓸 변수

    place_table = font.render("테이블", True, white)
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(table_image, (0, 0))
        screen.blit(place_table, (30,30))

        if select1_image.draw(): # 다른 장소 가기
            print("다른 장소로 갑니다")
            turn += 1  # 다른 장소로 가는 것도 턴 소비하는 것..?
            change_table(1) # 다른 장소로 가는 화면 전환
            

        if select2_image.draw(): # 안주 먹기
            print("안주를 먹습니다")  # 안주 먹기(취기 - 포만도 ++ )
            drunk -= 1
            full += 2
            change_table(2) # 안주를 먹는 화면 전환
            

        if select3_image.draw(): # 자리에 없는 사람 잔 확인
            print("자리에 없는 사람의 잔을 확인합니다")
            change_table(3) # 자리에 없는 사람의 잔을 확인하는 화면 전환
        
        pygame.display.update()
    pygame.display.update()

table_b=Button(330,500,table_b) # 테이블로 가는 버튼
toilet_b=Button(100,500,toilet) # 화장실로 가는 버튼
store_b=Button(330,500,store) # 편의점으로 가는 버튼
smoking_b=Button(580,500,smoking) # 흡연장으로 가는 버튼

def change_table(click_number): # 테이블 전용 화면 전환 함수
    running = True
    try_store=False # 편의점에 간 적이 있는지 판단하는 변수

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() # 아예 창이 닫혀야 함
        
        screen.fill(white) # 하얀색 배경
        
        if click_number==1: # 다른 장소로 가는 버튼을 눌렀을 때
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() # 아예 창이 닫혀야 함

            text_s1 = font2.render("다른 장소로 갑니다...", True, (255,0,0))
            text_s1_rect=text_s1.get_rect()
            pygame.draw.rect(text_s1,white,text_s1_rect,1)
            screen.blit(text_s1, (210,180))
            # toilet=Button(100,500,toilet) -> local variable 'toilet' referenced before assignment 라는 에러 발생
            # store=Button(330,500,store)
            # smoking=Button(580,500,smoking)

            # 화장실로 가는 버튼 부분
            text_t=font3.render("화장실",True,black)
            text_t_rect=text_t.get_rect()
            pygame.draw.rect(text_t,white,text_t_rect,1)
            screen.blit(text_t, (140,650))
            toilet_b.draw()
            # if toilet_b.draw()
                # toilet_f 함수 실행

            # 편의점으로 가는 버튼 부분
            text_st=font3.render("편의점",True,black)
            text_st_rect=text_st.get_rect()
            pygame.draw.rect(text_st,white,text_st_rect,1)
            screen.blit(text_st, (370,650))
            if store_b.draw() and try_store==False: # 편의점 버튼 눌렀을 때
                try_store=True # 편의점 한번 갔으니까 try_store를 True로 바꿈
                store_f() # 편의점 함수 실행

            # 흡연장으로 가는 버튼 부분
            text_sm=font3.render("흡연장",True,black)
            text_sm_rect=text_sm.get_rect()
            pygame.draw.rect(text_sm,white,text_sm_rect,1)
            screen.blit(text_sm, (630,650))
            smoking_b.draw()
            # if smoking_b.draw()
                # smoking_f 함수 실행

        if click_number==2: # 안주를 먹는 버튼을 눌렀을 때
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() # 아예 창이 닫혀야 함

            text_s2 = font3.render("안주를 맛있게 먹습니다... 취기 하락,포만도 크게 증가", True, (255,0,0))
            text_s2_rect=text_s2.get_rect()
            pygame.draw.rect(text_s2,white,text_s2_rect,1)
            screen.blit(text_s2, (140,350))

            # 테이블로 가는 버튼 부분
            text_tb=font3.render("테이블로 돌아가기",True,black)
            text_tb_rect=text_tb.get_rect()
            pygame.draw.rect(text_tb,white,text_tb_rect,1)
            screen.blit(text_tb, (310,650))
            if table_b.draw(): # 테이블 버튼 누르면 돌아가자
                table() # 문제! 이 부분에서 테이블로 넘어가고 quit 하면 안꺼지고 안주를 맛있게 먹습니다 부분으로 감
            pygame.display.update()
            
        if click_number==3: # 자리에 없는 사람 잔 확인 버튼을 눌렀을 때
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() # 아예 창이 닫혀야 함

            text_s3 = font3.render("자리에 없는 사람의 잔을 확인합니다...", True, (255,0,0))
            text_s3_rect=text_s3.get_rect()
            pygame.draw.rect(text_s3,white,text_s3_rect,1)
            screen.blit(text_s3, (220,350))

            # 테이블로 가는 버튼 부분
            text_tb=font3.render("테이블로 돌아가기",True,black)
            text_tb_rect=text_tb.get_rect()
            pygame.draw.rect(text_tb,white,text_tb_rect,1)
            screen.blit(text_tb, (310,650))
            if table_b.draw(): # 테이블 버튼 누르면 돌아가자
                table()# 문제! 이 부분에서 테이블로 넘어가고 quit 하면 안꺼지고 자리에 없는 사람 잔 확인 부분으로 감
            pygame.display.update()
        pygame.display.update()
    pygame.display.update()

table_button=Button(100, 550, table_button)
ice=Button(330, 550, ice) # 아이스크림
condition=Button(550, 550, condition) # 숙취해소제

def store_f(): # 편의점 함수 (store 변수랑 다르게 함수 이름 선언해야 됨 !)
    drunk = 0  # 플레이어 취기
    turn = 0  # 턴 수
    full = 0  # 포만감
    chance = 0  # 랜덤 이벤트 발생할때 쓸 변수

    store_back=pygame.image.load("C:/Users/woals/Desktop/PythonWorkspace/chokproject/이미지/store_f.jpg")
    store_back=pygame.transform.scale(store_back,(screen_w,screen_h))
    place_store = font.render("편의점", True, white)
    pygame.display.set_caption("편의점")

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        screen.blit(store_back,(0,0))
        screen.blit(place_store, (30,30))

        store_tb=font3.render("테이블로 돌아가기",True,black)
        store_tb_rect=store_tb.get_rect()
        pygame.draw.rect(store_tb,white,store_tb_rect,1)
        screen.blit(store_tb, (85,710))

        if table_button.draw():
            print("테이블로 돌아갑니다")
            table() # 문제! 여기서 테이블로 넘어가고 quit 누르면 편의점으로 감
        
        if ice.draw():
            print("아이스크림을 먹습니다")
            turn+=1
            drunk-=1
            full+=1
        
        if condition.draw():
            print("숙취해소제를 먹습니다")
            turn+=2
            drunk-=2

        pygame.display.update()
    pygame.display.update()


table()

pygame.quit()
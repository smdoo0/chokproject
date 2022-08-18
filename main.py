import pygame, sys
import time

#글씨쓰기
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

#플레이어 정보 및 체력
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((0,0))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (0,0))
        self.current_health = 20
        self.target_health = 50
        self.max_health = 100
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5 #고정

    def get_damage(self,amount): #취기 상승
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self,amount): #취기 하락
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def update(self):
        self.alcohol()
        self.full()
		
    def alcohol(self):
        transition_width = 0
        transition_color = (255,0,0)
        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0,255,0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed 
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255,255,0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(70,15,health_bar_width,25)
        transition_bar = pygame.Rect(health_bar.right,15,transition_width,25)
        draw_text('Drunk', 30, WHITE, 30, 18)
        pygame.draw.rect(screen,(255,0,0),health_bar)
        pygame.draw.rect(screen,transition_color,transition_bar)
        pygame.draw.rect(screen,(255,255,255),(70,15,self.health_bar_length,25),4)

    def full(self):
        transition_width = 0
        transition_color = (255,0,0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0,255,0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed 
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255,255,0)
        

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(70,45,health_bar_width,25)
        transition_bar = pygame.Rect(health_bar.right,45,transition_width,25)
        draw_text('Full', 30, WHITE, 30,50)
        pygame.draw.rect(screen,(255,0,0),health_bar)
        pygame.draw.rect(screen,transition_color,transition_bar)	
        pygame.draw.rect(screen,(255,255,255),(70,45,self.health_bar_length,25),4)	


#버튼
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

        if self.rect.collidepoint(pos): # slef.rect 즉 버튼크기의 좌표 위로 마우스 좌표가 겹쳐지면
            self.image = self.bigimage #마우스가 버튼위로 올라왔을때 빅 이미지로 바꾸며 버튼이 커지는 이펙트 부여

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # 0은 좌클릭 , 1은 휭클릭 2는 우클릭
                self.clicked = True
                action = True #눌리면 트루값 반납

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False #마우스를 때는순간 클릭은 거짓으로 바뀐다
        else:
            self.image = self.tempimage #마우스커서가 버튼 밖으로 나간다면 원래크기로 돌아간다

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

pygame.init()

WHITE = (255, 255, 255)
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background_img = pygame.image.load("이미지\\backgroundimg.png")
start_img = pygame.image.load("이미지\startimg.png")
restart_img = pygame.image.load("이미지\\restart1.png")

select_size = start_img.get_rect().size
w = select_size[0]
h = select_size[1]

clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle(Player())

#취기,포만감, 턴 관련 변수
drunk = 0
full = 0
turn = 1
pygame.display.set_caption("술자리 시뮬레이션")



#시작화면 및 메인 루프문
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
        player.draw(screen)
        player.update()
        if start_button.draw() == True:
            selectscreen()
        pygame.display.update()
        clock.tick(30)

#화면전환(테이블)
def selectscreen():
    select = True
    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.sprite.get_health(20) # 여기에 게이지 조작 +
                if event.key == pygame.K_DOWN:
                    player.sprite.get_damage(20) # 여기에 게이지 조작 -
        
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update()
        pygame.display.update()
        clock.tick(30)

#글씨쓰기
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

#플레이어 상태

#플레이어 상태 표시
#def showgauge():
    #if Event.type == pygame.KEYDOWN:
        #if Event.type == pygame.K_UP:
                #Player.sprite.get_health(20)
    #if Event.type == pygame.KEYDOWN:
            #if Event.type == pygame.K_DOWN:
                #Player.sprite.get_damage(20)

mainmenu()
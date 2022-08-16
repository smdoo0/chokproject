from select import select
import pygame
import time
import sys

pygame.init()

WHITE = (255, 255, 255)
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background_img = pygame.image.load("이미지//backgroundimg.png")
start_img = pygame.image.load("이미지/startimg.png")

select_size = start_img.get_rect().size
w = select_size[0]
h= select_size[1]

clock = pygame.time.Clock()

drunk = 0
full = 0

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

pygame.display.set_caption("술자리 시뮬레이션")

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

        screen.fill((0, 0, 0))
        gauge()

        pygame.display.update()
        clock.tick(30)

#글씨쓰기
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

#게이지
def gauge():
    draw_text('Drunk: %d' %drunk, 40, WHITE, 80, 10)
    draw_text('Full: %d' %full, 40, WHITE, 75, 60)

mainmenu()
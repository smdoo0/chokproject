import pygame

WHITE = (255, 255, 255)
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

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


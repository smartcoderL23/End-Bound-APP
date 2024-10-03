import pygame  #import pygame module
import random
import time
 # a= int(input("start"))
pygame.init()  # initialize pygame

# Step 1: create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_SURFACE = pygame.image.load('Screenshot 2024-10-03 8.36.42 AM.png
Lat.png').convert_alpha()
PLAYER_SURFACE = pygame.transform.scale(PLAYER_SURFACE, (200, 150))
PLAYER = PLAYER_SURFACE.get_rect(midbottom=(400, 600))

BG_SURFACE = pygame.image.load('homepage.png').convert_alpha()
BG_SURFACE = pygame.transform.scale(BG_SURFACE, (800, 600))
BACKROUND = BG_SURFACE.get_rect()

Cookie_SURFACE = pygame.image.load('cookie.png').convert_alpha()
Cookie_SURFACE = pygame.transform.scale(Cookie_SURFACE, (61, 61))
Cookie = Cookie_SURFACE.get_rect(midbottom=(random.randint(0, SCREEN_WIDTH), 50))

class SpriteObject(pygame.sprite.Sprite):
    # [...]

    def update(self, event_list):

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # [...]

my_sprite = SpriteObject()
group = pygame.sprite.Group(Screenshot 2024-10-03 8.36.42 AM.png
Lat.png)

font = pygame.font.Font('cookie.ttf', 50)

run = True
while run:

    # text_surface2 = font2.render('Score you got diabetes', True, (255, 255, 255), (245, 32, 78))

    # code = catching cookies

    text_surface = font.render(('Score  '+str(score)), True, (255, 255, 255), (245, 32, 78))
    text = text_surface.get_rect()
    screen.blit(BG_SURFACE, BACKROUND)
    screen.blit(Cookie_SURFACE, Cookie)
    screen.blit(PLAYER_SURFACE, PLAYER)
    screen.blit(text_surface, text)

    key = pygame.key.get_pressed()
        #add up and down limit/barrier
    if key[pygame.K_RIGHT] == True:
        PLAYER.x += 2
    if key[pygame.K_LEFT] == True:
        PLAYER.x -= 2
        # Step 3: Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    # pygame.time.Clock().tick(120)

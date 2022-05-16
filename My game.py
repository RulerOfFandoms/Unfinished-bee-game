import pygame
from sys import exit
import pygame.draw

def score_counter():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score = font.render(f' Your Score: {current_time} ',False, 'Black')
    score_rect = score.get_rect(center = (650,100))
    pygame.draw.rect(screen, '#75D9E8', score_rect, 10, 20)
    screen.blit(score, score_rect)

pygame.init() #start game
screen = pygame.display.set_mode((1375,710))
screen.fill((255,255,255))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('Koulen-Regular.ttf', 45)
game_active = True
start_time = 0

background = pygame.image.load('Pygame background.png').convert()
floor = pygame.image.load('Pygame Floor.png').convert()

#score = font.render(' Your score: ', False,(0,0,0))
#score_rect = score.get_rect(center = (650, 100))

#restart text
restart = font.render(' If you wish to play again, press space ', False,(0,0,0))
restart_rect = restart.get_rect(center = (650, 300))

#spider variables
spider = pygame.image.load('Spider.png').convert_alpha()
spider_rect = spider.get_rect(bottomright = (1300, 600))

#your player variables
bee = pygame.image.load('Bee(wings up).png').convert_alpha()
bee_rect = bee.get_rect(midbottom = (100, 600))
bee_mid = pygame.image.load("Bee(wings going down).png").convert_alpha()
bee_mid_rect = bee_mid.get_rect(midbottom = (100,600))
bee_down = pygame.image.load("Bee(wings down).png").convert_alpha()
bee_down_rect = bee_down.get_rect(midbottom = (100,600))
bee_fly = 0


def ground():  # make the ground
    screen.blit(floor,(0,600))
    screen.blit(floor,(100,600))
    screen.blit(floor, (200, 600))
    screen.blit(floor, (300, 600))
    screen.blit(floor, (400, 600))
    screen.blit(floor, (500, 600))
    screen.blit(floor, (600, 600))
    screen.blit(floor, (700, 600))
    screen.blit(floor, (800, 600))
    screen.blit(floor, (900, 600))
    screen.blit(floor, (1000, 600))
    screen.blit(floor, (1100, 600))
    screen.blit(floor, (1200, 600))
    screen.blit(floor, (1300, 600))
    screen.blit(floor, (1400, 600))

while True:
    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active: #key presses
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bee_rect.collidepoint(event.pos):
                    bee_fly = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bee_fly = -20
                elif event.key == pygame.K_SPACE: #close game when pressing space bar
                    pygame.quit()
                    exit()

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                spider_rect.left = 1375
                start_time = int(pygame.time.get_ticks() / 1000) #restart score
    if game_active:
        screen.blit(background,(0,0)) # changing screens
        ground()
        screen.blit(bee, bee_rect)
        spider_rect.x -= 6
        if spider_rect.right <= 0:
            spider_rect.left = 1375
        screen.blit(spider, spider_rect)
        score_counter()


        #your player code
        bee_fly += 1
        bee_rect.y += bee_fly
        if bee_rect.bottom >= 600:
            bee_rect.bottom = 600
        elif bee_rect.top <= 1:
            bee_rect.top = 1

        #collision
        if spider_rect.colliderect(bee_rect):
            game_active = False
    else:
        screen.blit(background,(0,0))
        ground()
        screen.blit(restart,(restart_rect))


    pygame.display.update() # keep window open and update
    clock.tick(60) #frame rate

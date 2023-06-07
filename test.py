import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("hero_sprite.png")
        #aq simagle da siganes tvisebebi
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0

    #refreshis methodi
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


#initializacia pygame-is

pygame.init()

#dispplay

screen = pygame.display.set_mode((920, 700))
pygame.display.set_caption("My Dario Game")

#heros obieqtis gaketeba
hero = Hero(100, 400, 64, 64)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #gilakebis (keyboardis) gamowera
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        hero.speed_x = -5
    elif keys[pygame.K_RIGHT]:
        hero.speed_x = 5
    elif keys[pygame.K_UP]:
        hero.speed_y = -5
    elif keys[pygame.K_DOWN]:
        hero.speed_y = 5
    else:
        #klavishs rom aushveb modzraoba rom shewyvitos
        hero.speed_x = 0
        hero.speed_y = 0
    
    #hero-s ganaxleba
    hero.update()

    #daxatva monitorze
    screen.blit(hero.image, hero.rect)

    #display update
    pygame.display.flip()

pygame.quit()
import pygame


#gmiris klasi
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



#init pygame!!
pygame.init()

#display-is obieqtis gaketeba zomaze
screen = pygame.display.set_mode((920, 800))
pygame.display.set_caption("My platformer Game")

#suratis chatvirtva!
background_img = pygame.image.load("start_screen.png")
next_screen_img = pygame.image.load("next_screen1.png")
next_screen_img = pygame.transform.scale(next_screen_img, (920, 700))

#gilakis gaketeba zomaze da suratis mimagreba!
start_btn_img = pygame.image.load("start_button.png")
button_width = 200
button_height = 100
start_btn_img = pygame.transform.scale(start_btn_img, (button_width, button_height))
start_btn_rect = start_btn_img.get_rect()
start_btn_rect.center = (400, 400)#button-is adgilmdebareoba
#aplikaciis dawyebis cvladi
running = True
#tamashis dawyebis cvladi
game_started = False
#heros obieqtis gaketeba
hero = Hero(100, 400, 64, 64)
#spritebis saxis micema rom suratze daidos zemodan 
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_btn_rect.collidepoint(mouse_pos):
                game_started = True
                print("Start button clicked!!!") # aq dawer shens logikas ra unda mmoxdes startze dacherisas
    if game_started:
        #screen image-is chveneba
        screen.blit(next_screen_img, (0, 0))
        #tu monitoris gasuftaveba ginda
        #screen.fill(0, 0, 0)
        #sprite-bis daxatva
        all_sprites.draw(screen)
        #input gilakebis gamowera
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

    else:
        #dasawyisis screenis backgroundis gaketeba
        screen.blit(background_img, (0, 0))
        #achvene start button-i
        screen.blit(start_btn_img, start_btn_rect)
    #ganaxleba monitoris
    pygame.display.flip()

pygame.quit()


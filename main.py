# Main file to my very first pygame called pyTANK
# Basic set up

# Acceso a la libreria 
import pygame
import os


# Constantes

SCREEN_WIDTH  = 800 # Anchura de la pantalla
SCREEN_HEIGHT = 800 # Altura de la pantalla
WHITE_COLOR = (255, 255, 255)# Color blanco
BLACK_COLOR = (0,   0,   0)  # Color negro
SCREEN_TITLE = "pyTANK 0.1"  # Nombre del juego
GAME_FOLDER = os.path.dirname(__file__)
SPRITES_FOLDER = os.path.join(GAME_FOLDER, "images")

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("Comicsans", 75)


class Game():
    TICK = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.all_sprites = pygame.sprite.Group()
        self.game_screen = pygame.display.set_mode((width, height))
        sherman = Tank(400, 300)
        self.all_sprites.add(sherman)
        self.game_screen.fill(BLACK_COLOR)
        pygame.display.set_caption(title)

    def run_game(self):
        is_game_over = False
        direction = 0
        
        while not is_game_over:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    is_game_over = True
					
                print (event)

            self.game_screen.fill(BLACK_COLOR)
            self.all_sprites.update()
            self.all_sprites.draw(self.game_screen)
            
            clock.tick(self.TICK)
            pygame.display.flip()        


        

class Tank(pygame.sprite.Sprite):
        
    def __init__(self, x, y, angle = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(SPRITES_FOLDER, "body.png")).convert()
        self.image = pygame.transform.rotate(self.image, 270)
        self.image.set_colorkey(BLACK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.speedy = 2
        self.speedr = 2
        
    def update(self):
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_w] and self.rect.top > 0:
            self.rect.top -= self.speedy
        if keystate[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.top += self.speedy

        
            
    def draw(self):
        pass


class Mob(pygame.sprite.Sprite):
    def __init__(slef):
#         pygame.sprite.Sprite.__init__(self)
        pass
        
    
pygame.init()

pytank = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
pytank.run_game()


pygame.quit()
quit()
    

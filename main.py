# Main file to my very first pygame called pyTANK
# Basic set up

# Acceso a la libreria 
import pygame


# Constantes

SCREEN_WIDTH  = 800 # Anchura de la pantalla
SCREEN_HEIGHT = 800 # Altura de la pantalla
WHITE_COLOR = (255, 255, 255)# Color blanco
BLACK_COLOR = (0,   0,   0)  # Color negro
SCREEN_TITLE = "pyTANK 0.1"  # Nombre del juego
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("Comicsans", 75)


class Game():
    TICK = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game(self):
        is_game_over = False
        direction = 0

        sherman = Tank("images/body.png", 200, 300, 142, 124)
        
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        direction = 1
                    elif event.key == pygame.K_s:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        direction = 0

                print (event)

            self.game_screen.fill(WHITE_COLOR)    
            sherman.move(direction)
            sherman.draw(self.game_screen)
            
            
            pygame.display.update()
            clock.tick(self.TICK)

class GameObjects:
    def __init__(self, image_path, x, y, width, hight):
        object_image = pygame.image.load(image_path)
        self.sprite = pygame.transform.scale(object_image, (width, hight))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = hight

    def draw(self, background):
        background.blit(self.sprite, (self.x_pos, self.y_pos))
        

class Tank(GameObjects):

    SPEED = 10
    def __init__(self, image_path, x, y, width, hight):
        super().__init__(image_path, x, y, width, hight)

    def move(self, direction):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        
            
        
    

pygame.init()

pytank = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
pytank.run_game()


pygame.quit()
quit()
    

import pygame

TAMAÑO = (600, 600)
BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
clock = pygame.time.Clock()

class game():
    TICK = 60

    def __init__(self, tam):

        self.pantalla = pygame.display.set_mode(tam)
        

    def run_game(self):
        self.fin = False
        while not self.fin:
            self.pablo = pygame.draw.rect(self.pantalla, (0, 0, 0), (50, 50, 150, 150), 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin = True
                    
                self.pablo.   
                print(event)
                pygame.display.update()
            
                clock.tick(self.TICK)
                self.pantalla.fill(BLANCO)
            





play = game(TAMAÑO)
pygame.init()

play.run_game()

pygame.quit()
quit()
    

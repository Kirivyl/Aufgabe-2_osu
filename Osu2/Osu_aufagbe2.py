import pygame 
import os
from random import randint 
#Settingsklasse
class Settings(object):

    # Bildschirm 
    window_height = 800
    window_width = 800
    #datei
    path_file = os.path.dirname(os.path.abspath(__file__))
    path_image = os.path.join(path_file, "Images")
    #overlay
    title = "Pygame Osuplatzen"
    #Ball
    #Inneres Rechteck
    inner_rect = pygame.Rect(50, 50, (window_height) -200, (window_width)-200)
    

class Background(pygame.sprite.Sprite):
    def __init__(self, filename) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.path_image, filename)).convert()
        self.image = pygame.transform.scale(self.image, (Settings.window_width, Settings.window_height))
      
    # Bei Null anfängt zu "zeichnen"
    def draw(self, screen):
        screen.blit(self.image,(0,0))

class ball(pygame.sprite.Sprite): 
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.path['Images'], "ball.png"))
        self.image_scale = pygame.transform.scale(self.image_scale, (10,10))

    def ball_scale(self):
        pass

    def draw(self):
        screen.blit.
        ()
        
class Game(object):
    def __init__(self) -> None:
        super().__init__()
        # Init PyGame Settings
        pygame.init()
        pygame.display.set_caption(Settings.title)

        self.screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.watch_for_events()
            self.update()
            self.draw()
        pygame.quit()

    def watch_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass
    def draw(self):
        self.background.draw(self.screen)
        pygame.display.flip()




if __name__ == "__main__":
    os.environ["SDL_VIDEO_WINDOW_POS"] = "500, 50"

    game = Game()
    game.run()
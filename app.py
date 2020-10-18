import pygame as pg

class Game:
    
    def __init__(self, width, height):
        self.resolution = self.width, self.height = width, height
        self.running = True
        self.display_surface = None
    
    def init(self):
        if pg.init():
            self.display_surface = pg.display.set_mode(self.resolution, pg.HWSURFACE | pg.DOUBLEBUF)
            if self.display_surface:
                self.running = True
    
    def render(self):
        pass
    
    def cleanupe(self):
        pg.quit()
    
    def handle_event(self, event):
        if event.type == pg.QUIT:
            self.running = False
        
    def update(self):
        pass
        
    def start(self):
        if self.init() == False:
            self.running = False
        
        while self.running:
            for event in pg.event.get():
                self.handle_event(event)
                
            self.update()
            self.render()
        self.cleanup()    

if __name__ == "__main__":
    game = Game(800, 600)
    game.start()
        
    
    
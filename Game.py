import pygame as pg
from settings import *
from Board import *

class Game:
    def __init__(self):
        
        # To control game excecution
        self.running = True

        # Board object
        self.board = Board()

        # Initialize pygame
        pg.init()

        # Initialize the screen.
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.screen.fill(WHITE)

        # Clock object
        self.clock = pg.time.Clock()

    def handle_events(self):
        # Handling events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONUP:
                self.board.mouse_listener = True

        self.board.handle_events()
    
    def draw(self):
        self.board.draw(self.screen)
        pg.display.flip()

    def update(self):
        self.board.update()
        self.clock.tick(FPS)

    def run(self):
        # Main loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
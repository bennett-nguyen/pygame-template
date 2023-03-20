import sys
import pygame as pg
from src.comp.debug_panel import DebugPanel
from src.comp.object import Object
from src.preload.settings import WIDTH, HEIGHT, FPS
from pygame.locals import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, WINDOWFOCUSLOST, WINDOWMOVED


class Game:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 512)
        pg.init()

        pg.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, WINDOWFOCUSLOST, WINDOWMOVED])
        pg.display.set_caption("Sample Text")

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.new_game()

    def new_game(self):
        """
        Connecting components
        """
        self.debug_panel = DebugPanel(self)
        self.object = Object(self)

    def draw(self):
        """
        For drawing backgrounds
        """
        self.screen.fill("White")

    def update(self):
        """
        For updating and drawing main components
        """
        self.delta_time = self.clock.tick(FPS)
        self.object.update()
        self.debug_panel.update()
        pg.display.flip()

    def check_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == QUIT:
                pg.quit()
                sys.exit(0)

    def run(self):
        while 1:
            self.check_events()
            self.update()
            self.draw()

import pygame as pg
from src.preload.settings import HALF_HEIGHT, HALF_WIDTH


class Object:
    def __init__(self, game):
        self.game = game
        self.surf = pg.Surface((50, 50))
        self.rect = self.surf.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
        self.velocity = 1

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_DOWN]:
            self.rect.y += self.velocity * self.game.delta_time
        if keys[pg.K_UP]:
            self.rect.y -= self.velocity * self.game.delta_time
        if keys[pg.K_LEFT]:
            self.rect.x -= self.velocity * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.rect.x += self.velocity * self.game.delta_time
        
        self.draw()

    def draw(self):
        self.game.screen.blit(self.surf, self.rect)

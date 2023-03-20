import pygame as pg
from typing import Dict, Any


class DebugPanel:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.SysFont("consolas", 15)
        self.number_of_registries = 2
        self.registries: Dict[str: Any] = {}
        self.margin = 10
        self.padding = 20

        sample = self.font.render("example", False, "White")
        self.background = pg.Surface((200 + self.padding * 2, self.number_of_registries * sample.get_height() + self.padding))
        self.background.fill("black")
        self.background.set_alpha(100)

    def get_info(self):
        self.registries["FPS"] = int(self.game.clock.get_fps())
        self.registries["Delta Time"] = self.game.delta_time

    def update(self):
        self.get_info()
        offset_y = 0
        self.game.screen.blit(self.background, (self.margin, self.margin))

        for register, value in self.registries.items():
            text = self.font.render(f"{register}: {value}", True, "white")
            self.game.screen.blit(text, (self.padding, self.padding+offset_y))
            offset_y += text.get_height() + offset_y

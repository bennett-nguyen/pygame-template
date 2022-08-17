import pygame as pg
import src.preload.constant as const
from src.preload.template import Scene

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.id = const.GAME_SCENE_ID
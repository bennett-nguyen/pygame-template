import pygame as pg
import src.preload.ds as ds
from src.preload.template import Scene

class SceneSwitcher:
    def __init__(self, scenes: dict[int: Scene], start_id: int):
        self.scenes = scenes
        self.current_scene = self.scenes[start_id]

    def input(self):
        pass

    def update(self):
        self.current_scene.update()

    def change_scene(self, id: int):
        self.current = self.scenes[id]


import time
import pygame as pg
import src.preload.ds as ds
import src.preload.constant as const

from sys import exit
from src.preload.shared import shared_data
from src.comp.scene.main_scene import Game
from src.preload.switcher import SceneSwitcher

dt: float = 0
current: float = 0
last: float = time.time()

scenes = {
    const.GAME_SCENE_ID: Game()
}

scene_switcher = SceneSwitcher(scenes, const.GAME_SCENE_ID)

while 1:
    current = time.time()
    dt = current - last
    last = current

    ds.screen.fill('Black')
    ds.clock.tick(const.FPS)

    events = pg.event.get()
    shared_data.events = events
    shared_data.dt = dt

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    scene_switcher.update()
    pg.display.flip()
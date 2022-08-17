import json
import pygame as pg
from typing import Optional

class Spritesheet:
    def __init__(self, image_path: str, config_path: Optional[str] = None, meta_data_path: Optional[str] = None):
        with open(config_path, 'r') as config:
            self.config = json.load(config)

        with open(meta_data_path, 'r') as meta:
            self.meta_data = json.load(meta)

        if self.config['transparent']:
            self.sprite_sheet = pg.image.load(image_path).convert_alpha()
            return

        self.sprite_sheet = pg.image.load(image_path).convert()

    def get_sprite(self, x: int, y: int, width: int, height: int) -> pg.Surface:
        """
        (not recommended)
        get sprite directly from the spritesheet using x, y coordinates and width, height of the image
        """
        sprite = pg.Surface((width, height), pg.SRCALPHA, 32)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite

    def parse_sprite(self, name: str, angle: Optional[float] = None, scale: Optional[float] = None) -> pg.Surface:
        """
        (recommended)
        get sprite from the spritesheet using the name of the sprite in the metadata
        """
        sprite = self.meta_data['frames'][name]['frame']
        x, y, width, height = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        angle = angle if angle is not None else self.config['angle']
        scale = scale if scale is not None else self.config['scale']

        image = pg.transform.rotozoom(self.get_sprite(x, y, width, height), angle, scale)

        return image

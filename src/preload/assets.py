import pygame as pg
from dataclasses import dataclass
from src.preload.spritesheet import Spritesheet

@dataclass(frozen=True, init=True, eq=False, unsafe_hash=False)
class Font:
    FONT_MAP = {
        "name of font": "path to font"
    }

    @classmethod
    def get_font(cls, name: str, size: int):
        """
        Available fonts: 
        - name of font

        Standard size:
        - title font 1: 100
        - title font 2: 75
        - title font 3: 50
        - small font: 25
        """
        return pg.font.Font(cls.FONT_MAP[name], size)

@dataclass(frozen=True, eq=False, unsafe_hash=False, init=False)
class Gallery:
    pass

@dataclass(frozen=True, eq=False, unsafe_hash=False, init=False)
class Audio:
    pass
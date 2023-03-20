"""
Defines constants that are used throughout the game

What defines a constant?
- A constant is a variable whose value must not be changed AT run-time

Rules for defining constants:
- Name of the constant must be made UPPERCASE
- Must include type annotation for the constant
"""
from typing import Tuple

RES: Tuple[int, int] = (1200, 590)
WIDTH: int = RES[0]
HEIGHT: int = RES[1]
FPS: int = 60
PAUSED_FPS: int = 30

HALF_WIDTH: int = WIDTH/2
HALF_HEIGHT: int = HEIGHT/2

GAME_SCENE_ID = 0xAA0001
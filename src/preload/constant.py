"""
Defines constants that are used throughout the game

What defines a constant?
- A constant is a variable whose value must not be changed AT run-time

Rules for defining constants:
- Name of the constant must be made UPPERCASE
- Must include type annotation for the constant
- When defining constant as a flag, assign a hexadecimal value to it (e.g 0x123ABC)

Hex flag:
A hex flag must have 6 digits, 2 of which are prefix of the flag and will be used for denoting types of flag

Prefix:
- 0xAA: Game scene's id
- Any other prefix can be freely used for different purposes

When importing the constant module, assign a new alias for this module as "const"
(e.g. import src.preload.constant as const)
"""


WIDTH: int = 1200
HEIGHT: int = 590
FPS: int = 60
PAUSED_FPS: int = 30

HALF_WIDTH: int = WIDTH/2
HALF_HEIGHT: int = HEIGHT/2

GAME_SCENE_ID = 0xAA0001
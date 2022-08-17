import pygame as pg
from typing import Optional, Union

class Timer:
    '''
    Standard timer for pygame
    '''

    def __init__(self, length_of_timer):
        self.current_time = 0
        self.static_point = 0
        self.length_of_timer = length_of_timer

    def set_static_point(self):
        self.static_point = pg.time.get_ticks()

    def set_current_time(self):
        self.current_time = pg.time.get_ticks()

    def timer(self, new_length_of_timer: Optional[Union[int, float]] = None) -> bool:
        length_of_timer = self.length_of_timer if new_length_of_timer is None else new_length_of_timer
        return self.current_time - self.static_point > length_of_timer + self.paused_delay

    def reset_timer(self):
        self.paused_delay = 0
        self.current_time = self.static_point = pg.time.get_ticks()

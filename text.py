import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Text():
    def __init__(self, text, text_col, x, y):
        self.text = text
        self.text_col = text_col
        self.position = (x, y)

    def to_screen(self, screen):
        pass
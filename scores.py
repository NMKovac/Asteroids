import pygame
from text import Text
from constants import SCREEN_HEIGHT

class Score(Text):
    def __init__(self, score, text_col="white", x=10, y=10):
        super().__init__(score, text_col, x, y)
        self.text = f"Score: {self.text}"

    def to_screen(self, screen):
        font = pygame.font.SysFont('Arial', 20)
        img = font.render(self.text, True, self.text_col)
        screen.blit(img, self.position)
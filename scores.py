import pygame
from constants import SCREEN_HEIGHT

class Score():
    def __init__(self, score, text_col="white", x=10, y=10):
        self.text = f"Score: {score}"
        self.text_col = text_col
        self.position = (x, y)

    def to_screen(self, screen):
        font = pygame.font.SysFont('Arial', 20)
        img = font.render(self.text, True, self.text_col)
        screen.blit(img, self.position)
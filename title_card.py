import pygame
from text import Text
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class TitleCard(Text):
    def __init__(self, text, text_size, text_col="white", x=SCREEN_WIDTH/4, y=SCREEN_HEIGHT/2):
        super().__init__(text, text_col, x, y)
        self.text_size = text_size
       

    def to_screen(self, screen):
        font = pygame.font.SysFont('Arial', self.text_size)
        img = font.render(self.text, True, self.text_col)
        screen.blit(img, self.position)
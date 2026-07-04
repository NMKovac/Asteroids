import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen Width: {SCREEN_WIDTH}\nScreen Height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        x_player = SCREEN_WIDTH/2
        y_player = SCREEN_HEIGHT/2
        new_player = Player(x_player, y_player, PLAYER_RADIUS)
        new_player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

main()
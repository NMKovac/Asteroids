import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen Width: {SCREEN_WIDTH}\nScreen Height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    new_field = AsteroidField()

    x_player = SCREEN_WIDTH/2
    y_player = SCREEN_HEIGHT/2
    new_player = Player(x_player, y_player, PLAYER_RADIUS)
    while True:
        log_state()
        # basically boilerplate for the game environment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # updating and drawing player to screen 
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)

        # checking on each update tick for if an asteroid hit a player
        for asteroid in asteroids:
            if (new_player.collides_with(asteroid)):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

main()
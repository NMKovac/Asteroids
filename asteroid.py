import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self, score) -> int:
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return score + 100
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            vect1 = self.velocity.rotate(angle)
            vect2 = self.velocity.rotate(0-angle)

            new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_1.velocity = vect1 * 1.2
            new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_2.velocity = vect2 * 1.2
            
            return score

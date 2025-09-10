import pygame
import random

from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def set_velocity(self, velocity):
        self.velocity = velocity

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Otherwise spawn new Asteroids
        else:
            # random angle for new moving direction
            rand_angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(rand_angle)
            velocity2 = self.velocity.rotate(-rand_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid1.set_velocity(1.2*velocity1)
            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2.set_velocity(1.2*velocity2)

        

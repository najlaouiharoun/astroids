import pygame
import random

from entities.circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,width=2) 
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid"
        random_angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        sub_asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
        sub_asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
        sub_asteroid1.velocity = vector1 * 1.2
        sub_asteroid2.velocity = vector2 * 1.2

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player

from constants import *
def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    astroids = pygame.sprite.Group()
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (astroids,drawable,updatable)
    AsteroidField.containers = (updatable)
    
    player = Player(x=SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

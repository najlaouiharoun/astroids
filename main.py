# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from entities.asteroidfield import AsteroidField
from entities.asteroid import Asteroid
from entities.player import Player
from entities.shot import Shot

from constants import *
def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable  = pygame.sprite.Group()
  
    Asteroid.containers = (asteroids,drawable,updatable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Shot.containers = (shots,drawable, updatable)
    
    player = Player(x=SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collusion(player):
                sys.exit("Game over!")
            for shot in shots:
                if shot.collusion(asteroid):
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
                        

                        
                    
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

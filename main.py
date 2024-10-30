import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for upd in updatable:
            upd.update(dt)
        
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.detect_collision(asteroid):
                    shot.kill()
                    asteroid.split()            

        screen.fill("black")
        
        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        
        # pause the game loop until 1/60th of a second has passed.
        # delta time: time passed since last tick() was called 
        # converted in seconds from milliseconds
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
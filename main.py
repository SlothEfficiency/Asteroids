import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player1 = Player(x,y)
    asteroidfield = AsteroidField()

    


    while True:
        # make the game closeable
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # delete the last frame
        screen.fill("black")

        # update all objects
        updatable.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.check_collision(player1):
                print("Game over!")
                return
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        
        # draw all objects
        for drawing in drawable:
            drawing.draw(screen)
        
        # track the time
        dt = clock.tick(60)/1000

        # update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

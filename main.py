import pygame
import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Not Asteroids")
    
    my_font = pygame.font.Font(pygame.font.get_default_font(), 30)
    text_surface = my_font.render('Score:', True, (55,25,55))
    text_area = text_surface.get_rect()
    text_area.center = (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 35)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Shot.containers = (shots, updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    score = 0
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                print(f"Congrats on scoring {score} points")
                sys.exit(0)

            for shot in shots:
                if obj.collision(shot):
                    shot.kill()
                    obj.split()
                    score += 1


        screen.fill("black")
        screen.blit(text_surface, text_area)
        score_surface = my_font.render(str(score), True, (55,25,55))
        score_area = score_surface.get_rect()
        score_area.center = (SCREEN_WIDTH - 130, SCREEN_HEIGHT - 35)
        screen.blit(score_surface, score_area)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 fps
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()

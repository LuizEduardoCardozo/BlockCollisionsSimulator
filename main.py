import pygame
from Cubes import * 
from Colision import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,250))
screen.fill((0,255,0))

cubo  = Cubes(screen, 10,  0.1,   10,  (0,255,128))
cubo2 = Cubes(screen, 100, -1, 900, (0,255,255))

while True:

        cubo.move()
        cubo2.move()

        if cubo.checkColision(cubo2) or cubo2.checkColision(cubo):

                v1, v2 = colision(cubo, cubo2)

                cubo.setVelocity(v1)
                cubo2.setVelocity(v2)


        pygame.display.flip()

        screen.fill((0,128,255))
        clock.tick(60)

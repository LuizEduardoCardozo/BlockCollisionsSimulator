import pygame

class Cubes:

    def __init__(self,screen,mass, vel, pos_x, color):
        self.mass = mass
        self.vel = vel
        self.pos_x = pos_x
        self.color = color

        self.screen = screen
        

    def getPosition(self):
        return self.pos_x

    def getVel(self):
        return self.vel
    
    def getMass(self):
        return self.mass

    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos_x,100,60,60))


    def checkColision(self, block):

        # border colision
        if(self.getPosition() < -1):
            self.setVelocity( -1 * self.vel )
        
        delta = self.getPosition() - block.getPosition()

        if(delta < 0):          # module
            delta = -1 * delta

        if(delta < 61):          # smaller than block width, plus one
            return True
        

    def move(self):
        self.pos_x += self.vel
        self.update()


    def setVelocity(self,new_velocity):
        self.vel = new_velocity

import pygame
import random
from physics import *

pygame.init()
wn_x, wn_y = (500, 500)
wn = pygame.display.set_mode((wn_x, wn_y))
pygame.display.set_caption("Black hole");

#######Global physics constants
gravConst = 6.67*10**(-11)
c = 3*10**(8)
#dt = 0.000000001
#print(gravConst)



class Planet():
    def __init__(self, x, y, radius, mass):
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.mass = mass

    def pull(self, moon):
        dst = self.pos - photon.pos
        r = dst.magnitude()
        gravForce = gravConst * self.mass / (r**2)
        print(gravForce)
        #photonVel = dst * gravForce/r
        #photonVelNorm = photonVel * c / gravForce
        #photon.vel = photonVelNorm



    def draw(self,wn):
        xPos = int(self.pos[0])
        yPos = int(self.pos[1])
        pygame.draw.circle(wn, (0,0,255), (xPos, yPos), int(self.radius))

class Moon():
    def __init__(self, x, y, radius, mass):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(c, 0)
        self.mass = mass
        self.radius = radius

    def stop(self):
        self.stopped = True

    def update(self):
        if self.stopped == False:
            self.history.append(self.pos)
        dv = self.vel
        self.pos += dv * dt

        if len(self.history) > 500:
            self.history.pop(0)

    def draw(self, wn):
        pygame.draw.circle(wn, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), self.radius)

        return

def drawScene():
    wn.fill((0,0,0))
    earth.draw(wn)
    #photon.update()
    #blackhole.pull(photon)

    moon.draw(wn)
    pygame.display.update()


earth = Planet(250, 250, scaledEarth, 10000)
moon = Moon(100, 100, scaledMoon, 100)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawScene()

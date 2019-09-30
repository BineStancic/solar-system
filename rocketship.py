import pygame
import random
from physics import *

pygame.init()
wn_x, wn_y = (500, 500)
wn = pygame.display.set_mode((wn_x, wn_y))
pygame.display.set_caption("Orbits");

#######Global physics constants
gravConst = 6.67*10**(-11)
dt = 10000


class Planet():
    def __init__(self, x, y, radius, mass):
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.mass = mass

    def pull(self, body):
        fx, fy = newtonGrav(self.mass, body.mass, self.pos[0], self.pos[1], body.pos[0], body.pos[1])
        body.vel[0] += fx / body.mass * dt
        body.vel[1] += fy / body.mass * dt
        print(body.vel[0], body.vel[1])



    def draw(self,wn):
        xPos = int(self.pos[0])
        yPos = int(self.pos[1])
        pygame.draw.circle(wn, (0,0,255), (xPos, yPos), int(self.radius))

class Moon():
    def __init__(self, x, y, radius, mass):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0.00005, 0)
        self.mass = mass
        self.radius = radius

    def update(self):
        # Update positions
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt

    def draw(self, wn):
        pygame.draw.circle(wn, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), self.radius)

def drawScene():
    wn.fill((0,0,0))
    earth.draw(wn)
    moon.update()
    earth.pull(moon)
    moon.draw(wn)
    pygame.display.update()

####GOES IN MAIN
earth = Planet(250, 250, 20, 10000)
moon = Moon(250, int(100 + scaledDist), 10, 100)


###GOES IN def LOOP
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawScene()

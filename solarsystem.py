import pygame
import random
from physics import *
from OpenGL.GL import *

pygame.init()
wn_x, wn_y = (500, 500)
wn = pygame.display.set_mode((wn_x, wn_y))
pygame.display.set_caption("Orbits");

#######Global physics constants
gravConst = 6.67*10**(-11)
dt = 0.00001

class Sun():
    def __init__(self, x, y, radius, mass):
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.mass = mass

    def pull(self, body):
        fx, fy = newtonGrav(self.mass, body.mass, self.pos[0], self.pos[1], body.pos[0], body.pos[1])
        body.vel[0] += fx / body.mass * dt
        body.vel[1] += fy / body.mass * dt
        #print(body.vel[0], body.vel[1])



    def draw(self,wn):
        xPos = int(self.pos[0])
        yPos = int(self.pos[1])
        pygame.draw.circle(wn, (252, 212, 64), (xPos, yPos), int(self.radius))


class Planet():
    def __init__(self, x, y, radius, mass, vx):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(vx, 0)
        self.radius = radius
        self.mass = mass

    def pull(self, body):
        fx, fy = newtonGrav(self.mass, body.mass, self.pos[0], self.pos[1], body.pos[0], body.pos[1])
        body.vel[0] += fx / body.mass * dt
        body.vel[1] += fy / body.mass * dt
        print(body.vel[0], body.vel[1])

    def update(self):
        # Update positions
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt


    def draw(self,wn):
        xPos = int(self.pos[0])
        yPos = int(self.pos[1])
        pygame.draw.circle(wn, (0,0,255), (xPos, yPos), int(self.radius))

class Moon():
    def __init__(self, x, y, radius, mass, vx):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(vx, 0)
        self.mass = mass
        self.radius = radius

    def update(self):
        # Update positions
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt

    def draw(self, wn):
        pygame.draw.circle(wn, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), self.radius)


def drawScene(sun, earth, moon):
    wn.fill((0,0,0))
    earth.draw(wn)
    moon.update()
    earth.pull(moon)
    earth.update()
    sun.pull(earth)
    sun.draw(wn)
    moon.draw(wn)
    pygame.display.update()

def loop(sun, earth, moon):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #if event.type ==pygame.MOUSEBUTTONDOWN:
            #    print(event)
            #    print(event.button)

            #    if event.button == 4:
            #        glTranslatef(0.0,0.0,1.0)
            #    elif event.button == 5:
            #        glTranslatef(0.0, 0.0, -1.0)

        drawScene(sun, earth, moon)

def main():
    sun = Sun(250, 250, 20, scaledSunMass)
    earth = Planet(250, int(250 + scaledEarthSun), 5, scaledEarthMass, earthV)
    moon = Moon(250, int(250 +scaledEarthSun+ scaledEarthMoon), 1, scaledMoonMass, 3800)
    loop(sun, earth, moon)

if __name__ == '__main__':
    main()

pygame.quit()

import math
import sys
#print(sys.maxsize)


gravConst = 6.67*10**(-11)


def newtonGrav(m1, m2, x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    r = math.sqrt(dx**2 + dy**2)
    F = gravConst*m1*m2/(r**2)

    theta = math.atan2(dy, dx)
    fx = math.cos(theta) * F
    fy = math.sin(theta) * F
    return fx, fy


def orbitVel(m, r):
    v = math.sqrt(gravConst*m/(r))
    return v


massEarth = 5.972e24
massMoon = 7.348e22
massSun = 1.9891e30

rEarth = 6.371e6
rMoon = 1.737e6
rSun = 6.95510e8

distToMoon = 3.844e8
distToSun = 1.496e11


def scale(param):
    #scaled = param*5.3e-7              #SCALE FOR EARTH MOON
    scaled = param*1.3368984e-9         #SCALE FOR SUN
    return scaled

scaledEarth = scale(rEarth)
scaledMoon = scale(rMoon)
scaledSun = scale(rSun)

scaledEarthMass = scale(massEarth)
scaledMoonMass = scale(massMoon)
scaledSunMass = scale(massSun)

scaledEarthMoon = scale(distToMoon)
scaledEarthSun = scale(distToSun)

#print(scaledEarthSun)
#print(scaledEarthMoon)
#print(scaledEarth)
#print(scaledSun)

moonV = 1.022e3
earthV = 2.9722e4

#SCALING VELOCITY BREAKES the sim
scaledMoonV = scale(moonV)
scaledEarthV = scale(earthV)
#print(scaledMoonV)

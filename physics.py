import math


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

#def gravField(m, r):
#    g = gravConst*m/(r**2)
#    return g

def orbitVel(m, r):
    v = math.sqrt(gravConst*m/(r))
    return v


massEarth = 5.972 * 10 **(24)
massMoon = 7.348 * 10 **(22)
#massSun = 3.48 * 10**(30)

rEarth = 6.371 * 10 **(6)
rMoon = 1.737 * 10 **(6)
#rSun = 6.95* 10 **(8)

def scaleDist(dist):
    scaledDist = dist/(1000000**6)
    return int(scaledDist)

scaledEarth = scaleDist(rEarth)
scaledMoon = scaleDist(rMoon)

distToMoon = 3.844 * 10 **(8)

scaledDist = scaleDist(distToMoon)

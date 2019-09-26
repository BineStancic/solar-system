


def newtonGrav(m1, m2, r):
    F = gravConst*m1*m2/(r**2)
    return F

def gravField(m, r):
    g = gravConst*m/(r**2)
    return g


massEarth = 5.972 * 10 **(24)
massMoon = 7.348 * 10 **(22)

rEarth = 6.371 * 10 **(6)
rMoon = 1.737 * 10 **(6)

def scaleDist(dist):
    scaledDist = dist/(10**6)
    return int(scaledDist)

scaledEarth = scaleDist(rEarth)
scaledMoon = scaleDist(rMoon)

distToMoon = 3.844 * 10 **(8)

moonOrbitSpeed = 1.022 * 10 **(3)

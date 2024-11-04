from math import *
def makeDegrees(rad):
    return 180*(rad/pi)
def makeRadians(angle):
    return pi*(angle/180)
def string_angle(angle):
    return f"{angle/pi} pi"
print(makeDegrees(pi))
print(string_angle(makeRadians(180)))


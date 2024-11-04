from math import *
def makeDegrees(rad):
    return 180*(rad/pi)
def makeRadians(angle):
    return pi*(angle/180)
def string_angle(angle):
    return f"{angle/pi} pi"
def ask(prompt):
    return(input(prompt+'\n>>> '))
def searchList(quarry,list):
    for item in list:
        if item == quarry:
            return True
    return False

list = [4,7,'penguin','potato','bicycle']
if searchList('potato',list):
    print('dinosaur')
else:
    print('something is wrong')

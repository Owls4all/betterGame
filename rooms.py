import random as r
from utility import *
class Room:
    def __init__(self,exits=[None,None,None,None],trueExits=[None,None,None,None],connections=0):
        self.exits=exits
        self.trueExits=trueExits
        self.connections=connections
    def orient(self,entry):
        if entry == '0':
            self.exits =[self.trueExits[1],self.trueExits[0],self.trueExits[3],self.trueExits[2]]
        if entry == '1':
            self.exits =[self.trueExits[0],self.trueExits[1],self.trueExits[2],self.trueExits[3]]
        if entry == 2:
            self.exits =[self.trueExits[2],self.trueExits[3],self.trueExits[1],self.trueExits[0]]
        if entry == 3:
            self.exits =[self.trueExits[3],self.trueExits[2],self.trueExits[0],self.trueExits[1]]
        
#rooms have 'forward, back, left, right' ->this is determined by player's point of entry
# they also have 'north south west east' ->this is absolute direction
surface=Room
#1st floor rooms (some variation may occur)
steps0=Room
r00=Room
r01=Room
r02=Room
r03=Room
r04=Room
r05=Room
r06=Room
r07=Room
r08=Room
r09=Room
steps1=Room
#2nd floor rooms (some variation may occur)
steps2=Room
r10=Room
r11=Room
r12=Room
r13=Room
r14=Room
steps3=Room
#3rd floor rooms (some variation may occur)
steps4=Room

allTheRooms=[surface,steps0,r00,r01,r02,r03,r04,r05,r06,r07,r08,r09,steps1]
floorBreaks=[steps2,steps4]
generatedRooms=[surface]
def keepRolling(room):
    way = r.randint(0,4)
    if room.trueExits[way] == None:
        return way
    else:
        keepRolling(room)
def genfloor(room:Room):
    wayBack=r.randint(0,4)
    room.trueExits[wayBack]=surface   
    paths=r.randint(0,3)
    if paths >= 1:
        direction=keepRolling(steps0)
        room.TrueExits[direction] = allTheRooms[len(generatedRooms)]
        generatedRooms.append(room.TrueExits[direction])
    if paths >= 2:
        keepRolling(steps0)
    if paths >= 3:
        keepRolling(steps0)
    room.orient(wayBack)
def genDungeon(firstRoom):
    currentFloor = 0
    while indexInList(floorBreaks[currentFloor],allTheRooms) <= len(generatedRooms):
        genfloor(floorBreaks[currentFloor])
    currentFloor=currentFloor+1
    if currentFloor >= 3:
        pass
    else:
        genDungeon(generatedRooms+1)

genDungeon(steps0)

print(steps0.trueExits)
print(r00.trueExits)

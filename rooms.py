import random as r
from utility import *
class Room:
    def __init__(self,left=None,right=None,forward=None,back=None,floor=0,north=None,south=None,east=None,west=None):
        self.l=left
        self.r=right
        self.f=forward
        self.b=back
        self.floor=floor
        self.n =north
        self.s = south
        self.e = east
        self.w = west
        list_of_things=[]
        for thing in [self.n,self.s,self.e,self.w]:
            if thing != None:
                list_of_things.append(thing)
        self.exitsNumber=len(list_of_things)-1
    def orient(self,entry):
        if searchList(entry,["north",0]):
            self.f=self.s
            self.b=self.n
            self.l=self.e
            self.r=self.w
        elif entry == "west":
            self.f=self.e
            self.l=self.n
            self.b=self.w
            self.r=self.s
        elif entry == 'south':
            self.f=self.n
            self.l=self.w
            self.r=self.e
            self.b=self.s
        else:
            self.f=self.w
            self.b=self.e
            self.l=self.s
            self.r=self.n
        
#rooms have 'forward, back, left, right' ->this is determined by player's point of entry
# they also have 'north south west east' ->this is absolute direction

#1st floor rooms
steps0=Room
r00=Room
r01=Room
r02=Room
r03=Room
r04=Room
r05=Room
r06=Room
r07=Room
steps1=Room

# first floor map assembly

steps0.s=r00

r00.n=steps0
r00.w=r01

r01.e=r00
r01.n=r02

r02.s=r01
r02.w=r03
r02.n=r04

r03.e=r02

r04.s=r02
r04.e=r05
r04.n=r06

r05.w=r04

r06.s=r04
r06.w=r07
r06.e=steps1

steps1.w=r06

#2nd floor rooms 
steps2=Room
r10=Room
r11=Room
r12=Room
r13=Room
r14=Room
r15=Room
r16=Room
r17=Room
steps3=Room

#2nd floor map assembly

#3rd floor rooms 
steps4=Room
r20=Room
r21=Room
r22=Room
r23=Room
r24=Room
r25=Room
r26=Room
r27=Room
steps5=Room

#3rd floor map assembly


# Special Rooms
surface=Room
bossfight=Room

stairs=[steps0,steps1,steps2,steps3,steps4,steps5]
directions=['s','w','n','w','w','s']
floors=[0,0,1,1,2,2]
def pruneFloors(floor):
    while searchList(floor,floors):
        stairs.__delitem__(indexInList(floor,floors))
        directions.__delitem__(indexInList(floor,floors))
        floors.__delitem__(indexInList(floor,floors))
def genDungeon():
    #choose first floor + staircase
    firstStair=r.randint(0,5)
    if firstStair == 0 or firstStair == 5:
        surface.s=stairs[firstStair]
        stairs[firstStair].n=surface
    elif searchList(firstStair,[1,3,4]):
        surface.w=stairs[firstStair]
        stairs[firstStair].e=surface
    else:
        surface.n=steps2
        steps2.s=surface 
    firstFloor=floors[firstStair]
    if firstStair % 2 == 0:
        nextDescent = stairs[firstFloor+1]
    else:
        nextDescent = stairs[firstFloor-1]
    wayDown = directions[indexInList(nextDescent,stairs)]
    pruneFloors(firstFloor)
    #
    secondStairs=r.randint(0,3)
    if directions[secondStairs] == 's':
        stairs[secondStairs].n = nextDescent
        if nextDescent.s != None:
            pass #figure something out
        else:
            nextDescent.s = stairs[secondStairs]
            secondFloor = floors[secondStairs]
    elif directions[secondStairs]== 'n':
        stairs[secondStairs].s = nextDescent
        if nextDescent.s != None:
            pass #figure something out
        else:
            nextDescent.n = stairs[secondStairs]
            secondFloor = floors[secondStairs]
    else:
        stairs[secondStairs].e=nextDescent
        if nextDescent.w != None:
            pass #figure something out
        else:
            nextDescent.w = stairs[secondStairs]
    
    #designate 4th stair
    pruneFloors[secondFloor]
    #choose 5th stair
    #assign bossfight to 6th stair
    



    
    
    
    
    
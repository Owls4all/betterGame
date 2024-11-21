import random as r
from utility import *
no= 'Nothing'
class Room:
    def __init__(self,desc='a room',left='Nothing',right='Nothing',forward='Nothing',back='Nothing',floor=0,north='Nothing',south='Nothing',east='Nothing',west='Nothing',stairConnection='Nothing'):
        self.l=left
        self.r=right
        self.f=forward
        self.b=back
        self.floor=floor
        self.n =north
        self.s = south
        self.e = east
        self.w = west
        self.stair = stairConnection
        self.facing = 'north'
        self.desc=desc
        list_of_things=[]
        for thing in [self.n,self.s,self.e,self.w]:
            if thing != 'Nothing':
                list_of_things.append(thing)
        self.exitsNumber=len(list_of_things)-1
    def orient(self,entry):
        if searchList(entry,["north",0]):
            self.f=self.s
            self.b=self.n
            self.l=self.e
            self.r=self.w
            self.facing = 'south'
        elif entry == "west":
            self.f=self.e
            self.l=self.n
            self.b=self.w
            self.r=self.s
            self.facing = 'east'
        elif entry == 'south':
            self.f=self.n
            self.l=self.w
            self.r=self.e
            self.b=self.s
            self.facing = 'north'
        elif entry == 'east':
            self.f=self.w
            self.b=self.e
            self.l=self.s
            self.r=self.n
            self.facing = 'west'
        elif self.stair !='Nothing':
            if self.w != 'Nothing':
                self.orient('east')
            if self.e != 'Nothing':
                self.orient('west')
            if self.n != 'Nothing':
                self.orient('south')
            if self.s != 'Nothing':
                self.orient('north')
        #making descriptions
        if self.stair != 'Nothing':
            desc='A room with stairs'
        else:
            if self.l != 'Nothing':
                if self.r != 'Nothing':
                    if self.f != 'Nothing':
                        self.desc='There are doors to the left, to the right, and straight ahead'
                    else:
                        self.desc='There are doors to the left and to the right'
                else:
                    if self.f != no:
                        self.desc= 'There is a door to the left and a door straight ahead'
                    else:
                        self.desc='there is a door to the left'
            else:
                if self.r != no:
                    if self.f != no:
                        self.desc ='there is a door to the right and a door straight ahead'
                    else:
                        self.desc='there is a door to the right'
                else:
                    if self.f != no:
                        self.desc = 'there is a door straight ahead'
                    else:
                        self.desc = 'it is a dead end'
#rooms have 'forward, back, left, right' ->this is determined by player's point of entry
# they also have 'north south west east' ->this is absolute direction

#1st floor rooms
steps0=Room()
r00=Room()
r01=Room()
r02=Room()
r03=Room()
r04=Room()
r05=Room()
r06=Room()
r07=Room()
steps1=Room()

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

steps2=Room()
r10=Room()
r11=Room()
r12=Room()
r13=Room()
r14=Room()
r15=Room()
r16=Room()
r17=Room()
steps3=Room()

#2nd floor map assembly

steps2.n = r10

r10.s = steps2
r10.e = r11

r11.w = r10
r11.s=r12
r11.e=steps3
r11.n=r13

r12.n=r11

r13.s=r11
r13.e=r14
r13.n=r15

r14.w=r13

r15.s=r13
r15.w=r16

r16.e=r15
r16.s=r17

r17.e=r16

steps3.w=r11

#3rd floor rooms 
steps4=Room()
r20=Room()
r21=Room()
r22=Room()
r23=Room()
r24=Room()
r25=Room()
r26=Room()
r27=Room()
steps5=Room()

#3rd floor map assembly
steps4.w=r20

r20.e=steps4
r20.w=r21
r20.n=r22
r20.s=r24

r21.e=r20

r22.s=r20
r22.e=r23

r23.w=r22

r24.n=r22
r24.e=r25
r24.s=r26

r25.w=r24

r26.n=r24
r26.w=r27

r27.e=r26
r27.n=steps5

steps5.s=r27

# Special Rooms
surface=Room()
bossfight=Room()


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
    surface.stair = stairs[firstStair]
    stairs[firstStair] = surface
    firstFloor=floors[firstStair]

    if firstStair % 2 == 0:
        nextDescent = stairs[firstFloor+1]
    else:
        nextDescent = stairs[firstFloor-1]
    pruneFloors(firstFloor)
    #next floor

    secondStairsUp=r.randint(0,3)
    stairs[secondStairsUp].stair = nextDescent
    nextDescent.stair=stairs[secondStairsUp]
    secondFloor = floors[secondStairsUp]

    if secondStairsUp%2 == 0:
        fourthStair = stairs[secondStairsUp+1]
    else:
        fourthStair = stairs[secondStairsUp-1]

    pruneFloors(secondFloor)
    

    #choose 5th stair
    anotherStair =r.randint(0,1)
    fourthStair.stairs = stairs[anotherStair]
    stairs[anotherStair] = fourthStair

    if anotherStair %2 ==0:
        finalStair = stairs[anotherStair+1]
    else:
        finalStair = stairs[anotherStair-1]

    finalStair.stair = bossfight
    bossfight.stair = finalStair
    
genDungeon()

def travelBetweenRooms(room:Room):
    print(room.desc)
    angles=['east','north','west','south']
    options = ['back']
    if room.stair != 'Nothing':
        options.append("stairs")
    if room.l != 'Nothing':
        options.append('left')
    if room.f != 'Nothing':
        options.append('forward')   
    if room.r != 'Nothing':
        options.append('right')
    
    choice = ask('Which way do you want to go\n'+str(options))
    if not searchList(choice,options):
        print("you can't go that way from here!")
        travelBetweenRooms(room)
    else:
        if choice == 'stairs':
            newRoom = room.stair
            facing = 'stair'
            
        elif choice == 'forward':
            newRoom = room.f
            facing = room.facing
        elif choice == 'back':
            newRoom = room.b
            facing = angles[indexInList('backward',angles)+2]   
        elif choice == 'left':
            newRoom = room.l
            facing = angles[indexInList('backward',angles)+1]   
        elif choice == 'right':
            newRoom = room.r
            facing = angles[indexInList('backward',angles)+3]  
        if newRoom == 'Nothing':
            newRoom=room.stair  
        newRoom.orient(facing)
        travelBetweenRooms(newRoom)
travelBetweenRooms(surface)
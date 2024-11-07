import random as r
from utility import *
class Room:
    def __init__(self,left,right,forward,back,floor,north,south,east,west):
        self.l=left
        self.r=right
        self.f=forward
        self.b=back
        self.floor=floor
        self.n =north
        self.s = south
        self.e = east
        self.w = west
    def orient(self,entry):
        i = 7           
        
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
r15=Room
steps3=Room
#3rd floor rooms (some variation may occur)
steps4=Room



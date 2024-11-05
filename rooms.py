import random as r
import utility
class Room:
    def __init__(self,level):
        self.level=level
    def orient(self,entry):
        if entry == 'north':
            self.exits =[self.south,self.north,self.west,self.east]
#rooms have 'forward, back, left, right' -> this is determined by player's point of entry
# they also have 'north south west east' -> this is absolute direction

steps0=Room(0)

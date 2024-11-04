import turtle 
from tkinter import *
import utility 
import time


core = Tk()
core.title('Super epic game (definitely no exaggeration whatsoever)')
#-------------Variable setup------------------#
Stats = ['strength','defense','health','agility','inteligence']
class Item:
    def __init__(self,slot,name,strength,defense,health,agility,intelligence):
        self.slot=slot
        self.name=name
        self.strength=strength
        self.defense=defense
        self.health = health
        self.agility = agility
        self.intelligence = intelligence
        

#---------------------------------------------#
menubar = Menu(core)
#------------------Game Menu------------------#
game = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Game', menu = game)
game.add_command(label='Save', command = None)
game.add_command(label='Load', command = None)
game.add_command(label='Quit', command = core.destroy)
#---------------------------------------------#

#----------------Actions Menu-----------------#
actions = Menu(menubar,tearoff=0)
menubar.add_cascade(label= 'Actions', menu = actions)
actions.add_command(label= 'Attack', command = None)
actions.add_command(label= 'Focus', command = None)
#---------------------------------------------#

#-----------------Magic Menu------------------#
magic = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Magic',menu=magic)
#---------------------------------------------#

#---------------Inventory Menu----------------#
stuff = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Inventory',menu=stuff)

#---------------------------------------------#

core.config(menu = menubar)
mainloop()


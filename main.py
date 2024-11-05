import turtle 
from tkinter import *
import utility 
import random
from items import *
from rooms import *

core = Tk()
core.title('Super epic game (definitely no exaggeration whatsoever)')
#-------------Variable setup------------------#
# Stats are strength, defense, health, agility, inteligence
#items have a slot, and, when found, can be equipped in that slot.
#there exists one of each item, and they are either in the 'not found' list or the '[slot]' list
#the slots for items are head, neck, chest, belt, feet, hands, arms, weapon
  

helmets=[noHelm,cardboardHelm]
necklaces=[noNecklace]
armors=[noArmor,tunic]
belts=[noBelt]
boots=[noBoots,wornBoots]
gloves=[noGloves]
bracers=[noBracers]
weapons=[noWeapon,rustyBlade]

undiscovered=[speedPendant,scaleMail,mithrilGloves,strengthBelt,armorBracers]

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


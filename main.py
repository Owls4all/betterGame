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
baseStats=[5,0,100,0,50]
class Entity:
    def __init__(self,helmet,necklace,armor,belt,shoes,gloves,bracers,weapon,location,loot):
        #define equipment
        self.helmet=helmet
        self.necklace=necklace
        self.armor=armor
        self.belt=belt
        self.shoes=shoes
        self.gloves=gloves
        self.bracers=bracers 
        self.weapon=weapon
        self.location=location
        self.loot=loot
    def stats(self):
        #stats
        self.strength=baseStats[0]+self.helmet.strength+self.necklace.strength+self.armor.strength+self.belt.strength+self.shoes.strength+self.gloves.strength+self.bracers.strength+self.weapon.strength
        self.defense=baseStats[1]+self.helmet.defense+self.necklace.defense+self.armor.defense+self.belt.defense+self.shoes.defense+self.gloves.defense+self.bracers.defense+self.weapon.defense
        self.health=baseStats[2]+self.helmet.health+self.necklace.health+self.armor.health+self.belt.health+self.shoes.health+self.gloves.health+self.bracers.health+self.weapon.health
        self.agility=baseStats[3]+self.helmet.agility+self.necklace.agility+self.armor.agility+self.belt.agility+self.shoes.agility+self.gloves.agility+self.bracers.agility+self.weapon.agility
        self.intelligence=baseStats[4]+self.helmet.intelligence+self.necklace.intelligence+self.armor.intelligence+self.belt.intelligence+self.shoes.intelligence+self.gloves.intelligence+self.bracers.intelligence+self.weapon.intelligence
    def monsterstats(self,strength,defense,health,agility,intelligence):
        self.strength=strength+self.helmet.strength+self.necklace.strength+self.armor.strength+self.belt.strength+self.shoes.strength+self.gloves.strength+self.bracers.strength+self.weapon.strength
        self.defense=defense+self.helmet.defense+self.necklace.defense+self.armor.defense+self.belt.defense+self.shoes.defense+self.gloves.defense+self.bracers.defense+self.weapon.defense
        self.health=health+self.helmet.health+self.necklace.health+self.armor.health+self.belt.health+self.shoes.health+self.gloves.health+self.bracers.health+self.weapon.health
        self.agility=agility+self.helmet.agility+self.necklace.agility+self.armor.agility+self.belt.agility+self.shoes.agility+self.gloves.agility+self.bracers.agility+self.weapon.agility
        self.intelligence=intelligence+self.helmet.intelligence+self.necklace.intelligence+self.armor.intelligence+self.belt.intelligence+self.shoes.intelligence+self.gloves.intelligence+self.bracers.intelligence+self.weapon.intelligence
   
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


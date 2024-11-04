import turtle 
from tkinter import *
import utility 
import time


core = Tk()
core.title('I can set text here aparently')

menubar = Menu(core)
#------------------Game Menu------------------#
game = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Game',menu=game)
'[Other Game menu commands here]'
game.add_command(label='Quit',command=core.destroy)
#----------------Actions Menu-----------------#
actions = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Actions',menu = actions)
actions.add_command(label='Attack', command = None)

#-----------------Magic Menu------------------#
magic = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Magic',menu=magic)

core.config(menu = menubar)
mainloop()


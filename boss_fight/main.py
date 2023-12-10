from tkinter import *
import os

from constants import WIDTH, HEIGHT
from entities.player import Player
from entities.boss import Boss
from entities.estus_flask import EstustFlask
from ui.game_ui import GameUI

#get the directory for assets and join them
scriptDirectory = os.path.dirname(os.path.abspath(__file__))
assetsDirectory = os.path.join(scriptDirectory, 'assets')

def fullscreen(event):
    current_state = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not current_state)

def bindKeys():
    canvas.bind("<F11>", fullscreen)
    canvas.bind("a", player.moveLeft)
    canvas.bind("d", player.moveRight)
    canvas.bind("<space>", player.jump)

#main function

#create root
root = Tk()
root.title('Title')
#create canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()
canvas.focus_set()
#import images
rune_background = PhotoImage(file=os.path.join(assetsDirectory, 'rune_background.PNG'))
rune_frame = PhotoImage(file=os.path.join(assetsDirectory, 'rune_frame.PNG'))
#create objects
player = Player(canvas, name='Player1', healthPoints=700, mana=200, stamina=500)
boss = Boss(canvas, name='Malenia, Blade of Miquella', healthPoints=800)
estustFlask = EstustFlask(quantity=12, healing=280)
gameUI = GameUI(canvas, player, boss, rune_background, rune_frame)

bindKeys()

root.mainloop()
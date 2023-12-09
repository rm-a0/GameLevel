from tkinter import *
from constants import WIDTH, HEIGHT
from entities.player import Player
from entities.boss import Boss
from entities.estus_flask import EstustFlask
from ui.game_ui import GameUI

def placeBackground():
    print('TODO 1')

# program start
root = Tk()
root.title('Title')
root.attributes('-fullscreen', True)

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()
canvas.focus_set()

player = Player(canvas, name='Player1', healthPoints=700, mana=200, stamina=500)
boss = Boss(canvas, name='Malenia, Blade of Miquella', healthPoints=800)
estustFlask = EstustFlask(quantity=12, healing=280)
gameUI = GameUI(canvas, player, boss)

canvas.bind("a", player.moveLeft)
canvas.bind("d", player.moveRight)
canvas.bind("w", player.jump)

root.mainloop()
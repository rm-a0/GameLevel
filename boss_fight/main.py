from tkinter import *
import os

from constants import WIDTH, HEIGHT, DELAY
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
    #UI RELEATED KEYBINDS
    canvas.bind("<F11>", fullscreen)

    #PLAYER RELEATED KEYBINDS
    #fix clunky movement in the future - refine left and right movement (probably not happening cuz tkinter is shit)
    #make jumping more realistic - add exponential and log fucntions
    canvas.bind("<KeyPress-a>", player.moveLeft)
    canvas.bind("<KeyRelease-a>", player.stopMoveLeft)
    canvas.bind("<KeyPress-d>", player.moveRight)
    canvas.bind("<KeyRelease-d>", player.stopMoveRight)
    canvas.bind("<space>", player.jump)
    canvas.bind("<KeyPress-Shift_L>", player.roll)
    canvas.bind("<Button-1>", player.attack)

    #ITEM RELEATED KEYBINDS
    canvas.bind("<e>", lambda event: estustFlask.heal(player, event))

def updateGame():
    #converts delay to seconds
    dt = DELAY / 1000.0

    #update entities
    player.updatePosition(dt)
    player.applyGravity(dt)
    player.refillStamina()

    #update UI
    gameUI.updateHealthBar()
    gameUI.updateStaminaBar()
    gameUI.updateManaBar()

    #recursive call
    canvas.after(DELAY, updateGame)

#MAIN FUNCTION

#create root
root = Tk()
root.title('Title')
#create canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()
canvas.focus_set()
#import images
rune_background = PhotoImage(file=os.path.join(assetsDirectory, 'rune_background.PNG'))
rune_frame = PhotoImage(file=os.path.join(assetsDirectory, 'rune_frame.PNG'))
godricks_rune = PhotoImage(file=os.path.join(assetsDirectory, 'godricks_rune.PNG'))
#create objects
player = Player(canvas, name='Player1', healthPoints=800, mana=100, stamina=700)
boss = Boss(canvas, name='Boss1', healthPoints=800)
estustFlask = EstustFlask(quantity=12, healing=280)
gameUI = GameUI(canvas, player, boss, rune_background, rune_frame, godricks_rune)

bindKeys()

#game loop
canvas.after(DELAY, updateGame)

#delete later
print(f"delay: {DELAY} ms")
print(f"delta time: {DELAY/1000} ms")

root.mainloop()
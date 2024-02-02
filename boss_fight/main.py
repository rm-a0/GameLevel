from tkinter import *
import os

from constants import WIDTH, HEIGHT, DELAY, DAMAGE
from entities.player import Player
from entities.weapon import Weapon
from entities.boss import Boss
from entities.estus_flask import EstusFlask
from entities.spell import Spell
from ui.game_ui import GameUI

#get the directory for assets and join them
scriptDirectory = os.path.dirname(os.path.abspath(__file__))
assetsDirectory = os.path.join(scriptDirectory, 'assets')

def fullscreen(event, root):
    current_state = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not current_state)

def disableMouse(event):
    return "break"

def healEvent(event, player, estusFlask, gameUI):
    player.stopMovement(1000)
    estusFlask.heal(player, event)
    gameUI.updateEstusFlaskCounter(event)

def bindKeys(canvas, player, boss, estusFlask, gameUI):
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
    canvas.bind("<Button-1>", lambda event: player.attack(boss, event))

    #ITEM AND SPELL RELEATED KEYBINDS
    canvas.bind("e", lambda event: healEvent(event, player, estusFlask, gameUI))
    canvas.bind("<Button-5>", lambda event: player.castSpell(player.spells[0], boss, event))
    canvas.bind("<Button-4>", lambda event: player.castSpell(player.spells[1], boss, event))


def checkGameEnd(canvas, player, boss):
    if player.healthPoints <= 0:
        canvas.create_text(WIDTH/2, HEIGHT/2, text="YOU DIED", font=("Helvetica", 18), fill="red")
        return True
    elif boss.healthPoints <= 0:
        canvas.create_text(WIDTH/2, HEIGHT/2, text="YOU WON", font=("Helvetica", 18), fill="red")
        return True
    else:
        return False

def updateGame(canvas, player, boss, gameUI):
    try: 
        #converts delay to seconds
        dt = DELAY / 1000.0

        if checkGameEnd(canvas, player, boss) == False:
            #update player
            player.updatePosition(dt)
            player.applyGravity(dt)
            player.refillStamina()
            #player.applyStatusEffect()

            #update boss
            boss.updatePosition(dt)

            #update UI
            gameUI.updatePlayerHealthBar()
            gameUI.updateBossHealthBar()
            gameUI.updateStaminaBar()
            gameUI.updateManaBar()

            #recursive call
            canvas.after(DELAY, updateGame, canvas, player, boss, gameUI)
    except: 
        print("Error updating game")

def main():
    #create root
    root = Tk()
    root.title('Title')

    #create canvas
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
    canvas.pack()
    canvas.focus_set()

    #disable cursor and mouse movement
    root.config(cursor="none")

    #import images
    rune_background = PhotoImage(file=os.path.join(assetsDirectory, 'rune_background.PNG'))
    rune_frame = PhotoImage(file=os.path.join(assetsDirectory, 'rune_frame.PNG'))
    godricks_rune = PhotoImage(file=os.path.join(assetsDirectory, 'godricks_rune.PNG'))

    #create objects
    player = Player(canvas, name='Player', healthPoints=800, mana=100, stamina=700)
    weaponSpell = Spell(canvas, name='Weapon Spell', effect=DAMAGE, magnitude=200, manaCost=50, castDuration=1000)
    weapon = Weapon(canvas, name='Sword', damage=100, weight=50, length=150, width=10, spell=weaponSpell)
    boss = Boss(canvas, name='Boss', healthPoints=900)
    estusFlask = EstusFlask(quantity=12, healing=280)

    gameUI = GameUI(canvas, player, boss, estusFlask, rune_background, rune_frame, godricks_rune)

    #equip weapon and spells
    player.equipWeapon(weapon)
    player.equipSpell(weapon.spell, 0)

    #pass boss and player instance to each other (used for interaciton)
    player.createBossInstance(boss)
    boss.createPlayerInstance(player)

    #bind keys
    bindKeys(canvas, player, boss, estusFlask, gameUI)

    #game loop
    canvas.after(DELAY, updateGame, canvas, player, boss, gameUI)

    #delete later
    print(f"delay: {DELAY} ms")
    print(f"delta time: {DELAY/1000} ms")

    root.mainloop()

if __name__ == "__main__":
    main()
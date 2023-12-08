from tkinter import *

class Player:
    def __init__(self, canvas, name, healthPoints, mana, stamina):
        self.canvas = canvas
        self.name = name
        self.healthPoints = healthPoints
        self.mana = mana
        self.stamina = stamina
        self.speed = 10
        #starting coordinates and dimensions of a player object
        self.x = 200
        self.y = HEIGHT - 250
        self.height = 100
        self.width = 60
        #creating hitbox for a character
        self.hitbox = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline='green')
        
        canvas.bind("w", self.jump)
        canvas.bind("a", self.moveLeft)
        canvas.bind("d", self.moveRight)

    def jump(self, event):
        print("TODO")

    def moveLeft(self, event):
        self.canvas.move(self.hitbox, -self.speed, 0)

    def moveRight(self, event):
        self.canvas.move(self.hitbox, self.speed, 0)


class Boss:
    def __init__(self, canvas, name, healthPoints):
        self.canvas = canvas
        self.name = name
        self.healthPoints = healthPoints
        #starting coordinates and dimensions of a boss object
        self.x = WIDTH - 200
        self.y = HEIGHT - 250
        self.height = 100
        self.width = 60
        #creating hitbox for a boss
        self.hitbox = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline='red')

class EstustFlask:
    def __init__(self, quantity, healing):
        self.quantity = quantity
        self.healing = healing

class GameUI:
    def __init__(self, canvas, player, boss):
        self.canvas = canvas
        self.player = player
        self.boss = boss
        
        self.playerRune = self.createRune()
        self.playerHealthBar = self.createBar(100, 30, player.healthPoints, 'red')
        self.playerManaBar = self.createBar(100, 50, player.mana, 'blue')
        self.playerStaminaBar = self.createBar(100, 70, player.stamina, 'green')

        self.estusFlaskSlot = self.createItemSlot(50, HEIGHT-180)
        self.weaponSlot = self.createItemSlot(120, HEIGHT-220)
        self.emptySlot1 = self.createItemSlot(120, HEIGHT-130)
        self.emptySlot2 = self.createItemSlot(190, HEIGHT-180)

        self.bossHealthBar = self.createBar(400, HEIGHT-100, boss.healthPoints, 'red')

    def createRune(self):
        x = 20
        y = 20
        runeSize = 70
        rune = self.canvas.create_rectangle(x, y, x + runeSize, y + runeSize, fill='black')
        return rune

    def createItemSlot(self, x, y):
        slotWidth = 60
        slotHeight = 80
        rune = self.canvas.create_rectangle(x, y, x + slotWidth, y + slotHeight, fill='black')
        return rune

    def createBar(self, x, y, barWidth, color):
        barHeight = 10
        bar = self.canvas.create_rectangle(x, y, x + barWidth, y + barHeight, fill=color)
        return bar

def placeBackground():
    print('TODO 1')

# program start
root = Tk()
root.title('Title')

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

player = Player(canvas, name='Player1', healthPoints=700, mana=200, stamina=500)
boss = Boss(canvas, name='Malenia, Blade of Miquella', healthPoints=800)
estustFlask = EstustFlask(quantity=12, healing=280)
gameUI = GameUI(canvas, player, boss)

canvas.focus_set()
canvas.bind("<Key>", lambda event: player.moveLeft(event) if event.char == "a" else player.moveRight(event) if event.char == "d" else None)

root.mainloop()
from constants import HEIGHT

class GameUI:
    def __init__(self, canvas, player, boss, estusFlask, rune_background, rune_frame, chosen_rune):
        self.canvas = canvas
        self.player = player
        self.boss = boss
        self.estusFlask = estusFlask
        
        self.playerRune = self.createRune(rune_background, rune_frame, chosen_rune)
        self.playerHealthBar = self.createHealthBar()
        self.playerManaBar = self.createManaBar()
        self.playerStaminaBar = self.createStaminaBar()
        #self.borders = self.createBorders()

        self.estusFlaskSlot = self.createItemSlot(50, HEIGHT-180)
        self.estusFlaskCounter = self.createEstusFlaskCounter(50, HEIGHT-180)
        self.weaponSlot = self.createItemSlot(120, HEIGHT-220)
        self.emptySlot1 = self.createItemSlot(120, HEIGHT-130)
        self.emptySlot2 = self.createItemSlot(190, HEIGHT-180)

        #self.bossHealthBar = self.createBar(400, HEIGHT-100, boss.healthPoints, 'red')

    def createRune(self, rune_background, rune_frame, chosen_rune):
        x = 20
        y = 20
        rune = self.canvas.create_image(x, y, anchor="nw", image=rune_background)
        rune = self.canvas.create_image(x, y, anchor="nw", image=rune_frame)
        rune = self.canvas.create_image(x, y, anchor="nw", image=chosen_rune)
        return rune

    def createHealthBar(self):
        x = 150
        y = 60
        healthBar = self.canvas.create_rectangle(x, y, x + self.player.healthPoints, y - 16, fill='red', outline='')
        return healthBar
    
    def updateHealthBar(self):
        x = 150
        y = 60
        self.canvas.coords(self.playerHealthBar, x, y, x + self.player.healthPoints, y - 16)

    def createManaBar(self):
        x = 150
        y = 90
        manaBar = self.canvas.create_rectangle(x, y, x + self.player.mana, y - 16, fill='blue', outline='')
        return manaBar
    
    def updateManaBar(self):
        x = 150
        y = 90
        self.canvas.coords(self.playerManaBar, x, y, x + self.player.mana, y - 16)
    
    def createStaminaBar(self):
        x = 150
        y = 120
        staminaBar = self.canvas.create_rectangle(x, y, x + self.player.stamina, y - 16, fill='green', outline='')
        return staminaBar

    def updateStaminaBar(self):
        x = 150
        y = 120
        self.canvas.coords(self.playerStaminaBar, x, y, x + self.player.stamina, y - 16)

    def createItemSlot(self, x, y):
        slotWidth = 60
        slotHeight = 80
        slot = self.canvas.create_rectangle(x, y, x + slotWidth, y + slotHeight, fill='yellow')
        return slot
    
    def createEstusFlaskCounter(self, x, y):
        slotWidth = 60
        slotHeight = 80

        centerX = x + slotWidth / 2
        centerY = y + slotHeight / 2
        counter = self.canvas.create_text(centerX, centerY, text = self.estusFlask.quantity)
        return counter

    def updateEstusFlaskCounter(self, event):
        self.canvas.itemconfig(self.estusFlaskCounter, text = self.estusFlask.quantity)
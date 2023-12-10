from constants import HEIGHT

class GameUI:
    def __init__(self, canvas, player, boss, rune_background, rune_frame, chosen_rune):
        self.canvas = canvas
        self.player = player
        self.boss = boss
        
        self.playerRune = self.createRune(rune_background, rune_frame, chosen_rune)
        self.playerHealthBar = self.createHealthBar()
        self.playerManaBar = self.createManaBar()
        self.playerStaminaBar = self.createStaminaBar()

        self.estusFlaskSlot = self.createItemSlot(50, HEIGHT-180)
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
        healthBar = self.canvas.create_rectangle(x + 25, y, x + self.player.healthPoints/1.2, y - 16, fill='red', outline='')
        healthBar = self.canvas.create_rectangle(x + 25, y, x + self.player.healthPoints/1.2, y - 4, fill='#f08e0c', outline='')
        return healthBar
    
    def createManaBar(self):
        x = 150
        y = 90
        manaBar = self.canvas.create_rectangle(x + 25, y, x + self.player.mana/1.2, y - 16, fill='blue', outline='')
        manaBar = self.canvas.create_rectangle(x + 25, y, x + self.player.mana/1.2, y - 4, fill='#f08e0c', outline='')
        return manaBar
    
    def createStaminaBar(self):
        x = 150
        y = 120
        staminaBar = self.canvas.create_rectangle(x + 25, y, x + self.player.stamina/1.2, y - 16, fill='green', outline='')
        staminaBar = self.canvas.create_rectangle(x + 25, y, x + self.player.stamina/1.2, y - 4, fill='#f08e0c', outline='')
        return staminaBar

    def createItemSlot(self, x, y):
        slotWidth = 60
        slotHeight = 80
        rune = self.canvas.create_rectangle(x, y, x + slotWidth, y + slotHeight, fill='black')
        return rune
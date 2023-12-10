from constants import HEIGHT

class GameUI:
    def __init__(self, canvas, player, boss, rune_background, rune_frame):
        self.canvas = canvas
        self.player = player
        self.boss = boss
        
        self.playerRune = self.createRune(rune_background, rune_frame)
        self.playerHealthBar = self.createBar(100, 30, player.healthPoints, 'red')
        self.playerManaBar = self.createBar(100, 50, player.mana, 'blue')
        self.playerStaminaBar = self.createBar(100, 70, player.stamina, 'green')

        self.estusFlaskSlot = self.createItemSlot(50, HEIGHT-180)
        self.weaponSlot = self.createItemSlot(120, HEIGHT-220)
        self.emptySlot1 = self.createItemSlot(120, HEIGHT-130)
        self.emptySlot2 = self.createItemSlot(190, HEIGHT-180)

        self.bossHealthBar = self.createBar(400, HEIGHT-100, boss.healthPoints, 'red')

    def createRune(self, rune_background, rune_frame):
        x = 20
        y = 20
        # Create an image item using a path
        rune = self.canvas.create_image(x, y, anchor="nw", image=rune_background, tags="rune")
        rune = self.canvas.create_image(x, y, anchor="nw", image=rune_frame, tags="rune")
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
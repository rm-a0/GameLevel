from constants import HEIGHT

class Player:
    def __init__(self, canvas, name, healthPoints, mana, stamina):
        self.canvas = canvas
        self.name = name
        self.maxHealthPoints = healthPoints
        self.healthPoints = healthPoints
        self.maxMana = mana
        self.mana = mana
        self.maxStamina = stamina
        self.stamina = stamina
        self.speed = 10
        #jump() releated atribbutes
        self.jumpHeight = 150
        #coordinates and dimensions of a player object
        self.x = 200
        self.y = HEIGHT - 250
        self.height = 100
        self.width = 60
        #creating hitbox for a character
        self.hitbox = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline='green')

    def refillStamina(self):
        if self.stamina < self.maxStamina:
            self.stamina += 10
        self.canvas.after(500, self.refillStamina)

    def moveLeft(self, event):
        self.x -= self.speed
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)
        self.canvas.after(10, self.moveLeft)

    def moveRight(self, event):
        self.x += self.speed
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)
        self.canvas.after(10, self.moveRight)

    def jump(self, event):
        if self.stamina > 200:
            self.y -= self.jumpHeight
            self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)
            self.stamina -= 200
            self.canvas.after(10, self.jump)

    
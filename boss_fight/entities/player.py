from constants import HEIGHT

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
        
    def moveLeft(self, event):
        self.x -= self.speed
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)

    def moveRight(self, event):
        self.x += self.speed
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)

    def jump(self, event):
        self.y -= self.speed
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)
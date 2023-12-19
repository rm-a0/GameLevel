import time

from constants import HEIGHT, GRAVITY

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
        self.speed = 500

        self.jumpStrength = 500
        self.jumpHeight = 200 + 150

        self.velocityX = 0
        self.velocityY = 0
        self.isJumping = False
        #selg.gravity = idk

        #coordinates and dimensions of a player object
        self.x = 200
        self.y = HEIGHT - 250
        self.height = 100
        self.width = 60
        #creating hitbox for a character
        self.hitbox = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline='green')

    def refillStamina(self):
        if self.stamina < self.maxStamina:
            self.stamina += 1

    def updatePosition(self, dt):
        self.x += self.velocityX * dt
        self.y += self.velocityY * dt
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)

    def moveLeft(self, event):
        self.velocityX = -self.speed

    def stopMoveLeft(self, event):
        self.velocityX = 0

    def moveRight(self, event):
        self.velocityX = self.speed

    def stopMoveRight(self, event):
        self.velocityX = 0

    def jump(self, event):
        if self.isJumping == False and self.stamina > 200:
            self.stamina -= 200
            self.velocityY = -self.jumpStrength
            self.isJumping = True

    def applyGravity(self, dt):
        if self.isJumping:
            self.velocityY += GRAVITY * dt

            if self.y == HEIGHT- 250:
                self.isJumping = False
                self.velocityY = 0
  
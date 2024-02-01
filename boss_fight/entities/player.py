RIGHT = 0
LEFT = 1

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

        self.equippedWeapon = None
        self.attackHitbox = None
        self.bossInstance = None

        self.rollSpeed = self.speed*1.5
        self.jumpStrength = 500
        self.jumpHeight = 200 + 150

        self.velocityX = 0
        self.velocityY = 0

        self.isJumping = False
        self.isFacing = RIGHT
        self.isRolling = False #used for checking hitbox status

        #coordinates and dimensions of a player object
        self.x = 200
        self.y = HEIGHT - 250
        self.height = 100
        self.width = 60
        #creating hitbox for a character
        self.hitbox = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline='green')

    def createBossInstance(self, bossInstance):
        self.bossInstance = bossInstance

    def equipWeapon(self, weapon):
        self.equippedWeapon = weapon

    def refillStamina(self):
        if self.stamina < self.maxStamina:
            self.stamina += 1

    def updatePosition(self, dt):
        self.x += self.velocityX * dt
        self.y += self.velocityY * dt
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)

    def moveLeft(self, event):
        self.velocityX = -self.speed
        self.isFacing = LEFT

    def stopMoveLeft(self, event):
        self.velocityX = 0

    def moveRight(self, event):
        self.velocityX = self.speed
        self.isFacing = RIGHT

    def stopMoveRight(self, event):
        self.velocityX = 0

    def jump(self, event):
        if self.isJumping == False and self.stamina > 200 and self.isRolling == False:
            self.stamina -= 200
            self.velocityY = -self.jumpStrength
            self.isJumping = True

    def applyGravity(self, dt):
        if self.isJumping:
            self.velocityY += GRAVITY * dt

            if self.y == HEIGHT- 250:
                self.isJumping = False
                self.velocityY = 0
    
    def roll(self, event):
        if self.isRolling == False and self.stamina > 200 and self.isJumping == False:
            self.stamina -= 200
            self.isRolling = True
            self.executeRoll()
            self.canvas.after(500, self.endRoll)

    def executeRoll(self):
        if self.isFacing == RIGHT:
            self.velocityX = self.rollSpeed
        if self.isFacing ==  LEFT:
            self.velocityX = -self.rollSpeed

    def endRoll(self):
        self.isRolling = False
        self.velocityX = 0

    def attack(self, boss, event):
        if self.isRolling == False and self.stamina > 200:
            self.stamina -= 200
            self.executeAttack(boss)

    def executeAttack(self, boss):
        if self.isFacing == RIGHT:
            self.attackHitbox = self.equippedWeapon.createHibox(self.canvas, self.x + self.width, self.y + self.height/2, self.equippedWeapon.length, self.equippedWeapon.width, self.isFacing)
        if self.isFacing == LEFT:
            self.attackHitbox = self.equippedWeapon.createHibox(self.canvas, self.x, self.y + self.height/2, self.equippedWeapon.length, self.equippedWeapon.width, self.isFacing)
        if self.checkCollision(boss) == True:
            self.bossInstance.healthPoints -= self.equippedWeapon.damage
            print(f"boss hp: {self.bossInstance.healthPoints}")
        self.canvas.delete(self.attackHitbox)
        self.attackHitbox = None


    def checkCollision(self, boss):
        weaponCoords = self.canvas.coords(self.attackHitbox)
        bossCoords = self.canvas.coords(boss.hitbox)
        
        return weaponCoords[0] < bossCoords[2] and weaponCoords[2] > bossCoords[0] and weaponCoords[3] > bossCoords[1] and weaponCoords[1] < bossCoords[3]
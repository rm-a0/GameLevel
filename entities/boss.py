from constants import HEIGHT, WIDTH

class Boss:
    def __init__(self, canvas, name, healthPoints):
        self.canvas = canvas
        self.name = name
        self.healthPoints = healthPoints

        self.playerInstance = None
        #starting coordinates and dimensions of a boss object
        self.x = WIDTH - 200
        self.y = HEIGHT - 250
        self.height = 100
        self.width = 60
        #creating hitbox for a boss
        self.hitbox = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline='red')

    def createPlayerInstance(self, playerInstance):
        self.playerInstance = playerInstance

    def updatePosition(self, dt):
        self.x -= 0 * dt
        self.canvas.coords(self.hitbox, self.x, self.y, self.x + self.width, self.y + self.height)
    
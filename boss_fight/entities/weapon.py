RIGHT = 0
LEFT = 1

class Weapon:
    def __init__(self, canvas, name, damage,  weight, length, width):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.length = length
        self.width = width

    def createHibox(self, canvas, x, y, radius, width, facing):
        if facing == RIGHT:
            return canvas.create_rectangle(x, y, x + radius, y + width, outline="yellow")
        if facing == LEFT:
            return canvas.create_rectangle(x, y, x - radius, y + width, outline="yellow")
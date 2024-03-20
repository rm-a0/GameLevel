from constants import LEFT, RIGHT

class Weapon:
    def __init__(self, canvas, name, damage,  weight, length, width, spell):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.length = length
        self.width = width
        self.spell = spell

    def createWeaponHibox(self, canvas, x, y, weapon, facing):
        if facing == RIGHT:
            return canvas.create_rectangle(x, y, x + weapon.length, y + weapon.width, outline="yellow")
        if facing == LEFT:
            return canvas.create_rectangle(x, y, x - weapon.length, y + weapon.width, outline="yellow")
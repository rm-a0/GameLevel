from constants import LEFT, RIGHT

class Spell:
    def __init__(self, canvas, name, effect, magnitude, manaCost, castDuration, height, width):
        self.name = name
        self.effect = effect
        self.magnitude = magnitude
        self.manaCost = manaCost
        self.castDuratio = castDuration
        self.height = height
        self.width = width


    def createSpellHitbox(self, canvas, x, y, spell, facing):
        if facing == RIGHT:
            return canvas.create_rectangle(x, y, x + spell.width, y + spell.height, outline="yellow")
        if facing == LEFT:
            return canvas.create_rectangle(x, y, x - spell.width, y + spell.height, outline="yellow")
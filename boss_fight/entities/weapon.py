class Weapon:
    def __init__(self, canvas, name, damage,  weight, reach):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.reach = reach

    def createHibox(self, canvas, x, y, radius, extent):
        return canvas.create_arc(x-radius, y-radius, x+radius, y+radius, start = 90, extent = extent, outline="yellow")
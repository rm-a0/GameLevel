class EstustFlask:
    def __init__(self, quantity, healing):
        self.quantity = quantity
        self.healing = healing

    def heal(self, player, event):
        if self.quantity < 0 and player.isJumping == False and player.isRolling == False:
            if player.healthPoints <= player.maxHealthPoints - self.healing:
                player.healthPoints += self.healing
            else: 
                player.healthPoints += (player.healthPoints + self.healing) - player.maxHealthPoints
            self.quantity -= 1
        
        #delete later
        print(f"flask amount: {self.quantity}")
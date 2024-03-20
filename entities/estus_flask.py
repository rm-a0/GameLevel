class EstusFlask:
    def __init__(self, quantity, healing):
        self.quantity = quantity
        self.healing = healing

    def heal(self, player, event):
        if self.quantity > 0 and player.isRolling == False and player.isJumping == False and player.isPerformingAction == False:
            player.healthPoints += self.healing
            if player.healthPoints > player.maxHealthPoints:
                player.healthPoints = player.maxHealthPoints
        self.quantity -= 1
        
        #delete later
        print(f"flask amount: {self.quantity}")
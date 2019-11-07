import random

class coin():
    side = random.choice(['heads', 'tails'])

    def __init__(self, side):
        self.side = side
    
    def toss(self):
        return random.choice(['heads', 'tails'])

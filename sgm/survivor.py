class Survivor:
    def __init__(self, health, hunger):
        self.health = health
        self.hunger = hunger
    
    def next_day(self):
        self.hunger -= 10
        if self.hunger < 30:
            self.health -= 10
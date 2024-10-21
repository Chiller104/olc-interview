import random

class GamePlayer:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def roll_dice(self):
        roll = random.randint(1, 6)
        print(f"{self.name} hodil {roll}")
        return roll

    def move(self, steps, board):
        new_position = self.position + steps
        if new_position > 100:
            print(f"{self.name} stojíš, prekročil si 100 !")
        else:
            self.position = board.check_position(new_position)
        print(f"{self.name} je na pozícií {self.position}")
from Board import Board

class Game:
    def __init__(self, players):
        self.players = players
        self.board = Board()

    def play_turn(self, player):
        total_roll = 0
        while True:
            roll = player.roll_dice()
            total_roll += roll
            if roll != 6:
                break
        player.move(total_roll, self.board)

    def play(self):
        while True:
            for player in self.players:
                self.play_turn(player)
                if player.position == 100:
                    print(f"{player.name} je víťaz!")
                    return
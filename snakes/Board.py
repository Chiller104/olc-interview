class Board:
    def __init__(self):
        self.ladders = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            78: 83,
            87: 94
}

        self.snakes = {
            16: 6,
            46: 25,
            49: 11,
            62: 19,
            64: 60,
            74: 53,
            89: 68,
            92: 88,
            95: 75,
            99: 80
}
        
    def check_position(self, position):
        if position in self.ladders:
            print(f"Rebrík! lezieš z pozície {position} na pozíciu {self.ladders[position]}")
            return self.ladders[position]
        elif position in self.snakes:
            print(f"Had! padáš z pozície {position} na pozíciu {self.snakes[position]}")
            return self.snakes[position]
        return position

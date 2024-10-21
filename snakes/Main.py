from Game import Game
from GamePlayer import GamePlayer
import time


def generate_player_name(i):
    name = "hráč-"
    while i >= 26:
        name += chr(65 + (i // 26) - 1)
        i = i % 26
    name += chr(65 + i)
    return name

def main():

    players = []    

    while True:
        try:
            num_players = int(input("Zadajte počet hráčov (max 702): "))
            if 1 <= num_players <= 702:
                break
            else:
                print("Prosím, zadajte počet hráčov v rozsahu 1 až 702.")
        except ValueError:
            print("Neplatný vstup. Prosím, zadajte celé kladné číslo.")

    for i in range(num_players):
        name = generate_player_name(i)
        players.append(GamePlayer(name))

    start_time = time.time()

    game = Game
    (players)
    game.play()

    end_time = time.time()
    
    duration = end_time - start_time
    print(f"\nHra trvala {duration:.2f} sekúnd.\n")

if __name__ == "__main__":
    main()


#!usr/bin/env python3
from models import Game, Player, Dealer

game = Game()

def main():
    game.num_of_players()
    game.start_game()

if __name__ == '__main__':
    main()

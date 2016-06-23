#!usr/bin/env python3
from models import Game, Player, Dealer

game = Game()

def main():
    game.prepare_game()
    game.play_game()

if __name__ == '__main__':
    main()

#!usr/bin/env python3
from models import Game, Player, Dealer

game = Game()
player = Player()
game.add_player(player)

def main():
    game.start_game()

if __name__ == '__main__':
    main()

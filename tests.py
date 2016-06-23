from models import Game, Player, Dealer, Deck
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print('Setting up tests')
        self.game = Game()
        self.game.players.append(Player())

    def tearDown(self):
        print('Tearing down tests')
    
    def test_deal_one_card_to_dealer_two_to_player(self):
        self.game.deck.draw_card(self.game.dealer)
        for player in self.game.players:
            self.game.deck.draw_card(player)
            self.game.deck.draw_card(player)
        self.assertTrue(len(self.game.dealer.hand_stack) == 1)
        self.assertTrue(len(self.game.players[0].hand_stack) == 2)

    def test_busted_hand_value_with_nonaces(self):
        player = self.game.players[0]
        player.add_card_to_hand("8 of Diamonds", 8)
        player.add_card_to_hand("Ten of Diamonds", 10)
        player.add_card_to_hand("7 of Hearts", 7)
        self.assertTrue(player.hand_value == 25, "8 + 10 + 7 should equal 25 but instead got {}".format(player.hand_value))

    def test_nonbusted_hand_value_with_one_ace(self):
        player = self.game.players[0]
        player.add_card_to_hand("Ace of Hearts", 11)
        player.add_card_to_hand("Five of Diamonds", 5)
        self.assertTrue(player.hand_value == 16, "Ace + 5 should equal 16 but instead got {}".format(player.hand_value))

    def test_nonbusted_hand_value_with_ace_nonace_nonace(self):
        player = self.game.players[0]
        player.add_card_to_hand("Ace of Hearts", 11)
        player.add_card_to_hand("Five of Diamonds", 5)
        player.add_card_to_hand("Ten of Diamonds", 10)
        self.assertTrue(player.hand_value == 16, "Ace + 5 + 10 should equal 16 but instead got {}".format(player.hand_value))

    def test_nonbusted_hand_value_with_nonace_nonace_ace(self):
        player = self.game.players[0]
        player.add_card_to_hand("Five of Diamonds", 5)
        player.add_card_to_hand("Ten of Diamonds", 10)
        player.add_card_to_hand("Ace of Hearts", 11)
        self.assertTrue(player.hand_value == 16, "5 + 10 + Ace should equal 16 but instead got {}".format(player.hand_value))

    def test_nonbusted_hand_value_with_ace_nonace_ace(self):
        player = self.game.players[0]
        player.add_card_to_hand("Ace of Diamonds", 11)
        player.add_card_to_hand("2 of Diamonds", 2)
        player.add_card_to_hand("Ace of Hearts", 11)
        self.assertTrue(player.hand_value == 14, "Ace + 2 + Ace should equal 14 but instead got {}".format(player.hand_value))

if __name__ == '__main__':
    unittest.main()

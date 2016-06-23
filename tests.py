from models import Game, Player, Dealer, Deck
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print('Setting up tests')
        self.game = Game()
        self.game.players.append(Player())
        self.player = self.game.players[0]
        self.dealer = self.game.dealer
        self.deck = self.game.deck

    def tearDown(self):
        print('Tearing down tests')
        del self.game

class PrepareGameTest(Test):

    def test_game_initialization(self):
        pass 
    
class CardDealingTest(Test):

    def test_deal_one_card_to_dealer_two_to_player(self):
        self.deck.draw_card(self.dealer)
        self.deck.draw_card(self.player)
        self.deck.draw_card(self.player)
        self.assertTrue(len(self.dealer.hand_stack) == 1)
        self.assertTrue(len(self.player.hand_stack) == 2)

    def test_busted_hand_value_with_nonaces(self):
        self.player.add_card_to_hand("8 of Diamonds", 8)
        self.player.add_card_to_hand("Ten of Diamonds", 10)
        self.player.add_card_to_hand("7 of Hearts", 7)
        self.assertTrue(self.player.hand_value == 25, 
            "8 + 10 + 7 should equal 25 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_one_ace(self):
        self.player.add_card_to_hand("Ace of Hearts", 11)
        self.player.add_card_to_hand("Five of Diamonds", 5)
        self.assertTrue(self.player.hand_value == 16, 
            "Ace + 5 should equal 16 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_ace_nonace_nonace(self):
        self.player.add_card_to_hand("Ace of Hearts", 11)
        self.player.add_card_to_hand("Five of Diamonds", 5)
        self.player.add_card_to_hand("Ten of Diamonds", 10)
        self.assertTrue(self.player.hand_value == 16, 
            "Ace + 5 + 10 should equal 16 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_nonace_nonace_ace(self):
        self.player.add_card_to_hand("Five of Diamonds", 5)
        self.player.add_card_to_hand("Ten of Diamonds", 10)
        self.player.add_card_to_hand("Ace of Hearts", 11)
        self.assertTrue(self.player.hand_value == 16, 
            "5 + 10 + Ace should equal 16 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_ace_nonace_ace(self):
        self.player.add_card_to_hand("Ace of Diamonds", 11)
        self.player.add_card_to_hand("2 of Diamonds", 2)
        self.player.add_card_to_hand("Ace of Hearts", 11)
        self.assertTrue(self.player.hand_value == 14, 
            "Ace + 2 + Ace should equal 14 but instead got {}".format(self.player.hand_value))

class ResetGameTest(Test):
    
    def test_reset_game_deck_and_player_stats(self):
        self.player.reset_stats()
        self.assertTrue(self.player.hand_value == 0)
        self.assertTrue(self.player.hand_stack == {})
        self.assertTrue(self.player.still_playing == True)
        self.assertTrue(self.player.busted == False)

    def test_resetted_stats_after_restart_game(self):
        card1, value1 = self.deck.deck.popitem()
        self.player.hand_stack[card1] = value1
        self.player.reset_stats()
        card2, value2 = self.deck.deck.popitem()
        self.player.hand_stack[card2] = value2
        self.assertTrue(card2 != card1)
        self.assertTrue(value2 != value1)


if __name__ == '__main__':
    unittest.main()

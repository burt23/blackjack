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

    def test_of_bust(self):
        card1 = ("8 of Diamonds", 8)
        card2 = ("10 of Diamonds", 10)
        card3 = ("10 of Hearts", 10)
        self.player.add_card_to_hand(*card1)
        self.player.add_card_to_hand(*card2)
        self.player.add_card_to_hand(*card3)
        self.assertTrue(self.player.check_for_bust())

    def test_busted_hand_value_with_nonaces(self):
        card1 = ("8 of Diamonds", 8)
        card2 = ("10 of Diamonds", 10)
        card3 = ("7 of Hearts", 7)
        self.player.add_card_to_hand(*card1)
        self.player.add_card_to_hand(*card2)
        self.player.add_card_to_hand(*card3)
        self.assertTrue(self.player.hand_value == 25, 
            "8 + 10 + 7 should equal 25 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_one_ace(self):
        card1 = ("Ace of Hearts", 11)
        card2 = ("Five of Diamonds", 5)
        self.player.add_card_to_hand(*card1)
        self.player.add_card_to_hand(*card2)
        self.assertTrue(self.player.hand_value == 16, 
            "Ace + 5 should equal 16 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_ace_nonace_nonace(self):
        card1 = ("Ace of Hearts", 11)
        card2 = ("Five of Diamonds", 5)
        card3 = ("Ten of Diamonds", 10)
        self.player.add_card_to_hand(*card1)
        self.player.add_card_to_hand(*card2)
        self.player.add_card_to_hand(*card3)
        self.assertTrue(self.player.hand_value == 16, 
            "Ace + 5 + 10 should equal 16 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_nonace_nonace_ace(self):
        card2 = ("Five of Diamonds", 5)
        card3 = ("Ten of Diamonds", 10)
        card1 = ("Ace of Hearts", 11)
        self.player.add_card_to_hand(*card1)
        self.player.add_card_to_hand(*card2)
        self.player.add_card_to_hand(*card3)
        self.assertTrue(self.player.hand_value == 16, 
            "5 + 10 + Ace should equal 16 but instead got {}".format(self.player.hand_value))

    def test_nonbusted_hand_value_with_ace_nonace_ace(self):
        card1 = ("Ace of Diamonds", 11)
        card2 = ("Two of Diamonds", 2)
        card3 = ("Ace of Hearts", 11)
        self.player.add_card_to_hand(*card1)
        self.player.add_card_to_hand(*card2)
        self.player.add_card_to_hand(*card3)
        self.assertTrue(self.player.hand_value == 14, 
            "Ace + 2 + Ace should equal 14 but instead got {}".format(self.player.hand_value))


class Soft17Test(Test):
    
    def test_soft_17(self):
        card1 = ("Ace of Diamonds", 11)
        card2 = ("Six of Diamonds", 6)
        self.player.add_card_to_hand(*card1)
        self.player.add_card_to_hand(*card2)
        self.assertTrue(self.dealer.soft_17())


class ResetGameTest(Test):
    
    def test_reset_game_deck_and_player_stats(self):
        self.player.reset_stats()
        self.assertTrue(self.player.hand_value == 0)
        self.assertTrue(self.player.hand_stack == [])
        self.assertTrue(self.player.still_playing == True)
        self.assertTrue(self.player.busted == False)

if __name__ == '__main__':
    unittest.main()
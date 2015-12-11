from player import Player, User, Dealer
import game

class Deck():
    def __init__(self):
        self.deck = {
                'Ace of Spades':1,
                '2 of Spades': 2,
                '3 of Spades': 3,
                '4 of Spades': 4,
                '5 of Spades': 5,
                '6 of Spades': 6,
                '7 of Spades': 7,
                '8 of Spades': 8,
                '9 of Spades': 9,
                '10 of Spades': 10,
                'Jack of Spades': 10,
                'Queen of Spades': 10,
                'King of Spades': 10,

                'Ace of Hearts':1,
                '2 of Hearts': 2,
                '3 of Hearts': 3,
                '4 of Hearts': 4,
                '5 of Hearts': 5,
                '6 of Hearts': 6,
                '7 of Hearts': 7,
                '8 of Hearts': 8,
                '9 of Hearts': 9,
                '10 of Hearts': 10,
                'Jack of Hearts': 10,
                'Queen of Hearts': 10,
                'King of Hearts': 10,

                'Ace of Clubs':1,
                '2 of Clubs': 2,
                '3 of Clubs': 3,
                '4 of Clubs': 4,
                '5 of Clubs': 5,
                '6 of Clubs': 6,
                '7 of Clubs': 7,
                '8 of Clubs': 8,
                '9 of Clubs': 9,
                '10 of Clubs': 10,
                'Jack of Clubs': 10,
                'Queen of Clubs': 10,
                'King of Clubs': 10,

                'Ace of Diamonds':1,
                '2 of Diamonds': 2,
                '3 of Diamonds': 3,
                '4 of Diamonds': 4,
                '5 of Diamonds': 5,
                '6 of Diamonds': 6,
                '7 of Diamonds': 7,
                '8 of Diamonds': 8,
                '9 of Diamonds': 9,
                '10 of Diamonds': 10,
                'Jack of Diamonds': 10,
                'Queen of Diamonds': 10,
                'King of Diamonds': 10,
                }

    def draw_card(self, player):
        # draw card from deck and add to user's hand stack
        card, value = self.deck.popitem()
        player.hand_stack[card] = value


class Game():
    def __init__(self):
        self.dealer = Dealer()
        self.players = []
        self.deck = Deck()

    def hit_or_stand(self):
        # ask user to hit or stand and performs functions based on
        # the input
        # user = user instance, deck = card instance (cards?)
        for player in self.players:
            choice = str(input("Do you want to hit or stand? [H/S] ")).upper()
            if choice == "H":
                # draw one card, show hand, then evaluate score for bust
                self.deck.draw_card(player)
                player.get_hand_stack() # displays hand
                # evaluate players hand by looking at Busted variable
                if player.check_for_bust():
                    self.dealer.force_hit_until_18(self.deck) # hit until over 17 but under 21.
                    self.compare_hands(player)
                else:
                    self.hit_or_stand() # ask to hit/stand again
            elif choice == "S":
                # set user not_standing to False, then evaluate score for bust
                player.stand()
                player.get_hand_stack()
                self.dealer.force_hit_until_18(self.deck)
                self.compare_hands(player)
            else:
                print("Error: Choose 'H' or 'S'.")
                self.hit_or_stand()

    def compare_hands(self, player):
        # user and dealer's scores are compared and
        # winner is printed. Game ends afterwards
        if player.busted:
            print("You lose")
        else: # user has not busted
            if not self.dealer.busted:
                if player.hand_value > self.dealer.hand_value or self.dealer.busted:
                    print("You win!")
                elif player.hand_value == self.dealer.hand_value:
                    print("Draw! You and the dealer have the same hand.")
                else: 
                    print("You lose")
            else:
                print("You win")
        self.play_again()

    def play_again(self):
        # asks user for input to play again, if yes, user/dealer
        # stats are reseted. Otherwise, the program ends.
        choice = str(input("Do you want to play again? [Y/N]")).upper()
        if choice == "Y":
            self.reset_game()
            self.start_game()
        elif choice == "N":
            print("Ok. See you next time")
        else:
            print("Error: Choose 'Y' or 'N'. ")
            self.play_again()

    def start_game(self):
        # add players to the game then
        # draw one card to dealer, two cards are drawn
        # to the user, both user/dealer hands are shown
        # game starts by asking user to hit/stand
        user = User()
        self.add_players(user)
        self.deal_card_to_dealer()
        self.deal_card(2)
        self.hit_or_stand()
        
    def deal_card(self, amount=1):
        # draw two cards to user
        for number in range(amount):
            for players in self.players:
                self.deck.draw_card(players)
        for players in self.players:
            players.get_hand_stack()
    
    def deal_card_to_dealer(self):
        self.deck.draw_card(self.dealer)
        self.dealer.get_hand_stack()

    def add_players(self, player):
        self.players.append(player)

    def reset_game(self):
        # both user/dealer stats are reseted
        self.players = []
        self.dealer.reset_stats()

    def get_data(self, player):
        # search within file, read & return
        # player stats.
        try:
            with open('data.py', 'r') as f:
                pass
        except Exception as err:
            print("Error: {}".format(err))

    def write_data(self, player, money=None, wins=None, losses=None):
        # search within file, read and write
        # player stats
        try:
            with open('data.py', 'w') as f:
                pass
        except Exception as err:
            print("Error: {}".format(err))

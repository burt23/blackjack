import time, sys

class Deck():
    def __init__(self):
        self.deck = {
                'Ace of Spades': 1,
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

                'Ace of Hearts': 1,
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

                'Ace of Clubs': 1,
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

                'Ace of Diamonds': 1,
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
        player.add_card_to_hand(*self.deck.popitem())


class Player():
    def __init__(self, name='Player'):
        self.name = name
        self.hand_value = 0
        self.hand_stack = {}
        self.still_playing = True
        self.busted = False

    def add_card_to_hand(self, card, value):
        self.hand_stack[card] = value
        if value != 1:
            self.hand_value += value
        else:
            if self.hand_value + 11 < 21:
                self.hand_value += 11
            else:
                self.hand_value += 1

    def show_cards_in_hand(self):
        print("-"*20)
        print("{}'s hand".format(self.name))
        print("-"*20)
        for card in self.hand_stack.keys():
            print(card)
        self.show_hand_value()
    
    def show_hand_value(self):
        print("{}'s card value is {}".format(
            self.name,
            self.hand_value))
    
    def num_of_aces_in_hand(self):
        return sum(card for card in self.hand_stack.values() if card == 1)

    def stand(self):
        self.still_playing = False

    def check_for_bust(self):
        if self.hand_value <= 21:
            return False
        else:
            self.busted = True
            print("{} bust!".format(self.name))
            time.sleep(2)
            return True

    def reset_stats(self):
        self.hand_value = 0
        self.hand_stack = {}
        self.still_playing = True
        self.busted = False


class Dealer(Player):
    def __init__(self):
        Player.__init__(self, "Dealer")        


class Game():
    def __init__(self):
        self.dealer = Dealer()
        self.players = []
        self.deck = Deck()

    def show_game_options(self):
        for player in self.players:
            print("-"*20)
            print("It's {}'s turn".format(player.name.upper()))
            print("-"*20)
            choice = str(input("Select an option:\n\
- View my hand [V]\n\
- View dealer's hand [D]\n\
- Hit [H]\n\
- Stand [S]\n\
- Restart game [R]\n\
- Quit [Q]\n\
------------------------\n\
")).strip().upper()
            if choice == 'H':
                self.deck.draw_card(player)
                player.show_cards_in_hand()
                if not player.check_for_bust():
                    self.show_game_options() 
            elif choice == 'S':
                player.stand()
                if len(self.players) == 1:
                    print("{} stood. Let's see the dealer's hand".format(player.name))
                else:
                    print("{} stood. Let's see the next player play.".format(player.name))
                time.sleep(2)
            elif choice == 'V':
                player.show_cards_in_hand()
                self.show_game_options()
            elif choice == 'D':
                self.dealer.show_cards_in_hand()
                self.show_game_options()
            elif choice == 'R':
                self.reset_game()
                self.start_game()
            elif choice == 'Q':
                sys.exit("Goodbye")
            else:
                print("Error: Choose a valid menu option.")
                self.show_game_options()
        self.force_hit_until_18() 
        self.compare_hands()

    def compare_hands(self):
        """All player's and dealer's scores are compared and
        winners are printed. Game ends afterwards """
        for player in self.players:
            if player.busted:
                print("{} busted".format(player.name))
            else: 
                if not self.dealer.busted:
                    if player.hand_value > self.dealer.hand_value:
                        print("{} wins!".format(player.name))
                    elif player.hand_value == self.dealer.hand_value:
                        print("Push! {} and the dealer have the same hand.".format(player.name))
                    else: 
                        print("{} lost".format(player.name))
                else:
                    print("{} wins!".format(player.name))
        self.play_again()

    def force_hit_until_18(self):
        while self.dealer.hand_value <= 17 and not self.dealer.hand_value >= 21:
            print("\nDealer is dealing himself a card. . .\n")
            time.sleep(2)
            self.deck.draw_card(self.dealer)
            self.dealer.show_cards_in_hand()
        if self.dealer.hand_value > 21:
            self.dealer.busted = True
            print("Dealer busts")

    def play_again(self):
        """ asks player for input to play again, if yes, user/dealer
        stats are reseted. Otherwise, the program ends."""
        choice = str(input("Do you want to play again? [Y/N]")).strip().upper()
        if choice == "Y":
            self.reset_game()
            self.start_game()
        elif choice == "N":
            print("Ok. See you next time")
        else:
            print("Error: Choose 'Y' or 'N'. ")
            self.play_again()

    def start_game(self):
        self.deal_card(self.dealer)
        self.dealer.show_cards_in_hand()
        self.deal_card(self.players, 2)
        for player in self.players:
            player.show_cards_in_hand()
        self.show_game_options()
        
    def deal_card(self, to_whom, amount=1):
        for number in range(amount):
            if isinstance(to_whom, Dealer):
                self.deck.draw_card(to_whom)
            else:
                for player in to_whom:
                    self.deck.draw_card(player)

    def num_of_players(self):
        num = int(input("How many players are going to play in this round of Blackjack? "))
        for count in range(num):
            name = str(input(
                "What is player {}'s username? ".format(count+1)).title())
            player = Player(name)
            self.add_player(player)

    def add_player(self, player):
        self.players.append(player)

    def reset_game(self):
        for player in self.players:
            player.reset_stats()
        self.dealer.reset_stats()
        self.deck = Deck()

    def get_data(self, player):
        try:
            with open('data.py', 'r') as f:
                pass
        except Exception as err:
            print("Error: {}".format(err))

    def write_data(self, player, money=None, wins=None, losses=None):
        try:
            with open('data.py', 'w') as f:
                pass
        except Exception as err:
            print("Error: {}".format(err))

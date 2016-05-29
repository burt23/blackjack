import time

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


class Player(object):
    def __init__(self):
        self.hand_value = 0
        self.hand_stack = {}
        self.not_standing = True
        self.number_of_aces = 0
        self.ace_value = 0
        self.busted = False

    def get_hand_stack(self):
        # returns the stack of cards and it's values.
        # also, returns the alternate hand if there are any Aces
        # found in the hand.
        self.set_hand_value()
        self.set_ace_value()
        for cards in self.hand_stack.keys():
            print(cards)
        if self.ace_value > 0 and self.ace_value <= 21:
            print("Your hand is a {}".\
                    format(self.ace_value))
        else:
            print("Your hand is a {}".format(self.hand_value))

    def set_ace_value(self):
        temp_value = self.hand_value
        for numbers in self.hand_stack.values():
            if numbers == 1:
                temp_value += 10
        self.ace_value = temp_value

    def set_hand_value(self):
        # add card to users hand in the form of a list
        total = 0
        for cards in self.hand_stack.values():
            total += cards
        #total = [sum(cards) for cards in self.hand_stack.values()]
        self.hand_value = total

    def show_hand_value(self):
        # displays the hand value in a string
        print("Your hand is a {total}".format(total=self.hand_value))

    def stand(self):
        # sets user to fold/stand, they are no longer playing
        self.not_standing = False

    def check_for_bust(self):
        # checks for bust, if so sets and returns Busted to True
        if self.hand_value > 21 or self.ace_value > 21:
            self.busted = True
            print("You bust!")
            time.sleep(2)
            return True
        else:
            return False

    def reset_stats(self):
        self.hand_value = 0
        self.hand_stack = []
        self.not_standing = True
        self.number_of_aces = 0
        self.ace_value = 0
        self.busted = False


class User(Player):
    def __init__(self):
        Player.__init__(self)


class Dealer(Player):
    def __init__(self):
        Player.__init__(self)        

    def show_hand_value(self):
        print("Dealer's hand is a", self.hand_value)

    def get_hand_stack(self):
        # returns the stack of cards and it's values.
        # also, returns the alternate hand if there are any Aces
        # found in the hand.
        self.set_hand_value()
        self.set_ace_value()
        for cards in self.hand_stack.keys():
            print(cards)
        if self.ace_value > 0 and self.ace_value <= 21:
            print("The dealer's hand is a {}".\
                    format(self.ace_value))
        else:
            print("The dealer's hand is a {}".format(self.hand_value))

    def force_hit_until_18(self, deck):
        # flip unknown card (deal card) before this func is called
        # then display hand stack 
        self.get_hand_stack()

        # If any Aces deal card until ace_value reaches 18 or doesn't bust,
        # then stand if dealer doesn't bust
        
        # Otherwise deal card until hand_value reaches 18. 
        # If hand_value doesn't bust then stand.
        # keep drawing cards until the dealer gets to 17
        # if dealer busts, run busts, then show value 
        if self.ace_value > 0:
            while self.ace_value <= 17 and not self.ace_value >= 21:
                print("\nDealer is dealing himself a card. . .\n")
                time.sleep(2)
                deck.draw_card(self)
                self.get_hand_stack()
        else:
            while self.hand_value < 17 and not self.hand_value >= 21:
                print("\nDealer is dealing himself a card. . .\n")
                time.sleep(2)
                deck.draw_card(self)
                self.get_hand_stack()
        if self.hand_value > 21 or self.ace_value > 21:
            self.busted = True


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
                print("\nYou stood. Let's see what the dealer's hand looks like.\n")
                time.sleep(2)
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
            self.start_new_game()
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

    def start_new_game(self):
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
        for player in self.players:
            player.reset_stats()
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

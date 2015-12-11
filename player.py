import time

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
        for values in self.hand_stack.values():
            if values == 1:
                temp_ace_value = 0
                temp_hand_value = self.hand_value
                while temp_hand_value > 21:
                    temp_ace_value += 10
                    temp_hand_value -= 10
                self.ace_value = temp_ace_value
        for cards in self.hand_stack.keys():
            print(cards)
        if self.ace_value > 0:
            print("Your hand is a {} or {}".\
                    format(self.ace_value, self.hand_value))
        else:
            print("Your hand is a {}".format(self.hand_value))

    def set_hand_value(self):
        # add card to users hand in the form of a list
        total = 0
        for cards in self.hand_stack.values():
            total += cards
        #total = [sum(cards) for cards in self.hand_stack.values()]
        self.hand_value = total

    def set_hand_stack(self, card, value):
        # appends card and its value to hand of cards, which is in the
        # form of a dictionary
        # MAKE SURE THIS IS TESTED AND WORKS ------------------------
        self.hand_stack.update(card, value)

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
        if 1 in self.hand_stack.values():
            temp_value = 0
            if not self.hand_value > 21:
                temp_value += 10
            self.ace_value -= temp_value
        for cards in self.hand_stack.keys():
            print(cards)
        if self.ace_value > 0:
            print("The dealer's hand is a {} or {}".\
                    format(self.ace_value, self.hand_value))
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

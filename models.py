import sys, json, math, random

class Deck():
    """A deck of 52 cards"""
    def __init__(self):
        """Attributes:
            self.deck (list): 52 dictionaries in a list
            self.deck_length (int): The num of items in self.deck
        """
        self.deck = [
            {'Card': 'Ace of Spades', 'Value': 11},
            {'Card': '2 of Spades', 'Value': 2},
            {'Card': '3 of Spades', 'Value': 3},
            {'Card': '4 of Spades', 'Value': 4},
            {'Card': '5 of Spades', 'Value': 5},
            {'Card': '6 of Spades', 'Value': 6},
            {'Card': '7 of Spades', 'Value': 7},
            {'Card': '8 of Spades', 'Value': 8},
            {'Card': '9 of Spades', 'Value': 9},
            {'Card': '10 of Spades', 'Value': 10},
            {'Card': 'Jack of Spades', 'Value': 10},
            {'Card': 'Queen of Spades', 'Value': 10},
            {'Card': 'King of Spades', 'Value': 10},
            {'Card': 'Ace of Hearts', 'Value': 11},
            {'Card': '2 of Hearts', 'Value': 2},
            {'Card': '3 of Hearts', 'Value': 3},
            {'Card': '4 of Hearts', 'Value': 4},
            {'Card': '5 of Hearts', 'Value': 5},
            {'Card': '6 of Hearts', 'Value': 6},
            {'Card': '7 of Hearts', 'Value': 7},
            {'Card': '8 of Hearts', 'Value': 8},
            {'Card': '9 of Hearts', 'Value': 9},
            {'Card': '10 of Hearts', 'Value': 10},
            {'Card': 'Jack of Hearts', 'Value': 10},
            {'Card': 'Queen of Hearts', 'Value': 10},
            {'Card': 'King of Hearts', 'Value': 10},
            {'Card': 'Ace of Clubs', 'Value': 11},
            {'Card': '2 of Clubs', 'Value': 2},
            {'Card': '3 of Clubs', 'Value': 3},
            {'Card': '4 of Clubs', 'Value': 4},
            {'Card': '5 of Clubs', 'Value': 5},
            {'Card': '6 of Clubs', 'Value': 6},
            {'Card': '7 of Clubs', 'Value': 7},
            {'Card': '8 of Clubs', 'Value': 8},
            {'Card': '9 of Clubs', 'Value': 9},
            {'Card': '10 of Clubs', 'Value': 10},
            {'Card': 'Jack of Clubs', 'Value': 10},
            {'Card': 'Queen of Clubs', 'Value': 10},
            {'Card': 'King of Clubs', 'Value': 10},
            {'Card': 'Ace of Diamonds', 'Value': 11},
            {'Card': '2 of Diamonds', 'Value': 2},
            {'Card': '3 of Diamonds', 'Value': 3},
            {'Card': '4 of Diamonds', 'Value': 4},
            {'Card': '5 of Diamonds', 'Value': 5},
            {'Card': '6 of Diamonds', 'Value': 6},
            {'Card': '7 of Diamonds', 'Value': 7},
            {'Card': '8 of Diamonds', 'Value': 8},
            {'Card': '9 of Diamonds', 'Value': 9},
            {'Card': '10 of Diamonds', 'Value': 10},
            {'Card': 'Jack of Diamonds', 'Value': 10},
            {'Card': 'Queen of Diamonds', 'Value': 10},
            {'Card': 'King of Diamonds', 'Value': 10}]
        self.deck_length = 52

    def draw_card(self, player, amount=1):
        """Draw 'x' AMOUNT of cards from self.deck to PLAYER"""
        for number in range(amount):
            self.deck_length -= 1
            player.add_card_to_hand(self.deck.pop(self.random_int()))

    def random_int(self):
        """Return a random list index based on the length of self.deck"""
        return math.floor(random.random()*self.deck_length)


class Player():
    """A single player in the game"""
    def __init__(self, name='Player', money=1000, wins=0, 
            losses=0, save_to_file= False):
        """Attributes:
            self.name (str): The player's username. Default: Player    
            self.hand_value (int): The value of the players hand. Default: 0
            self.hand_stack (list): The card,value tuple of each card in the
            players hand. Default: []
            self.still_playing (bool): Whether or not the player is currently
            playing or has stood. Default: True
            self.busted (bool): Whether or not the player has busted. Default:
            False
            self.money (int): Int of money user has. Default: 1000
            self.losses (int): Int of total losses in game. Default: 0
            self.wins (int): Int of total wins in game. Default: 0
            self.save_to_file (bool): Whether or not the players info will be
            saved to file. Default: False
            self.current_bet (int): Int of current bet in round. Default: 5
        """
        self.name = name
        self.hand_value = 0
        self.hand_stack = []
        self.still_playing = True
        self.busted = False
        self.money = money
        self.losses = losses
        self.wins = wins
        self.save_to_file = save_to_file
        self.current_bet = 5

    def add_card_to_hand(self, card):
        """Add card to players hand and reevaluate value of hand based on the
        number of Ace cards in hand."""
        self.hand_stack.append(card)
        temp_value = self.sum_non_aces()
        ace_count = self.num_aces() 
        if ace_count > 0:
            count = 0
            while count < ace_count:
                if temp_value + 11 <= 21:
                    temp_value += 11
                else:
                    temp_value += 1
                    index = self.hand_stack.index(card)
                    self.hand_stack[index]['Value'] = 1
                count += 1
        self.hand_value = temp_value

    def sum_non_aces(self):
        """Return the sum of all non-ace cards in hand"""
        return sum(v['Value'] for v in self.hand_stack if v['Value'] != 11)

    def num_aces(self):
        """Return the int of ace cards in hand"""
        return len(list(1 for c in self.hand_stack if c['Card'][:3] == 'Ace'))

    def num_of_soft_aces(self):
        """Return the int of all soft ace cards in hand"""
        return len(list(v for v in self.hand_stack if v['Value'] == 11))

    def show_cards_in_hand(self):
        """Print all cards in hand and the value of the player's hand"""
        print("-"*20)
        print("{}'s hand".format(self.name))
        print("-"*20)
        for card in self.hand_stack:
            print(card['Card'])
        print("{}'s card value is {}".format(
            self.name,
            self.hand_value))

    def stand(self):
        """Set self.still_playing to False"""
        self.still_playing = False

    def check_for_bust(self):
        """Set self.busted to True if value of hand is over 21"""
        if self.hand_value > 21:
            self.busted = True
            print("{} busts!".format(self.name))

    def reset_stats(self):
        """Set all object attributes back to their default values"""
        self.hand_value = 0
        self.hand_stack = []
        self.still_playing = True
        self.busted = False
        self.current_bet = 5


class Dealer(Player):
    """The dealer in the blackjack game. Subclass of Player"""
    def __init__(self):
        """Attributes: Inherits all attr from Player class
            self.name (str): The name of the dealer. Default: Dealer
        """
        Player.__init__(self, "Dealer")        

    def soft_17(self):
        '''Return True if the dealers hand value is soft 17. False otherwise'''
        if self.hand_value == 17 and self.num_of_soft_aces() >= 1:
            return True
        else:
            return False


class Game():
    """The gameplay of blackjack"""
    def __init__(self):
        """Attributes:
            self.dealer (:obj): class Dealer
            self.players (list): List of all the players in the game
            self.deck (:obj): class Deck
            self.data (dict): JSON dictionary with a list of player info such as
            username, wins, losses, and money
        """
        self.dealer = Dealer()
        self.players = []
        self.deck = Deck()
        self.data = None

    def show_game_options(self, player):
        """Prints the menu option to the player. Calls do_menu_choice based on
        players selection"""
        print("-"*20)
        print("It's {}'s turn".format(player.name.upper()))
        print("-"*20)
        choice = str(input("Select an option:\n\
- View my hand [V]\n\
- View dealer's hand [D]\n\
- View my money, current bet, wins and losses [M]\n\
- Hit [H]\n\
- Stand [S]\n\
- Restart game [R]\n\
- Quit [Q]\n\
------------------------\n\
")).strip().upper()
        self.do_menu_choice(choice, player)

    def do_menu_choice(self, choice, player):
        """Performs steps based on players choice made in the menu options"""
        if choice == 'H':
            self.deck.draw_card(player)
            player.show_cards_in_hand()
            player.check_for_bust()
            if player.busted == False:
                self.show_game_options(player) 
        elif choice == 'S':
            player.stand()
            if len(self.players) == 1:
                print("{} stood. Let's see the dealer's hand".format(player.name))
            else:
                print("{} stood. Let's see the next player play.".format(player.name))
        elif choice == 'M':
            print("Money: {} dollars\nCurrent bet: {} dollars\nWins: {}\nLosses: {}".format(
                str(player.money-player.current_bet),
                str(player.current_bet),
                str(player.wins), str(player.losses)))
            self.show_game_options(player)
        elif choice == 'V':
            player.show_cards_in_hand()
            self.show_game_options(player)
        elif choice == 'D':
            self.dealer.show_cards_in_hand()
            self.show_game_options(player)
        elif choice == 'R':
            restart = str(input(
                "You will lose your bet, still want to restart? [Y/N] ")).strip().upper()
            if restart == 'Y':
                player.money -= player.current_bet
                self.reset_game()
                self.get_player_bets()
                self.play_game()
            else:
                self.show_game_options(player)
        elif choice == 'Q':
            self.write_json_data()
            sys.exit("Goodbye")
        else:
            print("Error: Choose a valid menu option.")
            self.show_game_options(player)

    def compare_hands(self):
        """All player's and dealer's scores are compared and
        winners are printed. Game ends afterwards """
        for player in self.players:
            if player.busted:
                player.money -= player.current_bet
                player.losses += 1
                print("{} busted and losses {} dollars".format(
                    player.name, str(player.current_bet)))
            else: 
                if not self.dealer.busted:
                    if player.hand_value > self.dealer.hand_value:
                        player.money += player.current_bet
                        player.wins += 1
                        print("{} wins and gets {} dollars".format(
                            player.name, str(player.current_bet*2)))
                    elif player.hand_value == self.dealer.hand_value:
                        print("Push! {} and the dealer have the same hand.".format(player.name))
                    else: 
                        player.money -= player.current_bet
                        player.losses += 1
                        print("{} lost and losses {} dollars".format(
                            player.name, str(player.current_bet)))
                else:
                    player.money += player.current_bet
                    player.wins += 1
                    print("{} wins and gets {} dollars".format(
                        player.name, str(player.current_bet*2)))

    def force_hit_until_18(self):
        """Dealer forcefully draws cards until his hand is above 17 or he busts."""
        while self.dealer.hand_value <= 17 and not self.dealer.hand_value >= 21:
            self.deck.draw_card(self.dealer)
            self.dealer.show_cards_in_hand()

    def play_again(self):
        """Game asks player for input to play again, if yes, user/dealer
        stats are reseted. Otherwise, the program ends."""
        choice = str(input("Do you want to play another round? [Y/N]")).strip().upper()
        if choice == "Y":
            self.reset_game()
            self.get_player_bets()
            self.play_game()
        elif choice == "N":
            self.write_json_data()
            sys.exit("Ok. See you next time")
        else:
            print("Error: Choose 'Y' or 'N'. ")
            self.play_again()

    def prepare_game(self):
        """Collect number of players and their usernames before starting game"""
        self.get_player_info()
        self.get_player_bets()

    def play_game(self):
        """Game begins by dealing cards to players and dealer. Each player is
        provided with menu options. Game ends after all hands are compared"""
        self.deal_to_players()
        self.deal_to_dealer()
        for player in self.players:
            self.show_game_options(player)
        self.deal_to_dealer()
        if not self.dealer.soft_17():
            self.force_hit_until_18() 
            self.dealer.check_for_bust()
        self.compare_hands()
        self.play_again()

    def deal_to_players(self):
        """Deals two cards to each player"""
        for player in self.players:
            self.deck.draw_card(player, 2)
            player.show_cards_in_hand()

    def deal_to_dealer(self):
        """Deals a single card to the dealer"""
        self.deck.draw_card(self.dealer)
        self.dealer.show_cards_in_hand()

    def get_player_info(self):
        """Game prompts user for players info then adds those
        players to the self.players."""
        num = int(input("How many players are going to play in this round of Blackjack? "))
        for count in range(num):
            name = str(input(
                "What is player {}'s username? ".format(count+1)))
            player = self.get_json_player_info(name)
            if not player:
                self.create_new_player(name)
            else:
                self.json_to_player(player)

    def get_player_bets(self):
        for player in self.players:
            print("You have {} dollars to bet with".format(player.money))
            bet = int(input("{}, What is your minimum bet? ".format(
                player.name)))
            player.current_bet = bet 

    def json_to_player(self, jsonobj):
        player = Player(
            name = jsonobj['username'],
            money = jsonobj['money'],
            wins = jsonobj['wins'],
            losses = jsonobj['losses'],
            save_to_file = True
            )
        self.players.append(player)

    def get_json_player_info(self, name):
        self.data = self.get_json_data(name)
        for player in self.data['players']:
            if player['username'] == name:
                return player

    def create_new_player(self, name):
        choice = str(input("The username {} could not be found. Do you want to create a new user with this username? [Y/N]".format(
            name))).strip().upper()
        if choice == 'Y':
            player = Player(name=name, save_to_file=True)
        else:
            self.players.append(Player(name))

    def reset_game(self):
        """Resets all attributes of all objects in the Game class"""
        for player in self.players:
            player.reset_stats()
        self.dealer.reset_stats()
        self.deck = Deck()

    def get_json_data(self, username):
        try:
            with open('data.json', 'r') as f:
                return json.loads(f.read())
        except Exception as err:
            print("Error: {}".format(err))

    def write_json_data(self):
        for player in self.players:
            if player.save_to_file:
                json_player = {
                    'username' : player.name,
                    'wins' : player.wins,
                    'losses' : player.losses,
                    'money': player.money
                    }
                index = 0
                for i, dic in enumerate(self.data['players']):
                    if dic['username'] == player.name:
                        index = i
                self.data['players'][index] = json_player
        try:
            with open('data.json', 'w') as f:
                json.dump(self.data, f)
        except Exception as err:
            print("Error: {}".format(err))

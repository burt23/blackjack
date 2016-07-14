import json, math, random
from views import *

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
        """Add card and it's value to player's hand based on the
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
                count += 1
        self.hand_value = temp_value

    def sum_non_aces(self):
        """Return the sum of all non-ace cards in hand"""
        return sum(c['Value'] for c in self.hand_stack if c['Card'][:3] != 'Ace')

    def num_aces(self):
        """Return the int of ace cards in hand"""
        return len(list(1 for c in self.hand_stack if c['Card'][:3] == 'Ace'))

    def num_of_soft_aces(self):
        """Return the int of all soft ace cards in hand"""
        return len(list(v for v in self.hand_stack if v['Value'] == 11))

    def stand(self):
        """Set self.still_playing to False"""
        self.still_playing = False
        show_msg_after_stand(self)

    def check_for_bust(self):
        """Set self.busted to True if value of hand is over 21"""
        if self.hand_value > 21:
            self.still_playing = False
            return True

    def handle_bust(self):
        if self.check_for_bust():
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

    def handle_options(self, player, choice):
        """Perform actions based on players choice"""
        if choice in ['M', 'D', 'V']:
            self.handle_info_choice(player, choice)
        else:
            self.handle_game_choice(player, choice)

    def handle_game_choice(self, player, choice):
        """Perform hit, stand, restart or quit options"""
        if choice == 'H':
            self.handle_hit(player)
        elif choice == 'S':
            player.stand()
        elif choice == 'R':
            restart_choice = show_restart_prompt()
            if restart_choice == 'Y':
                player.money -= player.current_bet
                self.restart_game()
        else:
            self.write_json_data()
            show_exit_msg()

    def handle_info_choice(self, player, choice):
        """Shows user info requested from the menu"""
        if choice == 'D':
            show_cards(self.dealer)
        elif choice == 'V':
            show_cards(player)
        else:
            show_player_info(player)
    
    def handle_hit(self, player):
        """Card is drawn to user and the game checks if he/she busts"""
        self.deck.draw_card(player)
        show_cards(player)
        player.handle_bust()

    def show_options(self, player):
        while player.still_playing:
            choice = show_options(player)
            self.handle_options(player, choice)

    def compare_hands(self):
        """All player's and dealer's scores are compared and
        winners are printed. Game ends afterwards """
        for player in self.players:
            if player.busted:
                self.handle_outcome(player, "bust")
            else: 
                if not self.dealer.busted:
                    if player.hand_value == self.dealer.hand_value:
                        show_push_msg(player)
                    elif self.check_for_blackjack(player):
                        self.handle_outcome(player, "blackjack")
                    elif player.hand_value > self.dealer.hand_value:
                        self.handle_outcome(player, "win")
                    else: 
                        self.handle_outcome(player, "loss")
                else:
                    self.handle_outcome(player, "win")

    def check_for_blackjack(self, player):
        """Return true if player has blackjack"""
        return player.hand_value == 21 and \
            len(player.hand_stack) == 2 and \
            (player.hand_stack[0]['Value'] == 11 or \
            player.hand_stack[1]['Value'] == 11)

    def handle_outcome(self, player, outcome):
        """Increment/Decrement win, losses, and money and show win/loss msg"""
        if outcome == "win":
            player.money += player.current_bet
            player.wins += 1
            show_win_msg(player, str(player.current_bet*2))
        elif outcome == "loss" or outcome == "bust":
            player.money -= player.current_bet
            player.losses += 1
            if outcome == "bust":
                show_bust_msg(player)
            else:
                show_loss_msg(player, str(player.current_bet))
        elif outcome == "blackjack":
            player.money += math.floor(player.current_bet+(player.current_bet*1.5))
            player.wins += 1
            show_blackjack_msg(player,
                math.floor(player.current_bet+(player.current_bet*1.5)))

    def force_hit_until_18(self):
        """Dealer forcefully draws cards until his hand is above 17 or he busts."""
        while self.dealer.hand_value <= 17 and not self.dealer.hand_value >= 21:
            self.deck.draw_card(self.dealer)
            show_cards(self.dealer)

    def play_again(self):
        """ Game restarts if user wants to quit, 
        otherwise game is restarted"""
        choice = get_play_again_choice()
        if choice == "Y":
            self.restart_game()
        else:
            self.write_json_data()
            show_exit_msg()

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
            self.show_options(player)
        self.deal_to_dealer()
        if not self.dealer.soft_17():
            self.force_hit_until_18() 
            self.dealer.handle_bust()
        self.compare_hands()
        self.play_again()

    def deal_to_players(self):
        """Deals two cards to each player"""
        for player in self.players:
            self.deck.draw_card(player, 2)
            show_cards(player)

    def deal_to_dealer(self):
        """Deals a single card to the dealer"""
        self.deck.draw_card(self.dealer)
        show_cards(self.dealer)

    def restart_game(self):
        """Resets game stats, gets players bets and starts a new game"""
        self.reset_game()
        self.get_player_bets()
        self.play_game()

    def get_player_info(self):
        """Game prompts user for players info then adds those
        players to the self.players."""
        num = get_num_players()
        for count in range(num):
            name = get_player_name(count)
            player = self.get_json_player_info(name)
            if not player:
                self.create_new_player(name)
            else:
                self.json_to_player(player)

    def get_player_bets(self):
        for player in self.players:
            bet = show_bet_msg(player)
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
        choice = show_create_player_msg(name)
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

import sys


def show_cards(player):
    """Print all cards in hand and the value of the player's hand"""
    print("-"*20)
    print("{}'s hand".format(player.name))
    print("-"*20)
    for card in player.hand_stack:
        print(card['Card'])
    print("{}'s card value is {}".format(
        player.name,
        player.hand_value))

def show_options(player):
        """Prints the menu option to the player"""
        print("-"*20)
        print("It's {}'s turn".format(player.name.upper()))
        print("-"*20)
        while True:
            try:
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
            except ValueError:
                print("Sorry, please choose a valid option. Try again.")
                continue
            if isinstance(choice, int):
                print("Provide a letter not a number.")
                continue
            if choice not in ['V', 'D', 'M', 'H', 'S', 'R', 'Q']:
                print("Provide an appropriate letter- V, D, M, H, S, R, Q")
                continue
            else:
                return choice

def show_msg_after_stand(player):
    """Prints a message to the user after he/she stands"""
    print("{} stood. Let's see the next player's hand".format(player.name))

def show_player_info(player):
    """Prints uers money, current bet, wins, and losses"""
    print("Money: {} dollars\nCurrent bet: {} dollars\nWins: {}\nLosses: {}".format(
        str(player.money-player.current_bet),
        str(player.current_bet),
        str(player.wins), str(player.losses)))

def show_restart_prompt():
    """Returns the user's choice if he/she wants to quit"""
    while True:
        try:
            choice = str(input(
                "You will lose your bet, still want to restart? [Y/N] ")).strip().upper()
        except ValueError:
            print("Sorry, choose a valid option 'Y' or 'N'.")
            continue
        else:
            return choice

def show_exit_msg():
    """Prints exit message before the game ends"""
    sys.exit("Goodbye!")

def show_bust_msg(player):
    """Prints msg to user after he/she busts"""
    print("{} busted and losses {} dollars".format(player.name, str(player.current_bet)))

def show_push_msg(player):
    """Prints msg to user when he/she has the same hand as the dealer"""
    print("Push! {} and the dealer have the same hand.".format(player.name))

def show_blackjack_msg(player, winnings):
    """Prints msg to user when he/she has blackjack"""
    print("BLACKJACK! {} wins {} dollars".format(
        player.name, winnings)) 

def show_win_msg(player, winnings):
    """Prints msg to user when he/she wins"""
    print("{} wins and gets {} dollars".format(
        player.name, winnings))

def show_loss_msg(player, loss):
    """Prints msg to user when he/she loses"""
    print("{} lost and losses {} dollars".format(
        player.name, loss))

def get_play_again_choice():
        """Game asks player for input to play again, if yes, user/dealer
        stats are reseted. Otherwise, the program ends."""
        while True:
            try:
                choice = str(input("Do you want to play another round? [Y/N]")).strip().upper()
            except ValueError:
                print("Sorry, choose a valid option - Y or N.")
                continue
            if isinstance(choice, int):
                print("Provide a letter not a number")
                continue
            if choice not in ['N','Y']:
                print("Choose Y or N")
                continue
            else:
                return choice

def get_num_players():
    """Return num of players that are playing in the game"""
    while True:
        try:
            num = int(input("How many players are going to play in this round of Blackjack? "))
        except ValueError:
            print("Sorry, choose a valid option.")
            continue
        if isinstance(num, str):
            print("Provide a number not a letter or a word")
            continue
        else:
            return num

def get_player_name(count):
    """Return the name of the player who is playing"""
    while True:
        try:
            name = str(input(
                "What is player {}'s username? ".format(count+1)))
        except ValueError:
            print("Sorry, choose a valid option")
            continue
        if isinstance(name, int):
            print("Username must letters not numbers")
            continue
        else:
            return name

def show_bet_msg(player):
    """Return the bet of the player"""
    print("You have {} dollars to bet with".format(player.money))
    while True:
        try:
            bet = int(input("{}, What is your minimum bet? ".format(
                player.name)))
        except ValueError:
            print("Sorry, choose a valid number.")
            continue
        if isinstance(bet, str):
            print("Provide a number not a letter or word")
            continue
        elif bet < 1:
            print("Provide a positive bet above zero")
            continue
        elif (player.money - bet) < 0:
            print("You don't have enough money to bet this amount.")
            continue
        else:
            return bet

def show_create_player_msg(name):
    """Return the players choice to create a new player or not"""
    while True:
        try:
            choice = str(input("The username {} could not be found. Do you want to create a new user with this username? [Y/N]".format(
                name))).strip().upper()
        except ValueError:
            print("Sorry, choose a valid option- Y or N")
            continue
        else:
            return choice

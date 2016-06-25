A strategic game of blackjack that is played entirely in the command line.
===

Current Features:
---
- Currently supports only Python3
- Gameplay and strategy is similar to real-life casino blackjack. For example, players have to bet a minimnum amount of money to play. Also, in some casinos the dealer is required to hit on soft 17. 
- Infinite amount of players can play in a single game
- Users can create players and save their *digital dollars*, wins, and losses to a JSON file. But of course you can open and edit this file as freely as you want. 
- The CLI provides a menu with various gaming options such as allowing the player to view his/her hand, money, current bet, wins, losses, the dealer's hand, or quit or restart the game.


How to Play:
---
- Run the run.py file with Python3 then follow the onscreen prompts. Input the following command `python3 run.py`

To Do/Features to Add:
---
- Implement error handling instead of using if-else statements
- Fix and add to `tests.py`
- Improve documentation
- Reduce code smell
- Implement insurance, doubling-down, and splitting
- Implement multi-deck game
- Package program and use Click to make game into a CLI application?

A fully strategic game of blackjack that is played entirely in the bash/command line.
===


Things to work on:
---
- Create logic for alternative hand values when Ace cards are present in hand
- Re-factor classes (Player, User, Dealer, Game, etc.)
- Documentation
- Reduce code smell

Features to add:
--- 
- Users, money, bets, insurance, double down
- save wins/losses as pickled/JSON file
- alternate values of Aces (1 or 11)

Ace hand logic:
---

- sample hand= Ace(1), Ace(1), Five of Hearts(5), Seven of Diamonds (7)
- Add up all the ace alternative high values (11) in hand
>> High Ace Hand= 11+11+5+7= 34
>> Low Ace Hand= 1+1+5+7= 14
- if Ace Hand is above 21, subtract 1 Ace Value (-11 + 1 = 10) until it's under 21
>> High Ace Hand= 34-10= 24
>> High Ace Hand= 24-10= 14
- Compare high ace hand to low ace hand and set current to value of current hand

- Other example

>> sample hand = Ace(1), 6 (11+6= 17 or 1+6= 7)
- Let's say user hits... delt card = 7
>> sample hand = 11+6+7 = 24
- Count aces in hand, if any. If there are and hand is above 21 subtract 10 until it is.
>> 1 ace found, so new hand is 14 (24-10= 14). Then ask to hit or stand again.
- If no aces, and user hasnt busted, ask hit or stand, otherwise, end game.

- 2nd example
>> sample hand = Ace(11), 5
- user decides to hit 
- new card = 7, new hand = 11, 5, 7

- evaluate-score:
  if 1 in self.hand-stack.values()): # check for aces in hand
    if hand is a bust (if check-for-bust()): # check if hand is over 21/a bust
      temp_value = 0
      while not check-for-bust():
        temp_value += 10
      ace-hand -= temp_value
      # print the two possible hands: hand-value and ace-hand
      # hit-or-stand()
    else:
      hit-or-stand()
  else:
    check-for-bust()
      

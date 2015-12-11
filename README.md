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


Psuedo Code:
---
- Dealer is delt one card from the Deck, the User two.
- Game ask User if he wants to "hit or stand":
- If User stands, the hand is shown. Then the dealer's hand is evaluated. If under 18, dealer draws one card from the Deck. If the card is an Ace, the alternate hand is produced and the highest hand is shown. If this hand is under 18, the dealer draws another card until he gets his hand or alternate hand above 17 or busts (>21). If Dealer busts, game ends and User wins. If Dealer doesn't bust, his and the User's hands are compared. The winner is announced. 
- If User hits, one card is drawn from the Deck, if the card is an Ace, the alternate hand is produced and the highest hand is shown. If the alternative hand is below 21, the User is asked to "hit or stand" again. If the alternate hand exceeds 21, the original hand is shown and the User is asked to "hit or stand" again. This repeats until either the User busts or he stands, in which the above will run.

Ace hand logic:
---

- sample hand= Ace(1), Ace(1), Five of Hearts(5), Seven of Diamonds (7)
- Add up all the ace alternative high values (11) in hand
- High Ace Hand= 11+11+5+7= 34
- Low Ace Hand= 1+1+5+7= 14
- if Ace Hand is above 21, subtract 1 Ace Value (-11 + 1 = 10) until it's under 21
- High Ace Hand= 34-10= 24
- High Ace Hand= 24-10= 14
- Compare high ace hand to low ace hand and set current to value of current hand


Other example:
---

- sample hand = Ace(11), 5
- user decides to hit 
- new card = 7, new hand = 11, 5, 7
- possible hands= 23 or 13. Show 13 since Ace hand is over 21.

- get-alt-hand(self):
    temp_hand_value = self.hand_value
  for number in self.hand-stack.values():
    if number == 1: # check for aces in hand
        temp_hand_value += 10
  self.ace-hand-value = temp-hand-value

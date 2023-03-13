#Basic requirements#

#===================
Inital startup - Welcome messages and following text:

PRESS ANY KEY TO PLAY

#Welcome message 
#=====================

----Classic SNAP------


#Pre-Game
#==================

Decks of cards could be lists. 3 decks: 1 full deck, 1 for player 1, 1 for player 2

At the begining of a round, deck 1 is randomly shuffled.
Then the shuffled deck is traversed and cards are assigned sequentially to deck 2 and deck 3.



#During the game
#=================

Program waits for user input. 

Player 1 goes first - their "DEAL" key is d. The program will only accept an input from key d. (or both player's SNAP key)
When "d" is pressed, the first card from player 1's deck is dealt.

Then it will be player 2's go. Player 2's deal key is k. The program will not only accept input from key k. (or both player's SNAP key)
When "k" is pressed, the first card from player 2's deck is dealt.

This pattern of "d" and "k" is continued until:
a) There is a SNAP (see below)
b) The players run out of cards

If the players run out of cards, the main deck is reshuffled and redealt to the players, and then the round resumes

#SNAP
#=================

If, during play, the card that is dealt matches the previous card, the first player to press their "SNAP" key wins the round.
The SNAP keys are "q" for player 1 and "p" for player 2.

If a player hits their SNAP key when there isn't a match, the game will tell them: "No SNAP. The cards do not match!"

If a player hits their SNAP key when there IS a match, the game will tell them: "SNAP. Player <number> is the winner of this round"
The winning player gets "1" added to their rounds_won counter.


#Game end
#=====================

At the end of every round (their must be a winner for every round), the game will check how many rounds have occured.

Once 5 rounds have occurred, the overall winner will be the player with the highest rounds_won counter

#Other ideas
#=================


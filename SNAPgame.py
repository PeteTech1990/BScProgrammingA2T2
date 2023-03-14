#Idea for using "pygame" inspired by https://docs.replit.com/tutorials/python/build-card-game-pygame

#================================================================================================================
#================================================SNAP card game==================================================
#================================================================================================================

#SNAP card game. This is a 2-player card game where a a deck of 52 cards is divided into 2 sets of 26, 1 set per player.
#When each player presses their "deal" key, the card on the top of their deck is played.
#If the current card's "face value" - i.e jack or king or 2 - matches the previous card face value, then the first player to press their "SNAP"
#--key wins the round. The cards are then re-allocated and another round begins.
#After 5 rounds, the overall winner is declared (printed to screen)

#============================================================================================================================================================================

#==========================DEFINING CLASSES================================

#--Defined a class called DECK. This class has one attribute, a list called "cards". DECK objects represent collections of cards in
#--the game. Their will be 3 main DECK objects in the game: the main deck, player 1's deck and player 2's deck. The "cards" list
#--will be populated with objects of the class CARD
class DECK:
    cards = []#--"cards" list variable will contain objects of the class CARD
    
#--Defined a class called CARD. This class has two attributes, a string variable called "suit" and a string variable called "fvalue". 
#--This class has two methods "setSuit" and "setVal". These methods are used to set the suit and fvalue variables with appropraite values.
#--CARD objects represent individual cards in the game. Their will be 52 CARD objects in the game, representing a real world full set of cards    
class CARD:
    suit = ""#--"suit" string variable will contain the suit value for each object of class CARD
    fvalue = ""#--"fvalue" string variable will contain the face value for each object of class CARD
    ID = 0#--"ID" integer variable will contain a unique ID for each object of the class CARD
    
    #--Defined a function called "setSuit" that accepts one string parameter and assigns it to the variable "suit_to_set"
    #--The function then assigns the string value in "suit_to_set" to the "suit" variable
    def setSuit(self, suit_to_set):
        self.suit = suit_to_set
      
    #--Defined a function called "setFVal" that accepts one string parameter and assigns it to the variable "fval_to_set"
    #--The function then assigns the string value in "fval_to_set" to the "fvalue" variable  
    def setFVal(self, fval_to_set):
        self.fvalue = fval_to_set
        
#=====================================================================================================================================================================

#=============================DECLARING VARIABLES====================================

#--Declared and populated a list variable called "suits" with 4 string values, each representing one of the suits in a deck of cards
suits = ["♠", "♥", "♣", "♦"]

#--Declared and populated a list variable called "fvalues" with 4 string values, each representing one of the non-numerical face values in a deck of cards
fvalues = ["J", "Q", "K", "A"]

#--Declared a list variable called "main_board" that will represent the main game board for the card game. With each card that is played, a card 
#--object will be appended to the "main_board" list
main_board = []

#--Declared a list variable called "scoreboard" that will represent the scoreboard for the card game. Each time a player wins a round, an integer value
#--will be added to the list, representing the player that won the round
scoreboard = []


#=====================================================================================================================================================================

#=============================INSTANTIATING OBJECTS====================================

#--Declared an instance of a DECK class object, called "main_deck". This object will respresent the main deck of 52 cards for the game.
#--This object will be populated with 52 CARD objects at the beginning of the game. All of the CARD object will return to this object at the
#--end of every round, in order to be re-shuffled and re-dealt to the player DECK objects.
main_deck = DECK

#--Declared an instance of a DECK class object, called "p1_deck". This object will respresent player 1's deck, which will be populated with CARD objects
#--at the beginning of every round.
p1_deck = DECK

#--Declared an instance of a DECK class object, called "p2_deck". This object will respresent player 2's deck, which will be populated with CARD objects
#--at the beginning of every round.
p2_deck = DECK



#=====================================================================================================================================================================

#=============================DEFINING FUNCTIONS====================================

populateDeck (round_count):
    if (round_count == 0):
        ID = 1
        for suit in suits:
            for count in range(13):
                current_card = CARD
                current_card.suit = suit
                if count < 10:
                    current_card.fvalue = count
                else:
                    current_card.fvalue = values[count-9]
                
                current_card.ID = ID
                ID += 1

                main_deck.cards.append(current_card)
    else:
        for count in len(p1_deck.cards):
            main_deck.cards.append(p1deck.cards.pop())
        for count in len(p2_deck.cards):
            main_deck.cards.append(p2deck.cards.pop())

#SHUFFLE function
using RANDOM module
    FOR count in range(52):
        index1 = randrange(52)
        index2 = randrange(52)

        card1 = main_deck[index1]
        card2 = main_deck[index2]

        if card1.ID <> card2.ID:
            main_deck.cards[index1] = card2
            main_deck.cards[index2] = card1


#DEAL function
    for count in range(26):

        pl_deck.cards.append(maindeck.cards.pop())
        p2_deck.cards.append(maindeck.cards.pop())
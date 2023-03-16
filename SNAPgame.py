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

#==========================IMPORTING MODULES================================

import random #--RandRange method of random module will be used in the function for shuffling the main deck


#============================================================================================================================================================================

#==========================DEFINING CLASSES================================

#--Defined a class called DECK. This class has one attribute, a list called "cards". DECK objects represent collections of cards in
#--the game. Their will be 1 DECK objects in the game. The "cards" list instance variable will be populated with objects of the class CARD
class DECK:
    
    #--Defined the initializer method for the "DECK" class. This method is automatically called whenever a new instance of the DECK class is created.
    #--The newly created object is passed as a parameter to the initializer method, assigned to the name "self"
    #--The initializer method for this class creates the instance attribute/variable for the new object, "cards".
    #--This is the attribute that the DECK object will need, during the game. The attribute is assigned a "blank" list, initially.
    def __init__(self):
        self.cards = []
     
       
    #--Defined a method called "populateDeck". Method accepts one parameter, which is assigned to the variable "self". This is because this
    #--method needs to act on the state data within a particular instance of this object. The state data it works is the object's list called "cards".
    #--When this method is called, a parameter will not need to be explicitly passed into "self". This is an implicit function in python. When a object's method
    #--is called, the object itself is automatically passed as a parameter.
    #--The purpose of the function is to populate the main deck with cards (by creating 52 CARD objects) at the beginning of the game
    def populateDeck (self):
            
        ID = 1 #--Variable "ID" is assigned an integer variable 1. This variable will be used to assign a unique card ID value to each CARD object, as they are created
        
        #--FOR loop. The iterable sequence for this loop is the list "suits", with the iterator variable looping through each of the string values contained
        #--in "suits". These string values represent the 4 "suits" in a game of cards
        for suit in suits:
            
            #--Nested FOR loop. The iterable sequence for this loop is a range list with 13 indices, with the iterator variable "count" looping through each of the integer values contained
            #--in the range list. These string values represent the 13 "face values" in a game of cards
            for count in range(13):
                
                ##======These two FOR loops together will be used to create each of the 52 CARD objects that will be stored in the main_deck object.
                #--With each iteration of the first FOR loop, 13 nested FOR loops iterations (one for each card in the suit) will occur
                #--With each iteration of the nested FOR loop, 1 CARD will be created, given a suit value, a face value, a unique ID, then appended to the "card"
                #--list of the DECK object "main_deck" 
                
               # current_card = CARD()#--Instantiation of a new CARD class object, which is assigned to variable "current_card"
               # current_card.setSuit(suit)#--Assign the current value of "suit" variable to the "suit" attribute of the "current_card" CARD object
                
                #--IF the current integer value assigned to "count" is less than 9, then execute the IF code block. (The first 9 cards within a suit
                #--have numerical face values, so the "count" variable can be used to assign their "fvalue" attribute)
                if count < 9:
                    
                    current_card = CARD(suit, count+2, ID)
                                        
                    #current_card.setFVal(count+2) #-Assign the value of "count" plus 2 to the "fvalue" attribute of the "current_card" object
                    #--For example, if "count" is 0, then a value of 2 will be assigned to the "fvalue" attribute. On the first iteration of the FOR loop, 
                    #--the first card in the suit is created. The first card in the suit is "2".
            
                #--ELSE the current integer value assigned to "count" is equal to or more than 9. Then the ELSE code block will execute.
                #--(After the first 9 cards within a suit, the remaining 4 have string face values, so the "count" variable 
                #--now needs to be used to assign a string from the "fvalues" list to the CARD object's "fvalue" attribute)
                else:
                    
                    current_card = CARD(suit, fvalues[count-9], ID)
                    
                    #current_card.setFVal(fvalues[count-9])#-Assign the value at the index of "count" minus 9 in the "fvalues" list to the
                                                        #--"favlue" attribute of the "current_card" object
                    #--For example, if "count" is 10, then the value at index 1 of the fvalues list (which is "Q") will be assigned to the "fvalue" 
                    #--attribute. On the 10th, 11th, 12th and 13th iteration of the FOR loop, the last cards in the suit are created. 
                    #--The last cards in the suit are "J", "Q", "K" and "A" - representing Jack, Queen, King and Ace respectively.
                
                #current_card.setID(ID)#--The "ID" attribute of the "current_card" object is assigned the integer value currently assigned to the
                                    #--variable "ID". This is to assign a unique ID code to each individual CARD object
                
                ID += 1 #--The value currently assigned to "ID" is incremented by 1, so that the next CARD object created in the next FOR loop iteration
                        #--will have a different ID code

                #--The newly instantiated CARD object currently assigned to "current_card" is appended to the "cards" list attribute of the "self" DECK object
                self.cards.append(current_card)
                                    
             
        
    #--Defined a function called "shuffle". Function does not accept parameters.
    #--The purpose of the function is to re-order all of the CARD objects in the "cards" list of the "main_deck" object, randomly.
    #--This simulates a random shuffle of the deck before the beginning of a round

    def shuffle(self):
        
        #--The shuffling mechinism works in this way:
        #--Using the "randrange" method of the "random" module, 2 random integers between 0 - 51 will be obtained, one assigned to the variable "index1"
        #--and one assigned to the variable "index2". These 2 indices represent 2 cards in the main deck that will swap places.
        #--2 new instances of the CARD class will be created. One will be assigned the CARD object located at the "index1" index of the "cards" list of the 
        #--"main_deck" object and the other will be assigned the CARD object located at the "index2" index of the same list. These are the 2 CARD objects
        #--that will be swapping places. Then, after making sure that the program is not attempting to swap a CARD object with itself, the CARD objects are
        #--inserted into the index of the other CARD object, in the "cards" list. These CARD objects have now been swapped.
        #--Using the FOR loop, this random swap will occur 52 times when this function is called.
        
        #--FOR loop. The iterable sequence for this loop is a range list with a number of indicies equal to 52
        #--The iterator variable "count" will looping through each of the integer values contained in the range list. 
        #--Therefore there will be one iteration for every CARD object in the "main_deck" object.
        for count in range(52):
            
            #--Using the "randrange" method of the "random" module, obtain a random integer value between 0 and 51 and assign that value to the variable "index1"              
            swap_index_1 = random.randrange(52)
            
            #--Using the "randrange" method of the "random" module, obtain a random integer value between 0 and 51 and assign that value to the variable "index2"
            swap_index_2 = random.randrange(52)

            #--Obtain the CARD object located at the "swap_index_1" index of the "cards" list of the "main_deck" object, and assign that CARD object
            #--to a new instance of the CARD class, called "first_card_to_be_swapped"
            first_card_to_be_swapped = self.cards[swap_index_1]
            
            #--Obtain the CARD object located at the "swap_index_2" index of the "cards" list of the "main_deck" object, and assign that CARD object
            #--to a new instance of the CARD class, called "second_card_to_be_swapped"
            second_card_to_be_swapped = self.cards[swap_index_2]           

            #--IF statement code block will execute if the value of "ID" attributes of the 2 CARD objects are NOT equal 
            #--(This means that these are NOT the same CARD objects, identified by their unique card IDs.)
            #--The purpose of this IF statement is to prevent an error occuring from trying to overwrite a CARD object
            #--in the "cards" list of "main_deck" with itself.
            if first_card_to_be_swapped.getID != second_card_to_be_swapped.getID:
                #--IF these are not the same CARD objects
                
                #--Overwrite the CARD object at index "swap_index_1" with the CARD object assigned to "second_card_to_be_swapped"
                self.cards[swap_index_1] = second_card_to_be_swapped
                
                #--Overwrite the CARD object at index "swap_index_1" with the CARD object assigned to "second_card_to_be_swapped"
                self.cards[swap_index_2] = first_card_to_be_swapped

            
    def deal(self):
        pdeck1 = []
        pdeck2 = []
        for count in range(26):
            pdeck1.append(self.cards.pop())
            pdeck2.append(self.cards.pop())
        
        return pdeck1,pdeck2
    
    
    def returnCards(self, deck):
        
        for card in deck:
            self.cards.append(card)
            #p1_deck.cards.append(main_deck.cards.pop())
            #p2_deck.cards.append(main_deck.cards.pop())
    
#--Defined a class called CARD. This class has two attributes, a string variable called "suit" and a string variable called "fvalue". 
#--This class has two methods "setSuit" and "setVal". These methods are used to set the suit and fvalue variables with appropraite values.
#--CARD objects represent individual cards in the game. Their will be 52 CARD objects in the game, representing a real world full set of cards    
class CARD:
    
    #--Defined the initializer method for the "CARD" class. This method is automatically called whenever a new instance of the CARD class is created.
    #--The newly created object is passed as a parameter to the initializer method, assigned to the name "self"
    #--The initializer method for this class creates the 3 instance attributes/variables for the new object, "suit", "fvalue" and "ID".
    #--These are the attributes that each CARD object will need, during the game. The 3 attributes are assigned "blank" or 0 values, initially.
    def __init__(self, suit_to_set, fvalue_to_set, id_to_set):           
        self.suit = suit_to_set#--"suit" string variable/attribute will contain the suit value for the new CARD object. Initial value for "suit" is "" for each instance
        self.fvalue = fvalue_to_set#--"fvalue" string variable/attribute will contain the face value for the new CARD object. Initial value for "fvalue" is "" for each instance
        self.ID = id_to_set#--"ID" integer variable/attribute will contain a unique ID for the new CARD object. Initial value for "ID" is 0 for each instance
    
    #--Defined a function called "setSuit" that accepts one string parameter and assigns it to the variable "suit_to_set"
    #--The function then assigns the string value in "suit_to_set" to the "suit" variable
    #def setSuit(self, suit_to_set):
      #  self.suit = suit_to_set
      
    #--Defined a function called "setFVal" that accepts one string parameter and assigns it to the variable "fval_to_set"
    #--The function then assigns the string value in "fval_to_set" to the "fvalue" variable  
   # def setFVal(self, fval_to_set):
      #  self.fvalue = fval_to_set
        
  #  def setID(self, id_to_set):
     #   self.ID = id_to_set
     
    def __str__(self):
        return "|{:^3}{:^3}|".format(self.suit, self.fvalue)
        
    def getSuit(self):
        return self.suit
        
    def getFVal(self):
        return self.fvalue   
    
    def getID(self):
        return self.ID  
        
#=====================================================================================================================================================================

#=============================DECLARING VARIABLES====================================

#--Declared and populated a list variable called "suits" with 4 string values, each representing one of the suits in a deck of cards
suits = ["♠", "♥", "♣", "♦"]

#--Declared and populated a list variable called "fvalues" with 4 string values, each representing one of the non-numerical face values in a deck of cards
#--(Jack, Queen, King and Ace)
fvalues = ["J", "Q", "K", "A"]

#--Declared a list variable called "gameboard" that will represent the main game board for the card game. With each card that is played, a card 
#--object will be appended to the "gameboard" list
gameboard = []

#--Declared a list variable called "scoreboard" that will represent the scoreboard for the card game. Each time a player wins a round, an integer value
#--will be added to the list, representing the player that won the round
scoreboard = []


#=====================================================================================================================================================================

#=============================INSTANTIATING OBJECTS====================================

#--Declared a new instance of a DECK class object, called "main_deck". This object will respresent the main deck of 52 cards for the game.
#--This object will be populated with 52 CARD objects at the beginning of the game. All of the CARD object will return to this object at the
#--end of every round, in order to be re-shuffled and re-dealt to the player DECK objects.
main_deck = DECK()



#=====================================================================================================================================================================

#=============================DEFINING FUNCTIONS====================================


        
main_deck.populateDeck()#--Invokation of "populateDeck" method, for the "main_deck" DECK object, using dot notation
main_deck.shuffle()
p1_deck, p2_deck = main_deck.deal()

def check_snap():
        
    card_val1 = gameboard[-1].getFVal()
    card_val2 = gameboard[-2].getFVal()
    
    if card_val1 == card_val2: 
        print("SNAP")

gameboard.append(p1_deck.pop())
print(gameboard[-1])

for count in range(25):
    gameboard.append(p2_deck.pop())
    print(gameboard[-1])
    check_snap()
    
    gameboard.append(p1_deck.pop())
    print(gameboard[-1])
    check_snap()
    

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

#--Importing the "random" module
import random #--RandRange method of random module will be used in the function for shuffling the main deck

#--Importing the "os" module
import os#--The "system" method of the os module will be used to execute windows command prompt commands in the terminal. Specifically, the 'cls' command
         #--prompt command will be used to clear all text from the terminal



#============================================================================================================================================================================

#==========================DEFINING CLASSES================================

#--Defined a class called DECK. This class has one attribute, a list called "cards". DECK objects represent collections of cards in
#--the game. Their will be 1 DECK objects in the game. The "cards" list instance variable will be populated with objects of the class CARD
class DECK:
    
    #--Defined the initializer method for the "DECK" class. This method is automatically called whenever a new instance of the DECK class is created.
    #--The newly created object is passed as a parameter to the initializer method, assigned to the name "self"
    #--The initializer method for this class creates the instance attribute/variable for the new object, called "cards".
    #--This is an attribute that the DECK object will need during the game. The attribute "cards" is assigned a blank list, initially.
    def __init__(self):
        self.cards = []
     
       
    #--Defined a method called "populateDeck". Method accepts one parameter, which is assigned to the variable "self". "Self" will store a particular instance of
    #--a DECK object so that the program can act on the state data within that instance. The state data it will work on is the object's "cards" list.
    #--When this method is called, a parameter will not need to be explicitly passed into "self". This is an implicit function in python. When a object's method
    #--is called, the object itself is automatically passed as a parameter.
    #--The purpose of the function is to populate the main deck with cards (by creating 52 CARD objects) at the beginning of the game
    def populateDeck (self):
            
        ID = 1 #--Variable "ID" is assigned an integer variable 1. This variable will be used to assign a unique card ID value to each CARD object, as they are created
        
        ##======These two FOR loops together will be used to create each of the 52 CARD objects that will be stored in the main DECK object.
        #--With each iteration of the first FOR loop, 13 nested FOR loops iterations (one for each card in the suit) will occur
        #--With each iteration of the nested FOR loop, 1 CARD object will be instantiated with a suit value, a face value, a unique ID, then appended to the "card"
        #--list of the passed DECK object
        
        #--FOR loop. The iterable sequence for this loop is the list "suits", with the iterator variable "suit" looping through each of the string values contained
        #--in "suits". These string values represent the 4 "suits" in a game of cards
        for suit in suits:
            
            #--Nested FOR loop. The iterable sequence for this loop is a range list with 13 indices, with the iterator variable "count" looping through each of the integer values contained
            #--in the range list. These string values represent the 13 "face values" in a game of cards
            for count in range(13):

                #--IF the current integer value assigned to "count" is less than 9, then execute the IF code block. (The first 9 cards within a suit
                #--have numerical face values, so the "count" variable can be used to assign their "fvalue" attribute)
                if count < 9:
                    
                    #--Instantiation of a new CARD class object, which is assigned to variable "current_card"
                    #--3 values are passed to the "__init__" method of the CARD class, in order to instantiate this instance of the CARD object.
                    #--These values are:
                    #-----1. The value currently assigned to "suit", which will be a string value from the list "suits". This value will be stored
                    #-----in the "suit" attribute of the "current_card" CARD object. This represents the suit of the CARD object.
                    #-----2. The value currently assigned to "count", plus 2. This value will be stored
                    #-----in the "fvalue" attribute of the "current_card" CARD object. This represents the face value of the CARD object.
                    #-----For example, if "count" is 0, then a value of 2 will be assigned to the "fvalue" attribute. So, on the first iteration of the FOR loop, 
                    #-----the first card in the suit is created. And the first card in a suit is "2".
                    #-----3. The value currently assigned to "ID". This value will be stored in the "ID" attribute of the 
                    #-----"current_card" CARD object. This is the unique ID value for the CARD object.
                    current_card = CARD(suit, count+2, ID)
                      
                    
                #--ELSE the current integer value assigned to "count" is equal to or more than 9. Then the ELSE code block will execute.
                #--(This is because after the first 9 cards within a suit, the remaining 4 have string face values, so the "count" variable 
                #--now needs to be used to assign a string from the "fvalues" list, to the CARD object's "fvalue" attribute, rather than using the
                #--value from the count variable as the fvalue itself). So, on the 10th, 11th, 12th and 13th iteration of the nested FOR loop, the 
                #--last cards in the suit are created. The last cards in the suit are "J", "Q", "K" and "A" - representing Jack, Queen, King and Ace respectively.
                else:
                    
                    #--Instantiation of a new CARD class object, which is assigned to variable "current_card"
                    #--3 values are passed to the "__init__" method of the CARD class, in order to instantiate this instance of the CARD object.
                    #--These values are:
                    #-----1. The value currently assigned to "suit", which will be a string value from the list "suits". This value will be stored
                    #-----in the "suit" attribute of the "current_card" CARD object. This represents the suit of the CARD object.
                    #-----2. The value at the index of ("count" minus 9) in the "fvalues" list. This value will be stored
                    #-----in the "fvalue" attribute of the "current_card" CARD object. This represents the face value of the CARD object.
                    #-----For example, if "count" is 10, then the value at index 1 ("count" minus 9) of the fvalues list (which is "Q") will be 
                    #-----assigned to the "fvalue" attribute.
                    #-----3. The value currently assigned to "ID". This value will then be stored in the "ID" attribute of the 
                    #-----"current_card" CARD object. This is the unique ID value for the CARD object.
                    current_card = CARD(suit, fvalues[count-9], ID)
                
                #--The newly instantiated CARD object currently assigned to "current_card" is appended to the "cards" list attribute of the "self" DECK object
                self.cards.append(current_card)
                
                ID += 1 #--The value currently assigned to "ID" is incremented by 1, so that the next CARD object created in the next FOR loop iteration
                        #--will have a different ID code
                                    
     
             
        
    #--Defined a method called "shuffle". Method accepts one parameter, which is assigned to the variable "self". "Self" will store a particular instance of
    #--a DECK object so that the program can act on the state data within that instance. The state data it will work on is the object's "cards" list.
    #--The purpose of the method is to re-order all of the CARD objects in the "cards" list of the "self" DECK object, randomly.
    #--This simulates a random shuffle of the deck before the beginning of a round

    def shuffle(self):
        
        #--The shuffling mechinism works in this way:
        #--Using the "randrange" method of the "random" module, 2 random integers between 0 - 51 will be obtained, one assigned to the variable "index1"
        #--and one assigned to the variable "index2". These 2 indices represent 2 cards in the DECK that will swap places.
        #--2 new instances of the CARD class will be created. One will be assigned the CARD object located at the "index1" index of the "cards" list of the 
        #--"self" DECK object and the other will be assigned the CARD object located at the "index2" index of the same list. These are the 2 CARD objects
        #--that will be swapping places. Then, after making sure that the program is not attempting to swap a CARD object with itself, the CARD objects are
        #--inserted into the index of the other CARD object, in the "cards" list, overwriting the original 2 CARD objects that were in the list. 
        #--These CARD objects have effectively been swapped, though in reality they were copied, reversed and written over the originals.
        #--Using the FOR loop, this random swap will occur 52 times when this method is called.
        
        #--FOR loop. The iterable sequence for this loop is a range list with a number of indicies equal to 52
        #--The iterator variable "count" will loop through each of the integer values contained in the range list. 
        #--Therefore there will be one iteration for every CARD object in the "self" DECK object. The number 52 is
        #--arbitrary and only really has an impact on performance and "degree of shuffling". I could specify a higher number, 
        #--resulting in more shuffle operations (more system resources required) but with a more throughly shuffled DECK object
        for count in range(52):
            
            #--Using the "randrange" method of the "random" module, obtain a random integer value between 0 and 51 and assign that value to the variable "index1"              
            swap_index_1 = random.randrange(52)
            
            #--Using the "randrange" method of the "random" module, obtain a random integer value between 0 and 51 and assign that value to the variable "index2"
            swap_index_2 = random.randrange(52)

            #--Obtain the CARD object located at the "swap_index_1" index of the "cards" list of the "self" DECK object, and assign that CARD object
            #--to a new instance of the CARD class, called "first_card_to_be_swapped"
            first_card_to_be_swapped = self.cards[swap_index_1]
            
            #--Obtain the CARD object located at the "swap_index_2" index of the "cards" list of the "self" DECK object, and assign that CARD object
            #--to a new instance of the CARD class, called "second_card_to_be_swapped"
            second_card_to_be_swapped = self.cards[swap_index_2]           

            #--IF statement code block will execute if the value of "ID" attributes of the 2 new CARD objects are NOT equal 
            #--(This means that these are NOT the same CARD objects, identified by their unique card IDs.)
            #--The purpose of this IF statement is to prevent an error occuring from trying to overwrite a CARD object
            #--in the "cards" list of "self" with itself. This error would not cause an exception, but would be a waste
            #--of resources. It would be like taking a single card out of the deck and putting it back in the exact same place
            #--If the statement evaluates to True, then the code block will execute. The code block has 2 lines: 1 is for overwriting
            #--the first CARD object with the second CARD object, and the other line does the opposite. These 2 lines cause the 
            #--2 cards to be swapped in the "cards" list. 
            #--The ID values for each of the CARD objects are returned when the "getID" method of the CARD class is called
            if first_card_to_be_swapped.getID != second_card_to_be_swapped.getID:#--IF these are not the same CARD objects
                
                #--Overwrite the CARD object at index "swap_index_1" of the "cards" list of the "self" DECK object
                #--with the CARD object assigned to "second_card_to_be_swapped"
                self.cards[swap_index_1] = second_card_to_be_swapped
                
                #--Overwrite the CARD object at index "swap_index_2" of the "cards" list of the "self" DECK object
                #--with the CARD object assigned to "first_card_to_be_swapped"
                self.cards[swap_index_2] = first_card_to_be_swapped

    #--Defined a method called "deal". Method accepts one parameter, which is assigned to the variable "self". "Self" will store a particular instance of
    #--a DECK object so that the program can act on the state data within that instance. The state data it will work on is the object's "cards" list.
    #--The purpose of the method is create 2 new lists, called "player_deck_1" and "player_deck_2", and then sequentially assign the CARD objects from 
    #--the "self" DECK object into these 2 lists. After the method has executed, both lists should contain 26 CARD objects each and will then be returned 
    #--back to the line that called the method.
    #--The 2 lists represent the decks of cards that are assigned to each player during the game. This method simulates the
    #--dealing out of cards from the main deck to each player.       
    def deal(self):
        
        #--2 empty lists are declared.
        player_deck_1 = []
        player_deck_2 = []
        
        #--FOR loop. The iterable sequence for this loop is a range list with a number of indicies equal to 26.
        #--The iterator variable "count" will loop through each of the integer values contained in the range list. 
        #--Therefore there will be one iteration for every 2 CARD objects in the "self" DECK object. 1 CARD object is 
        #--assigned to each of the 2 lists with each iteration, meaning after 26 iterations, all 52 CARD objects will
        #--will have been "dealt" into the lists
        for count in range(26):
            #--On each iteration, using the pop method, remove the CARD object from the last index from the "cards" list of the "self" DECK object 
            #--and append that CARD object to the player_deck_1 list
            player_deck_1.append(self.cards.pop())
            
            #--On each iteration, using the pop method, remove the CARD object from the last index from the "cards" list of the "self" DECK object 
            #--and append that CARD object to the player_deck_2 list
            player_deck_2.append(self.cards.pop())
        
        #--At the end of the method, the 2 new created and populated player deck lists are returned back to the line that called the method
        return player_deck_1,player_deck_2
    
    #--Defined a method called "returnCards". Method accepts 2 parameters, which are assigned to the variable "self" and "returned_cards". 
    #--"Self" will store a particular instance ofa DECK object so that the program can act on the state data within that instance. 
    #--The state data it will work on is the object's "cards" list.
    #--"returned_cards" will store a list of cards that are to be put into the "cards" list of the "self" DECK object
    #--The purpose of the method is to return any CARD objects that are currently held in the 2 player decks or on the gameboard back into
    #--the main DECK object, at the end of a round of SNAP. This is so the cards can be re-shuffled and re-dealt before the next round.
    #--The method will return an empty list object that will be used to wipe any objects from the player decks and the gameboard before a new round
    #--begins.
    def returnCards(self, returned_cards):
        
        #--FOR loop. The iterable sequence for this loop is the list the was passed into "returned_Cards", with the iterator variable "card"
        #--looping through each of the CARD objects contained in "returned_cards". These CARD objects represent cards that may have been in
        #--a player's deck or on the gameboard, which now need to be returned to the main deck before the next round
        for card in returned_cards:
            #--On each iteration, append the CARD object currently stored in the variable "card" to the "cards" list of the "self" DECK object.
            #--This is simulating the returning of a single card from a player deck/gameboard back into the main deck.
            self.cards.append(card)
        
        return []#--Return a blank list. This will wipe any CARD objects from the list that called this method
            
    
#--Defined a class called CARD. This class has three instance attributes, a string variable called "suit",a string variable called "fvalue" and an integer variable
#--called "ID". This class also has five methods, the initialise method, the __str__ method, the "getSuit", "getFVal" and "getID" methods. These will be
#--explained lower down.
#--CARD objects represent individual cards in the game. Their will be 52 CARD objects in the game, representing a real world full set of cards    
class CARD:
    
    #--Defined the initializer method for the "CARD" class. This method is automatically called whenever a new instance of the CARD class is created.
    #--The newly created CARD object is passed as a parameter to the initializer method, assigned to the name "self".
    #--This method also accepts 3 other parameters: "suit_to_set", "fvalue_to_set", "id_to_set"
    #--The initializer method for this class creates the 3 instance attributes/variables for the new object, "suit", "fvalue" and "ID".
    #--These are the attributes that each CARD object will need, during the game. The 3 attributes are assigned the values passed into
    #--"suit_to_set", "fvalue_to_set" and "id_to_Set" respectively
    def __init__(self, suit_to_set, fvalue_to_set, id_to_set):           
        self.suit = suit_to_set#--"suit" string variable/attribute will contain the suit value for the new CARD object. 
        self.fvalue = fvalue_to_set#--"fvalue" string variable/attribute will contain the face value for the new CARD object. 
        self.ID = id_to_set#--"ID" integer variable/attribute will contain a unique ID for the new CARD object. 
    
    
    #--Defined the str method for the "CARD" class. This method is automatically called whenever an object of the CARD class is passed
    #--as a parameter to the "print" function. In essence, this method defines the behaviour of a CARD object when it is outputted to the screen.
    #--The method accepts one parameter, which is assigned to the variable "self". "Self" will store a particular instance of
    #--a CARD object so that the program can print the state data within that instance. The state data it will print is the object's "suit" value,
    #--and "face" value.
    #--The method will return a multi-line string that resembles a real-life playing card. The output will be a rectangular shape, stood up on one of
    #--it's shorter sides. In each corner of the rectangle, the CARD object's "fvalue" value will be printed. In the centre of the rectangle, the
    #--CARD object's "suit" value will be printed
    def __str__(self):
        
        #--Using the format method for the returned string, a multi-line string will be created, using placeholder braces to insert the "fvalue" and
        #--"suit" values into the correct places. The first and last rows of the string is a line of "-" symbols. These represent the top and bottom sides
        #--of the card. The second and sixth rows of the string contain a "|" symbol on the left and right sides, representing the sides of the card. Also, 
        #--these rows contain 2 placeholder {}, which use the formatting type :<5 and :>5, meaning the values that will be held within these braces will be
        #--left and right aligned within a 5 character space, respectively. The value passed into these 2 placeholders is the CARD's "fvalue" or face value. 
        #--This emulates the 2 face values that appear at the top of a playing card. The total space between the two "|" symbols is 10 characters.
        #--The third and fifth rows of the string contain a "|" symbol on the left and right sides, representing the sides of the card. Also, 
        #--these rows contain a 10 characater gap between the "|"symbols. 
        #--These lines emulate the gap between the face values and the suit symbol on a real playing card.
        #--Finally, the fourth row of the string contains a "|" symbol on the left and right sides, representing the sides of the card. Also, 
        #--this row contain 1 placeholder {}, which uses the formatting type :^10, meaning the value that will be held within this brace will
        #--be centrally aligned within a 10 character space, respectively. The value passed into these 2 placeholders is the CARD's "suit" value. 
        #--This emulates the suit symbol that appears in the centre of a playing card. The total space between the two "|" symbols is 10 characters.
        #--Altogether, these seven rows produce a multiline string that resembles a real-life playing card.
        return """------------
|{:<5}{:>5}|
|          |
|{:^10}|
|          |
|{:<5}{:>5}|
------------""".format(self.fvalue, self.fvalue, self.suit, self.fvalue, self.fvalue)
    
    #--Defined a method called "getSuit" The method accepts one parameter, which is assigned to the variable "self". 
    #--"Self" will store a particular instance of a CARD object so that the program can work on the state data within that instance. 
    #--The state data it will work on is the object's "suit" value.
    #--The method will return the "suit" string value belonging to the particular instance of the CARD class that called this method.
    #--The purpose of this method is to provide a way for the program to query the "suit" value for a particular CARD object
    #--without being able to access or change the specific value itself. The "suit" value will remain "private" in terms of its encapsulation.
    #--This is to ensure that the "suit" variables for specific CARD objects do not interfere with each other and cannot be accidentally changed by
    #--other parts of the code. The "suit" value of a CARD object should not change once the CARD has been instantiated, as it is representing a
    #--a real-life card, which cannot change its suit.
    #--Only the "getSuit" function, within the specific instance of the CARD object, will be able to access the "suit" value for that object.        
    def getSuit(self):
        return self.suit
    
    
    #--Defined a method called "getFVal" The method accepts one parameter, which is assigned to the variable "self". 
    #--"Self" will store a particular instance of a CARD object so that the program can work on the state data within that instance. 
    #--The state data it will work on is the object's "fvalue" value.
    #--The method will return the "fvalue" string value belonging to the particular instance of the CARD class that called this method.
    #--The purpose of this method is to provide a way for the program to query the "fvalue" value for a particular CARD object
    #--without being able to access or change the specific value itself. The "fvalue" value will remain "private" in terms of its encapsulation.
    #--This is to ensure that the "fvalue" variables for specific CARD objects do not interfere with each other and cannot be accidentally changed by
    #--other parts of the code. The "fvalue" value of a CARD object should not change once the CARD has been instantiated, as it is representing a
    #--a real-life card, which cannot change its face value.
    #--Only the "getFVal" function, within the specific instance of the CARD object, will be able to access the "fvalue" value for that object.       
    def getFVal(self):
        return self.fvalue   
    
    
    #--Defined a method called "getID" The method accepts one parameter, which is assigned to the variable "self". 
    #--"Self" will store a particular instance of a CARD object so that the program can work on the state data within that instance. 
    #--The state data it will work on is the object's "ID" value.
    #--The method will return the "ID" string value belonging to the particular instance of the CARD class that called this method.
    #--The purpose of this method is to provide a way for the program to query the "ID" value for a particular CARD object
    #--without being able to access or change the specific value itself. The "ID" value will remain "private" in terms of its encapsulation.
    #--This is to ensure that the "ID" variables for specific CARD objects do not interfere with each other and cannot be accidentally changed by
    #--other parts of the code. The "ID value of a CARD object should not change once the CARD has been instantiated, as it is representing a
    #--a real-life card, which cannot change its face value.
    #--Only the "getID" function, within the specific instance of the CARD object, will be able to access the "ID" value for that object. 
    def getID(self):
        return self.ID  
        
#=====================================================================================================================================================================

#=============================DECLARING VARIABLES====================================

#--Declared and populated a list variable called "suits" with 4 string values, each representing one of the suits in a deck of cards
suits = ["♠", "♥", "♣", "♦"]

#--Declared and populated a list variable called "fvalues" with 4 string values, each representing one of the non-numerical face values in a deck of cards
#--(Jack, Queen, King and Ace)
fvalues = ["J", "Q", "K", "A"]

#--Declared a list variable called "gameboard" that will represent the main game board for the card game. With each card that is played in a round, a card 
#--object will be appended to the "gameboard" list. At the end of each round, the "gameboard" list will be cleared
gameboard = []

#--Declared a list variable called "scoreboard" that will represent the scoreboard for the card game. Each time a player wins a round, an integer value
#--will be appended to the list, representing the player that won the round. E.g if Player 2 won the round, a 2 integer value would be appended 
#--to the "scoreboard" list
scoreboard = []


#=====================================================================================================================================================================

#=============================INSTANTIATING OBJECTS====================================

#--Declared a new instance of a DECK class object, called "main_deck". This object will respresent the main deck of 52 cards for the game.
#--This object will be populated with 52 CARD objects at the beginning of the game. All of the CARD object will return to this object at the
#--end of every round, in order to be re-shuffled and re-dealt to the player DECK objects.
#--The __init__ initialiser method is called automatically when this object is instantiated. The initialiser method will create the 52 CARD objects
#--for the game and append each one to the "cards" instance list variable for the "main_deck" DECK object.
main_deck = DECK()



#=====================================================================================================================================================================

#=============================DEFINING FUNCTIONS====================================

#--Defined a function called "check_snap". The function accepts one parameter, which will be assigned to the "player" variable. 
#--The function will return a boolean value back to the line that called the function.
#--The purpose of this function is to check whether a player's SNAP! call is valid. 
#--After a card is played during a round, each player will have the opportunity to press their "SNAP" key if they believe the face value of
#--the current CARD object on the gameboard matches the face value of the previous CARD object (as in a game of SNAP). This function checks 
#--if the player is correct. If the 2 CARD object are a match, the function will return "False" (because the boolean value is passed back and 
#--assigned to the variable "round_continue". A value of False means the WHILE loop for the current round does not need to loop again, as a 
#--player has successfully matched 2 cards and the round is over.) If the 2 CARD objects are not a match, the function will return "True" 
#--and the round will continue.
#--The number of the player that called SNAP is passed to the function and assigned to the "player" variable.
def check_snap(player):
              
    #--IF statement code block will execute if length of the "gameboard" list is less than 2 
    #--(This means that there is either 1 or 0 CARD objects in the gameboard list, so there aren't enough CARD objects in the list to 
    #--compare for a match. At least 2 CARD objects are needed before a match can be checked)
    #--The purpose of this IF statement is to prevent an error occuring from trying to compare 2 objects from the gameboard
    #--list when there aren't enough objects in the list
    if len(gameboard) < 2:
        #--The IF statement code block prints out 2 blank lines, plus an error message stating that there aren't enough cards in play
        #--for a SNAP to occur. Finally, the block returns a "True" boolean value back to the line that called the function, meaning the
        #--WHILE loop for the current round will need to loop again, so the round can continue.
        print("")
        print("ERROR - There aren't enough cards in play to SNAP!")
        print("")
        return True
    
    #--ELSE statement code block will execute if length of the "gameboard" list is more than or equal to 2 
    #--(This means that there is at least 2 CARD objects in the gameboard list, so there are enough CARD objects in the list to 
    #--compare for a match.) The purpose of this ELSE statement is to compare the 2 CARD objects currently in the last 2 indicies of the "gameboard"
    #--list. These 2 CARD object represent the last 2 cards to be placed on the gameboard, during the round. The code block uses a nested 
    #--IF ELSE block to test whether there is a match between the face values of the 2 CARD objects
    else:
                
        #--IF statement code block will execute if the face values (fvalue) of the 2 CARD objects in the last 2 indices of the "gameboard" list are equal.
        #--The last 2 indices of the "gameboard" list are obtained using the "-1" and "-2" integers as the index values. Using -1 and -2 will
        #--ensure that that last 2 indices are always obtained, no matter the length of the "gameboard" list
        #--The "fvalue" values for each CARD object are returned when the "getFVal" methods for each of the CARD objects are called.
        #--These fvalues are returned for the CARD objects at indices -1 and -2 in the "gameboard" list and are then compared
        #--If they are a match, then the player that called SNAP is correct and they have won this round. The function will return a boolean value
        #--of "False", meaning the WHILE loop for the current round does not need to loop again.
        
        if gameboard[-1].getFVal() == gameboard[-2].getFVal(): 
            #--The IF statement code block prints out 2 blank lines, plus a success message stating that player that called SNAP is correct and has won
            #--the round. The success message string uses the format method to insert the number of the player that called SNAP into the placeholder
            #--braces within the string.
            #--The number of the player that called SNAP was passed to the function and assigned to the variable "player". The value that was passed
            #--is an integer value, so before it is inserted into the placeholder braces, it is converted to a string value using the "str" function.
            #--After the 2 blank lines and the success message, the value that is currently held in the "player" variable (the number of the player who
            #--called SNAP) is appended to the "scoreboard" list. The purpose of this is to record the winner of the current round, so that after
            #--5 rounds, an overall winner can be declared, based on the mode value within the "scoreboard" list. For a full explanation of this, see the
            #--"printScoreboard" function below. 
            #--Finally, the block returns a "False" boolean value back to the line that called the function, meaning the
            #--WHILE loop for the current round will not need to loop again, and the current round can end.
            print("")
            print("SNAP! Player {} wins this round!".format(str(player)))
            print("")
            scoreboard.append(player)
            return False
        else:
            #--The ELSE statement code block prints out 2 blank lines, plus a failure message stating that player that called SNAP is incorrect 
            #--and is possibly trying to cheat. 
            #--Finally, the block returns a "True" boolean value back to the line that called the function, meaning the
            #--WHILE loop for the current round will need to loop again, so the round can continue.
            print("")
            print("NO SNAP! The cards do not match. No cheating!")
            print("")
            return True

def printInstructions():
    print("")
    print("Classic SNAP! card game")
    print("=======================")
    print("")
    print("")
    print("Instructions:")
    print("")
    print("This is a 2 player game where players must attempt to SNAP a duplicate card before the other player can.")
    print("")
    print("On each round, players will be dealt 26 card. WHen it is their turn, they must deal a card onto the gameboard from their deck")
    print("Player 1's DEAL key is 'D' and Player 2's DEAL key is 'K'")
    print("Each time a card a dealt, only the most recently dealt card will be visible on the gameboard")
    print("")
    print("If a player notices that the most recent card's face value (2, 3, 4...J, Q, K etc) matches the face value of the previous card, then they")
    print("can press their SNAP key to try to win the round")
    print("Player 1's SNAP key is 'Q' and Player 2's SNAP key is 'P'")
    print("If the last 2 cards are a match, then the first player to press their SNAP key wins the round")
    print("")
    print("5 rounds are played and the player with the most rounds won is declared the overall winner of the game!")
    print("")
    print("")
    
def printControls():
    print("")
    print("Classic SNAP! card game")
    print("=======================")
    print("")
    print("")
    print("Player 1 controls: Press D to deal a card and press Q to SNAP")
    print("Player 2 controls: Press K to deal a card and press P to SNAP")
    print("REMEMBER: you must also press ENTER after each key")
    print("")
    
def printScoreboard():
    os.system("cls")
    print("")
    print("==SCOREBOARD==")
    print("--------------")
    print("")
    print("")
    print("---------------------")
    print("| Player    | Score |")
    print("|-----------|-------|")
    print("| Player 1  |{:^7}|".format(scoreboard.count(1)))
    print("| Player 2  |{:^7}|".format(scoreboard.count(2)))
    print("---------------------")
    print("")
    print("")
    input("Press ENTER to continue")
    
def getWinner():
    if scoreboard.count(1) > scoreboard.count(2):
        return 1
    else:
        return 2

#===================================================================================
        
main_deck.populateDeck()#--Invokation of "populateDeck" method, for the "main_deck" DECK object, using dot notation

printInstructions()

print("")
input("PRESS ANY KEY TO BEGIN")
print("")

round_count = 1

while (round_count < 5):
    
    main_deck.shuffle()
    p1_deck, p2_deck = main_deck.deal()
    round_continue = True
    round_count = len(scoreboard)+1
      
    last_player = 0   
    
    while round_continue == True:
        
        os.system('cls')
        
        printControls()
        
        print("Round: {}".format(str(round_count)))
        print("==========")
        print("")
        
        if len(gameboard) == 0:
            print("Top Card: ")
        else:
            print("Top Card:")
            print("")
            print("{}".format(gameboard[-1]))
        
        key_pressed = str(input("Press a key, then press ENTER: ")).upper()
        
        
        match key_pressed:
            case "D":
                if last_player == 1:
                    print("")
                    print("ERROR - Player 2 must play a card next")
                    print("")
                    input()
                elif len(p1_deck) == 0:
                    print("")
                    print("ERROR - Player 1 has no more cards. Cards will be re-dealt and the round will begin again")
                    print("")
                    input()
                    round_continue = False
                else:
                    gameboard.append(p1_deck.pop())
                    last_player = 1
            case "K":
                if last_player == 2:
                    print("")
                    print("ERROR - Player 1 must play a card next")
                    print("")
                    input()
                elif len(p2_deck) == 0:
                    print("")
                    print("ERROR - Player 2 has no more cards. Cards will be re-dealt and the round will begin again")
                    print("")
                    input()
                    round_continue = False
                else:
                    gameboard.append(p2_deck.pop())
                    last_player = 2
            case "P":
                round_continue = check_snap(2)
                input()
            case "Q":
                round_continue = check_snap(1)
                input()
            case default:
                print("")
                print("ERROR - Invalid key pressed. Only 'D', 'K', 'Q' and 'P' are valid")
                print("")
                input()       
                
    gameboard = main_deck.returnCards(gameboard)
    p1_deck = main_deck.returnCards(p1_deck)
    p2_deck = main_deck.returnCards(p2_deck)  
    
    printScoreboard()  

print("")
print("")
print("GAME OVER")
print("")
print("=====================================================================")
print("||After 5 rounds, the overall winner is Player {}! Congratulations!||".format(getWinner()))
print("=====================================================================")
print("")
print("")
input("Press ENTER to quit")           

        
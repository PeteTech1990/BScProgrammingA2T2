<<<<<<< Updated upstream

#================================================================================================================
#================================================SNAP card game==================================================
#================================================================================================================

#SNAP card game. This is a 2-player card game where a a deck of 52 cards is divided into 2 sets of 26, 1 set per player.
#When each player presses their "deal" key, the card on the top of their deck is played.
#If the current card's "face value" - i.e jack or king or 2 - matches the previous card face value, then the first player to press their "SNAP"
#--key wins the round and a score board is printed to the terminal. The cards are then re-allocated and another round begins.
#After 5 rounds, the overall winner is declared and a final score board is printed to the terminal.



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
#--called "ID". This class also has five methods, the initialise method, the __str__ method, the "getFVal" and "getID" methods. These will be
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
        #--Altogether, these seven rows produce ASCII art that resembles a real-life playing card.
        return """------------
|{:<5}{:>5}|
|          |
|{:^10}|
|          |
|{:<5}{:>5}|
------------""".format(self.fvalue, self.fvalue, self.suit, self.fvalue, self.fvalue)
    
 
    
    
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

#--Defined a function called "check_snap". The function accepts one parameter, which will be assigned to the "player_number" variable. 
#--The function will return a boolean value back to the line that called the function.
#--The purpose of this function is to check whether a player's SNAP! call is valid. 
#--After a card is played during a round, each player will have the opportunity to press their "SNAP" key if they believe the face value of
#--the current CARD object on the gameboard matches the face value of the previous CARD object (as in a game of SNAP). This function checks 
#--if the player is correct. If the 2 CARD object are a match, the function will return "False" (because the boolean value is passed back and 
#--assigned to the variable "round_continue". A value of False means the WHILE loop for the current round does not need to loop again, as a 
#--player has successfully matched 2 cards and the round is over.) If the 2 CARD objects are not a match, the function will return "True" 
#--and the round will continue.
#--The number of the player that called SNAP is passed to the function and assigned to the "player_number" variable.
def check_snap(player_number):
              
    #--IF statement code block will execute if the number of items in the "gameboard" list is less than 2 
    #--The number of items in the "gameboard" list is obtained using the "len" function
    #--(This means that there is either 1 or 0 CARD objects in the gameboard list, so there aren't enough CARD objects in the list to 
    #--compare for a match. At least 2 CARD objects are needed before a match can be checked)
    #--The purpose of this IF statement is to prevent an error occuring from trying to compare 2 objects from the gameboard
    #--list when there aren't enough objects in the list
    if len(gameboard) < 2:
        #--The IF statement code block prints out 2 blank lines, plus an error message stating that there aren't enough cards in play
        #--for a SNAP to occur. Finally, the block returns a "True" boolean value back to the line that called the function, meaning the
        #--WHILE loop for the current round will need to loop again, and the round will continue.
        print("")
        print("ERROR - There aren't enough cards in play to SNAP!")
        print("")
        return True
    
    #--ELSE statement code block will execute if the number of items in the "gameboard" list is more than or equal to 2 
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
            #--The number of the player that called SNAP was passed to the function and assigned to the variable "player_number". The value that was passed
            #--is an integer value, so before it is inserted into the placeholder braces, it is converted to a string value using the "str" function.
            #--After the 2 blank lines and the success message, the value that is currently held in the "player_number" variable (the number of the player who
            #--called SNAP) is appended to the "scoreboard" list. The purpose of this is to record the winner of the current round, so that after
            #--5 rounds, an overall winner can be declared, based on the mode value within the "scoreboard" list. For a full explanation of this, see the
            #--"printScoreboard" function below. 
            #--Finally, the block returns a "False" boolean value back to the line that called the function, meaning the
            #--WHILE loop for the current round will not need to loop again, and the current round will end.
            print("")
            print("SNAP! Player {} wins this round!".format(str(player_number)))
            print("")
            scoreboard.append(player_number)
            return False
        else:
            #--The ELSE statement code block prints out 2 blank lines, plus a failure message stating that player that called SNAP is incorrect 
            #--and is possibly trying to cheat. 
            #--Finally, the block returns a "True" boolean value back to the line that called the function, meaning the
            #--WHILE loop for the current round will need to loop again, and the round will continue.
            print("")
            print("NO SNAP! The cards do not match. No cheating!")
            print("")
            return True

#--Defined a function called "printInstructions". The function accepts no parameters, and returns to values. 
#--The purpose of this function is to print multiple strings to the terminal that make up the initial game instructions 
#--that will inform the user how to play the game.
#--The reason why I have chosen to put these print statements into a function, rather than simple in the main game code block
#--is purely for the sake of keeping my code tidy
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


#--Defined a function called "printControls". The function accepts no parameters, and returns to values. 
#--The purpose of this function is to print multiple strings to the terminal that make up the a reminder of the controls for the game
#--These lines will print out at the top of the terminal during every round
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


#--Defined a function called "printScoreboard". The function accepts no parameters, and returns to values. 
#--The purpose of this function is to clear the terminal, then print multiple strings to the terminal that make up the a 
#--visual representation of the current scoreboard.
#--The terminal will be cleared and the scoreboard will be printed out at the end of every round of the game
def printScoreboard():
    
    #--Call the "system" method of the "os" module, in order to execute the windows command prompt command "cls". This command will clear the terminal
    #--before the scoreboard is printed.
    os.system("cls")
    
    #--The next 8 lines will print out blank spaces, a header and the beginning of the scoreboard table
    print("")
    print("==SCOREBOARD==")
    print("--------------")
    print("")
    print("")
    print("---------------------")
    print("| Player    | Score |")
    print("|-----------|-------|")
    
    #--The next two lines print out the strings that make up the main content for the scoreboard, namely the current scores for each player.
    #--The current scores for each player are inserted into the placeholder braces in the string in the following way:
    #--1. The current score for the player is obtained by calling the "count" method on the "scoreboard" list, in order to query to number of occurences
    #----of each player's number in the list. For example, if player 2 has won 3 rounds at this point, then the integer value "2" will occur in the 
    #----in the "scoreboard" list 3 times. This integer value is then passed as a parameter to the "format" method for the string to print.
    #--2. The "format" method of the string is called and passed the parameter from step 1. The formatting type :^7 is used between the placeholder
    #----braces in the string to print. This means that the integer value representing the player's score will be centrally aligned within a 7
    #----character space. This formatting type is used to ensure that the visual representation of the scoreboard that is printer to the terminal
    #----will look correct, no matter the size of the integer that is passed to the format method.
    print("| Player 1  |{:^7}|".format(scoreboard.count(1)))
    print("| Player 2  |{:^7}|".format(scoreboard.count(2)))
    
    #--The next 3 lines will print out the bottom edge of the scoreboard, plus two blank lines
    print("---------------------")
    print("")
    print("")
    
    #--The program prompts the user to press ENTER to continue, using the input function. Using "input" means that the program is paused until the user 
    #--enters a key.
    #--This is to allow the player's to look at the scoreboard before moving on to the next round or ending the game
    input("Press ENTER to continue")


#--Defined a function called "getWinner". The function accepts no parameters. The function will return an integer value that represents
#--the overall winner of the game. 
#--The purpose of this function is to check which player is the overall winner at the end of 5 rounds of the game  
def getWinner():
    
    #--IF statement code block will execute if number of occurences of the integer value 1 is more than the number of occurences of the integer
    #--value 2, in the "scoreboard" list variable. This would mean that player 1 has won more rounds than player 2 and is the overall winner of
    #--the game. The "count" method is called on the "scoreboard" list to query the number of occurences of the passed integer values. An integer
    #--value of 1 is passed to the "count" method to query how many occurences of 1 there are (representing the number of rounds player 1 has won), 
    #--and then the same is done for the integer value 2.
    if scoreboard.count(1) > scoreboard.count(2):
        #--If the above IF statement evaluates to True (meaning the overall winner of the game is player 1), then an integer value of 1 is
        #--passed by to the line that called the function
        return 1
    
    #--ELSE statement code block will execute the logical opposite of the above IF statement is True, i.e if number of occurences of the integer 
    #--value 2 is more than the number of occurences of the integer value 1, in the "scoreboard" list variable. 
    #--This would mean that player 2 has won more rounds than player 1 and is the overall winner of the game. 
    else:
        #--If the above ELSE statement evaluates to True (meaning the overall winner of the game is player 2), then an integer value of 2 is
        #--passed by to the line that called the function
        return 2

#=====================================================================================================================================================================

#=============================MAIN PROGRAM START POINT====================================
 
#--Invocation of "populateDeck" method, on the "main_deck" DECK object, using dot notation
#--This method will create 52 objects of the CARD class and append each one to the "cards" instance variable
#--of the "main_deck" object.    
main_deck.populateDeck()

printInstructions()#--The "printInstructions" method is called, in order to print the game instructions to the terminal

#--2 blank lines are printed. In between those lines, the program prompts the user to press ANY KEY TO BEING, using the input function. 
#--Using "input" means that the program is paused until the user enters a key.
# #--This is to allow the player's to look at the game instructions before beginning the game
print("")
input("PRESS ANY KEY TO BEGIN")
print("")

#--Declare a variable called "round_count".
#--This variable will be used as an accumulator to keep track of how many rounds of SNAP have been played
#--during this game
round_count = 0


#--This WHILE loop code block will execute on a loop for as long as the value assigned to the "round_count" is less than 5.
#--This is because the game will only allow 5 rounds of SNAP to be played before the overall winner is declared and the game is over
#--The program will continue as long as the WHILE loop condition is True. Else the loop will be broken and the program will end
while (round_count < 5):
    
    #---The next 5 lines are executed at the beginning of every round. First, the "shuffle" method is invoked on the "main_deck" DECK object, 
    #--using dot notation. This method will perform 52 random swaps of the CARD objects within the "cards" list of the "main_deck" object. This 
    #--randomization represents the shuffling of the deck of cards before a round of SNAP.
    
    #--The next line invokes the "deal" method on the "main_deck" object. This method will divide the 52 CARD objects into 2 sets of 26 CARD objects
    #--and append each of those sets to 2 new lists. Those list are then returned from the method and assigned to the lists "p1_deck" and "p2_deck" respectively.
    #--This represents the dealing of all the cards from a deck to the 2 players before each round of SNAP. The "p2_deck" and "p2_deck" lists represent
    #--the set of 26 cards that each player has at the beginning of a round of SNAP.
   
    #--The third line assigns a boolean value of True to the "round_continue" variable. This variable is used in the next WHILE loop to determine whether
    #--or not to loop again and continue the current round. At the beginning of each round, the "round_continue" variable must be explicitly assigned
    #--a value of True to ensure that the WHILE loop will loop at least once
    
    #--The fourth line takes a value equal to the current number of items in the "scoreboard" list, plus 1, and assigns it to the "round_count" list.
    #--The "len" function is used to obtain the number of items in the "scoreboard" list
    #--This is the way the the program keeps a track of how many rounds have been played, and what number the current round is.
    #--The logic behind this is that the number of items in the "scoreboard" list must always be 1 integer value less than the current round. This is 
    #--because an additional value is always added to the "scoreboard" list at the end of every round. For example, at the end of round 3, a third
    #--value is appended to the "scoreboard" list. The next round will be round 4, which is equal to the current number of items in "scoreboard", plus 1
    
    #--Finally, the fifth line declares a variable called "last_player" and assigns an integer value of 0 to it. This variable is used to keep track
    #--of which player was the last one to play a card onto the gameboard. As SNAP is a turn-based game, this variable is needed to allow the program
    #--to ensure that players play in turn. During the game, if player 1 plays a card onto the gameboard, then "last_player" will be assigned a value
    #--of 1 to indicate to the program that player 2 must play next. The initial value of 0 means that the round has only just begun, so neither player
    #--has played a card yet, and either will be able to play the first card.
    
    main_deck.shuffle()
    p1_deck, p2_deck = main_deck.deal()
    round_continue = True
    round_count = len(scoreboard)+1
    last_player = 0   
    
    #--This nested WHILE loop code block will execute on a loop for as long as the value assigned to the "round_continue" is True.
    #--This is used to ensure that the current round of SNAP continues until either: 
    #--a) a player has won the round by successfully calling snap and matching 2 cards.
    #--b) both players have played all 26 of their cards and neither of them called snap for the entire round.
    #--Either way, this nested WHILE loop will then break, the current round will end and the first WHILE loop will be tested again, to see if another
    #--round will be played
    while round_continue == True:
        
        #--Call the "system" method of the "os" module, in order to execute the windows command prompt command "cls". This command will clear the terminal
        #--before the round begins
        os.system('cls')
        
        printControls()#--At the beginning of every round, the game controls are printed at the top of the terminal, by calling the "printControls" function
        
        #--The next 3 lines print out a "header" for the round, which informs the players which round of the game they are currently playing
        #--In order to achieve this, the integer value currently assigned to "round_count" (which is the number of the current round) is converted
        #--to a string (using the str function), and passed to the format method of the string to be printed. This will insert the "round_count" value 
        #--into the placeholder braces within the string.
        #--The header string is underlined and followed by a blank line
        print("Round: {}".format(str(round_count)))
        print("==========")
        print("")
        
        #--The purpose of the next IF ELSE statement is to print out a graphical representation of the most recent CARD object to be 
        #--played to the gameboard. This is also referred to as the "top card". 
        #--First, the IF statement checks to see if there are any cards currently on the gameboard. If not, 
        #--then the round has just begun and no cards have been played, so there is no "top card" CARD object to print to the terminal.
        #--ELSE, if there are cards on the gameboard, then the "top card" CARD object needs to be printed to the terminal. 
        #--This is a key game mechanic, as players need to be able to see the sequence of CARD objects as they are played, and attempt to 
        #--call SNAP when they believe that the face value of the current "top card" CARD object matches the face value of the previous "top card"
        
        #--IF statement code block will execute if number of items in the "gameboard" list is equal to 0.
        #--The "len" function is used to obtain the number of items in the "gameboard" list.
        #--The "gameboard" list is used to store the CARD objects that have been played, during a round of SNAP.
        #--If there are 0 items in the "gameboard" list, it means that no cards have been played.
        if len(gameboard) == 0:
            
            #--IF no cards have yet been played onto the gameboard, then there are no CARD objects to print to the terminal.
            #--The program simply prints a "Top Card:" indicator string, with nothing after it, indicating to the players that
            #--the "top card" will be shown below this string.
            print("Top Card:")
        
        #--ELSE statement code block will execute if number of items in the "gameboard" list is more than 0.
        #--The "len" function is used to obtain the number of items in the "gameboard" list.
        #--If there are more that 0 items in the "gameboard" list, it means that at least 1 card has been played to the gameboard
        #--and the most recently played card must be printed to the terminal
        else:
            #--The "Top Card:" indicator string is printed, to tell the players that the card shown below this string
            #--is the most recent card to be played to the gameboard. A blank line is printed below that string.
            print("Top Card:")
            print("")
            
            #--A graphical representation of the "top card" CARD object is printed to the terminal.
            #--The most recent CARD object that has been played is obtained by referencing the -1 index of the gameboard list.
            #--The -1 index will always contain the very last item to be appended to the list, no matter how many items
            #--are in the list. Each time a player plays a card to the gameboard, a CARD object is removed from their player deck and
            #--appended to the "gameboard" list. Therefore the very last index in the "gameboard" list always contains the most recent CARD
            #--object to be played to the gameboard.
            #--The graphical representation of the CARD object is achieved by passing the CARD object into the "print" function. The string that
            #--is returned by the function to the terminal is defined by the "__str__" method of the "CARD" object.
            #--This string has been designed in a way that resembles a real life playing card. For a more detailled description of this
            #--functionality, see the "__str__" method of the CARD class.
            print(gameboard[-1])
        
        #--The next line of code is the primary method for recording an inputted key during the game. 
        #--During each round, each player has 2 possible keys they can press, their "Deal" key and their "Snap" key.
        #--The way this mechanic works is this:
        #--At the beginning of a round, the program will wait for user input, using the "input" function and outputting the string "Press a key, then press ENTER:"
        #--When a player presses a key, the value they entered goes through 2 transformations:
        #----1. The value is converting to a string, in order to be able to call the "upper" method on the string
        #----2. The value is converted to upper case, using the "upper" method, which is called on the string. This reason for converting to upper case
        #----is to reduce the number of values to test for in the match case statement below. The match case does not also have to check for lower case
        #----values.
        #--The inputted and converted value is then assigned to the variable name "key_pressed"
        key_pressed = str(input("Press a key, then press ENTER: ")).upper()
        
        
        #--This match case statement is used to progress the game based on the key that a player pressed during the game.
        #--Each player has 2 valid keys they can press, meaning there are only 4 valid values that will progress the game
        #--Also, as this is a turn-based game, a player will not be able to press they "Deal" key twice in a row.
        #--Either player can press they "Snap" key at any point in the game
        #--The conditional variable that is tested with this match case statement is "key_pressed", which currently contains the 
        #--value of the most recent key that a player entered during the game
        #--The match case statement will only ever evaluate 1 case condition at a time, as each of the case conditions are mutually exclusive
        match key_pressed:
            #--CASE 1: If the value assigned to "key_pressed" is "D". This means that player 1 has pressed their "Deal" key.
            case "D":
                #--IF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is the integer value 1. This means that the last player that played a card to the gameboard was player 1
                #--and since player 1 is attempting to play another card again, this turn is invalid. It is player 2's
                #--turn to play a card.
                if last_player == 1:
                    #--The if statement code block will print out 2 blank lines and an error message stating that it is player 2's
                    #--turn. No cards are played to the gameboard. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round
                    print("")
                    print("ERROR - Player 2 must play a card next")
                    print("")
                    input()
                #--ELIF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 1 (IF statement evaulated to false - meaning it is player 1's turn) AND if the number of items in
                #--the "p1_deck" list is not 0. The number of items in the "p1_deck" list is obtained using the "len" function and passing the "p1_deck"
                #--list as a parameter. If the number of items in "p1_deck" is 0, this means that player 1 has played all 26 of their allocated cards
                #--and there are no CARD objects left in the "p1_deck" list. Unless the other player has a card left, then the cards will need to be
                #--re-dealt from the main_deck and this round will begin again. And since this means there was no winner to this round, 
                #--the "round_count" variable will not be incremented. For a round to be over, there must be a winner
                elif len(p1_deck) == 0:
                    #--The elif statement code block will print out 2 blank lines and an error message stating that player 1 has no more cards, and
                    #--that this round will begin again. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will NOT loop again because the boolean value assigned
                    #--to the "round_continue" variable is set to "False". Instead, the main WHILE loop will loop again, all the CARD objects will
                    #--be returned to the "cards" list of the "main_deck" object. Then they will be shuffled and re-dealt. Then the current round
                    #--will begin again.
                    print("")
                    print("ERROR - Player 1 has no more cards. Cards will be re-dealt and the round will begin again")
                    print("")
                    input()
                    round_continue = False
                #--ELSE statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 1 (IF statement evaulated to false - meaning it is player 1's turn) AND if the number of items in
                #--the "p1_deck" list is MORE than 0 (meaning player 1 still has cards in their deck). This means that player 1 can play a card.
                else:
                    #--The else statement code block will remove the last CARD object from the end of the "p1_deck" list, using the "pop" method on the list, and then
                    #--pass that CARD object to the "append" method called by the "gameboard" list. This will append the last CARD object in the player's 
                    #--deck to the end of the gameboard list. This CARD object then becomes the "top card". This represents the player taking the top card from
                    #--their deck and placing it on top of card stack on the gameboard. Since player 1 successfully played a card, an integer value of 1
                    #--is assigned to the "last_player" variable, to indicate to the program that the last player to successfully play a card was player 1, 
                    #--so it should be player 2's turn next.
                    #--Once these 2 lines have executed, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round, printing
                    #--out the new "top card" to the terminal
                    gameboard.append(p1_deck.pop())
                    last_player = 1
            #--CASE 2: If the value assigned to "key_pressed" is "K". This means that player 2 has pressed their "Deal" key.
            case "K":
                #--IF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is the integer value 2. This means that the last player that played a card to the gameboard was player 2
                #--and since player 2 is attempting to play another card again, this turn is invalid. It is player 1's
                #--turn to play a card.
                if last_player == 2:
                    #--The if statement code block will print out 2 blank lines and an error message stating that it is player 1's
                    #--turn. No cards are played to the gameboard. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round
                    print("")
                    print("ERROR - Player 1 must play a card next")
                    print("")
                    input()
                #--ELIF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 2 (IF statement evaulated to false - meaning it is player 2's turn) AND if the number of items in
                #--the "p2_deck" list is not 0. The number of items in the "p2_deck" list is obtained using the "len" function and passing the "p2_deck"
                #--list as a parameter. If the number of items in "p2_deck" is 0, this means that player 2 has played all 26 of their allocated cards
                #--and there are no CARD objects left in the "p2_deck" list. Unless the other player has a card left, then the cards will need to be
                #--re-dealt from the main_deck and this round will begin again. And since this means there was no winner to this round, 
                #--the "round_count" variable will not be incremented. For a round to be over, there must be a winner
                elif len(p2_deck) == 0:
                    #--The elif statement code block will print out 2 blank lines and an error message stating that player 2 has no more cards, and
                    #--that this round will begin again. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will NOT loop again because the boolean value assigned
                    #--to the "round_continue" variable is set to "False". Instead, the main WHILE loop will loop again, all the CARD objects will
                    #--be returned to the "cards" list of the "main_deck" object. Then they will be shuffled and re-dealt. Then the current round
                    #--will begin again.
                    print("")
                    print("ERROR - Player 2 has no more cards. Cards will be re-dealt and the round will begin again")
                    print("")
                    input()
                    round_continue = False
                #--ELSE statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 2 (IF statement evaulated to false - meaning it is player 1's turn) AND if the number of items in
                #--the "p2_deck" list is MORE than 0 (meaning player 2 still has cards in their deck). This means that player 2 can play a card.
                else:
                    #--The else statement code block will remove the last CARD object from the end of the "p2_deck" list, using the "pop" method on the list, and then
                    #--pass that CARD object to the "append" method called by the "gameboard" list. This will append the last CARD object in the player's 
                    #--deck to the end of the gameboard list. This CARD object then becomes the "top card". This represents the player taking the top card from
                    #--their deck and placing it on top of card stack on the gameboard. Since player 2 successfully played a card, an integer value of 2
                    #--is assigned to the "last_player" variable, to indicate to the program that the last player to successfully play a card was player 2, 
                    #--so it should be player 1's turn next.
                    #--Once these 2 lines have executed, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round, printing
                    #--out the new "top card" to the terminal
                    gameboard.append(p2_deck.pop())
                    last_player = 2
            #--CASE 3: If the value assigned to "key_pressed" is "P". This means that player 2 has pressed their "Snap" key.
            case "P":
                #--If player 2 pressed their snap key, then they have attempted to call Snap! because they believe that the face value of the 
                #--current "top card" matches the face value of the previous "top card"
                #--In order to check if they have correctly called Snap!, the "check_snap" function is called, and an integer value of 2 is passed.
                #--This value will indicate to the function which player called snap! and, if they are correct, which player to allocate a point
                #--to on the scoreboard.
                #--The "check_snap" function will also return a boolean value which will be assigned to the "round_continue" variable.
                #--This is to indicate to the program whether to continue the current round or start a new one. If the "check_snap" function identifies
                #--that the player did NOT correctly call snap, then a value of True will be returned and the nested WHILE loop will loop again 
                #--and continue the current round. If the "check_snap" function identifies that the player DID correctly call snap, then a value of 
                #--False will be returned and the nested WHILE loop will NOT loop again. The main WHILE loop will loop again and a new round will begin.
                round_continue = check_snap(2)
                #The "input" command is used to pause the program until a player
                #--presses a key to continue. The pause is to allow the players to read the "congratulations - successful snap" message 
                #--before the program continues. (This message is printed by the "check_snap" function.
                #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                #--so the match case statement will end
                input()
            #--CASE 4: If the value assigned to "key_pressed" is "Q". This means that player 1 has pressed their "Snap" key.
            case "Q":
                #--If player 1 pressed their snap key, then they have attempted to call Snap! because they believe that the face value of the 
                #--current "top card" matches the face value of the previous "top card"
                #--In order to check if they have correctly called Snap!, the "check_snap" function is called, and an integer value of 1 is passed.
                #--This value will indicate to the function which player called snap! and, if they are correct, which player to allocate a point
                #--to on the scoreboard.
                #--The "check_snap" function will also return a boolean value which will be assigned to the "round_continue" variable.
                #--This is to indicate to the program whether to continue the current round or start a new one. If the "check_snap" function identifies
                #--that the player did NOT correctly call snap, then a value of True will be returned and the nested WHILE loop will loop again 
                #--and continue the current round. If the "check_snap" function identifies that the player DID correctly call snap, then a value of 
                #--False will be returned and the nested WHILE loop will NOT loop again. The main WHILE loop will loop again and a new round will begin.
                round_continue = check_snap(1)
                #The "input" command is used to pause the program until a player
                #--presses a key to continue. The pause is to allow the players to read the "congratulations - successful snap" message 
                #--before the program continues. (This message is printed by the "check_snap" function.
                #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                #--so the match case statement will end
                input()
            #--CASE 5 - default case: This case condition is the "default", meaning it will evaluate to True if
            #--none of the other case statement evaluated to true. If none of the other case statements evaluated to true, then a player 
            #--has inputted an invalid key. Only 4 keys are valid, namely D, K, Q and P.
            case default:
                #--The case statement code block will print out 2 blank lines and an error message stating that a player
                #--has inputted an invalid key. No cards are played to the gameboard. The "input" command is used to pause the program until a player
                #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round
                print("")
                print("ERROR - Invalid key pressed. Only 'D', 'K', 'Q' and 'P' are valid")
                print("")
                input()       
    
    #--The following 4 lines of code are executed at the end of every round, after the nested WHILE loop has been broken out of. There are only 2 
    #--reasons that the nested WHILE loop will be broken. Either a player has correctly called snap! and won a round, or both players have run out of
    #--cards and neither has successfully called snap! during the round. Either way, all of the CARD objects must be returned to the "main_deck", 
    #--then reshuffled, and re-dealt.
    #--The first 3 lines are for returning all CARD objects from the current round back to the "cards" list of the "main_deck" list object. This is done
    #--by calling the "returnCard" method for the "DECK" class, on the "main_deck" DECK object, and passing each list that may contain CARD objects, in turn.
    #--The 3 lists that may contain CARD objects are "gameboard", "p1_deck" and "p2_deck". The "returnCards" function then appends any CARD objects contained
    #--in the passed list object to the "cards" list of the DECK object that called the "returnCards" method, namely the "main_deck" object, in this instance
    #--Then, each time the "returnCards" method is called, it returns a blank list object, which is then assigned to the same list object that was passed
    #--to the function. This is in order to "empty" those lists, ready for the next round.
    #--Finally, the "printScoreboard" function is called, which will print a graphical representation of the current scoreboard to the terminal
    #--The scoreboard will be shown at the end of every round
    #--The main WHILE loop will then loop again, re-shuffle and re-deal the CARD objects from the "main_deck" object's list into the "p1_deck" and "p2_deck"
    #--lists, ready for another round to begin            
    gameboard = main_deck.returnCards(gameboard)
    p1_deck = main_deck.returnCards(p1_deck)
    p2_deck = main_deck.returnCards(p2_deck)  
    printScoreboard()  

#--The following 10 lines will execute after the main WHILE loop has been broken out of. If the main WHILE loop has been broken out of, then
#--the value of "round_count" currently equals integer 5. This means that 5 successful rounds of Snap! have been played, and it is time to declare
#--the overall winner and end the game.

#--The first 4 lines print out 3 blank lines and a "GAME OVER" message to the terminal
print("")
print("")
print("GAME OVER")
print("")

#--The next 3 line print out 2 divider lines and a congratulating message, informing the players who is the overall winner of the game.
#--In order to calculate and display the overall winner to the terminal, the "getWinner" function is called.
#--This function evaluates the "scoreboard" list and returns an integer value equal to the number of the player who is the overall winner
#--THen the integer value is converted to a string (using the str function), and passed to the format method of the string to be printed. 
#--This will insert the integer value into the placeholder braces within the string.
print("=====================================================================")
print("||After 5 rounds, the overall winner is Player {}! Congratulations!||".format(str(getWinner())))
print("=====================================================================")

#--Finally, 2 more blank lines are printed to the terminal, then the "input" command is used to pause the program until a player
#--presses a key to continue. The prompt string "Press ENTER to quit" is outputted to the terminal.
#--The pause is to allow the players to read the "congratulations" message before the program ends.
#--When a player presses a key, the program will end. 
print("")
print("")
=======

#================================================================================================================
#================================================SNAP card game==================================================
#================================================================================================================

#SNAP card game. This is a 2-player card game where a a deck of 52 cards is divided into 2 sets of 26, 1 set per player.
#When each player presses their "deal" key, the card on the top of their deck is played.
#If the current card's "face value" - i.e jack or king or 2 - matches the previous card face value, then the first player to press their "SNAP"
#--key wins the round and a score board is printed to the terminal. The cards are then re-allocated and another round begins.
#After 5 rounds, the overall winner is declared and a final score board is printed to the terminal.



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
#--called "ID". This class also has five methods, the initialise method, the __str__ method, the "getFVal" and "getID" methods. These will be
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
        #--Altogether, these seven rows produce ASCII art that resembles a real-life playing card.
        return """------------
|{:<5}{:>5}|
|          |
|{:^10}|
|          |
|{:<5}{:>5}|
------------""".format(self.fvalue, self.fvalue, self.suit, self.fvalue, self.fvalue)
    
 
    
    
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

#--Defined a function called "check_snap". The function accepts one parameter, which will be assigned to the "player_number" variable. 
#--The function will return a boolean value back to the line that called the function.
#--The purpose of this function is to check whether a player's SNAP! call is valid. 
#--After a card is played during a round, each player will have the opportunity to press their "SNAP" key if they believe the face value of
#--the current CARD object on the gameboard matches the face value of the previous CARD object (as in a game of SNAP). This function checks 
#--if the player is correct. If the 2 CARD object are a match, the function will return "False" (because the boolean value is passed back and 
#--assigned to the variable "round_continue". A value of False means the WHILE loop for the current round does not need to loop again, as a 
#--player has successfully matched 2 cards and the round is over.) If the 2 CARD objects are not a match, the function will return "True" 
#--and the round will continue.
#--The number of the player that called SNAP is passed to the function and assigned to the "player_number" variable.
def check_snap(player_number):
              
    #--IF statement code block will execute if the number of items in the "gameboard" list is less than 2 
    #--The number of items in the "gameboard" list is obtained using the "len" function
    #--(This means that there is either 1 or 0 CARD objects in the gameboard list, so there aren't enough CARD objects in the list to 
    #--compare for a match. At least 2 CARD objects are needed before a match can be checked)
    #--The purpose of this IF statement is to prevent an error occuring from trying to compare 2 objects from the gameboard
    #--list when there aren't enough objects in the list
    if len(gameboard) < 2:
        #--The IF statement code block prints out 2 blank lines, plus an error message stating that there aren't enough cards in play
        #--for a SNAP to occur. Finally, the block returns a "True" boolean value back to the line that called the function, meaning the
        #--WHILE loop for the current round will need to loop again, and the round will continue.
        print("")
        print("ERROR - There aren't enough cards in play to SNAP!")
        print("")
        return True
    
    #--ELSE statement code block will execute if the number of items in the "gameboard" list is more than or equal to 2 
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
            #--The number of the player that called SNAP was passed to the function and assigned to the variable "player_number". The value that was passed
            #--is an integer value, so before it is inserted into the placeholder braces, it is converted to a string value using the "str" function.
            #--After the 2 blank lines and the success message, the value that is currently held in the "player_number" variable (the number of the player who
            #--called SNAP) is appended to the "scoreboard" list. The purpose of this is to record the winner of the current round, so that after
            #--5 rounds, an overall winner can be declared, based on the mode value within the "scoreboard" list. For a full explanation of this, see the
            #--"printScoreboard" function below. 
            #--Finally, the block returns a "False" boolean value back to the line that called the function, meaning the
            #--WHILE loop for the current round will not need to loop again, and the current round will end.
            print("")
            print("SNAP! Player {} wins this round!".format(str(player_number)))
            print("")
            scoreboard.append(player_number)
            return False
        else:
            #--The ELSE statement code block prints out 2 blank lines, plus a failure message stating that player that called SNAP is incorrect 
            #--and is possibly trying to cheat. 
            #--Finally, the block returns a "True" boolean value back to the line that called the function, meaning the
            #--WHILE loop for the current round will need to loop again, and the round will continue.
            print("")
            print("NO SNAP! The cards do not match. No cheating!")
            print("")
            return True

#--Defined a function called "printInstructions". The function accepts no parameters, and returns to values. 
#--The purpose of this function is to print multiple strings to the terminal that make up the initial game instructions 
#--that will inform the user how to play the game.
#--The reason why I have chosen to put these print statements into a function, rather than simple in the main game code block
#--is purely for the sake of keeping my code tidy
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


#--Defined a function called "printControls". The function accepts no parameters, and returns to values. 
#--The purpose of this function is to print multiple strings to the terminal that make up the a reminder of the controls for the game
#--These lines will print out at the top of the terminal during every round
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


#--Defined a function called "printScoreboard". The function accepts no parameters, and returns to values. 
#--The purpose of this function is to clear the terminal, then print multiple strings to the terminal that make up the a 
#--visual representation of the current scoreboard.
#--The terminal will be cleared and the scoreboard will be printed out at the end of every round of the game
def printScoreboard():
    
    #--Call the "system" method of the "os" module, in order to execute the windows command prompt command "cls". This command will clear the terminal
    #--before the scoreboard is printed.
    os.system("cls")
    
    #--The next 8 lines will print out blank spaces, a header and the beginning of the scoreboard table
    print("")
    print("==SCOREBOARD==")
    print("--------------")
    print("")
    print("")
    print("---------------------")
    print("| Player    | Score |")
    print("|-----------|-------|")
    
    #--The next two lines print out the strings that make up the main content for the scoreboard, namely the current scores for each player.
    #--The current scores for each player are inserted into the placeholder braces in the string in the following way:
    #--1. The current score for the player is obtained by calling the "count" method on the "scoreboard" list, in order to query to number of occurences
    #----of each player's number in the list. For example, if player 2 has won 3 rounds at this point, then the integer value "2" will occur in the 
    #----in the "scoreboard" list 3 times. This integer value is then passed as a parameter to the "format" method for the string to print.
    #--2. The "format" method of the string is called and passed the parameter from step 1. The formatting type :^7 is used between the placeholder
    #----braces in the string to print. This means that the integer value representing the player's score will be centrally aligned within a 7
    #----character space. This formatting type is used to ensure that the visual representation of the scoreboard that is printer to the terminal
    #----will look correct, no matter the size of the integer that is passed to the format method.
    print("| Player 1  |{:^7}|".format(scoreboard.count(1)))
    print("| Player 2  |{:^7}|".format(scoreboard.count(2)))
    
    #--The next 3 lines will print out the bottom edge of the scoreboard, plus two blank lines
    print("---------------------")
    print("")
    print("")
    
    #--The program prompts the user to press ENTER to continue, using the input function. Using "input" means that the program is paused until the user 
    #--enters a key.
    #--This is to allow the player's to look at the scoreboard before moving on to the next round or ending the game
    input("Press ENTER to continue")


#--Defined a function called "getWinner". The function accepts no parameters. The function will return an integer value that represents
#--the overall winner of the game. 
#--The purpose of this function is to check which player is the overall winner at the end of 5 rounds of the game  
def getWinner():
    
    #--IF statement code block will execute if number of occurences of the integer value 1 is more than the number of occurences of the integer
    #--value 2, in the "scoreboard" list variable. This would mean that player 1 has won more rounds than player 2 and is the overall winner of
    #--the game. The "count" method is called on the "scoreboard" list to query the number of occurences of the passed integer values. An integer
    #--value of 1 is passed to the "count" method to query how many occurences of 1 there are (representing the number of rounds player 1 has won), 
    #--and then the same is done for the integer value 2.
    if scoreboard.count(1) > scoreboard.count(2):
        #--If the above IF statement evaluates to True (meaning the overall winner of the game is player 1), then an integer value of 1 is
        #--passed by to the line that called the function
        return 1
    
    #--ELSE statement code block will execute the logical opposite of the above IF statement is True, i.e if number of occurences of the integer 
    #--value 2 is more than the number of occurences of the integer value 1, in the "scoreboard" list variable. 
    #--This would mean that player 2 has won more rounds than player 1 and is the overall winner of the game. 
    else:
        #--If the above ELSE statement evaluates to True (meaning the overall winner of the game is player 2), then an integer value of 2 is
        #--passed by to the line that called the function
        return 2

#=====================================================================================================================================================================

#=============================MAIN PROGRAM START POINT====================================
 
#--Invocation of "populateDeck" method, on the "main_deck" DECK object, using dot notation
#--This method will create 52 objects of the CARD class and append each one to the "cards" instance variable
#--of the "main_deck" object.    
main_deck.populateDeck()

printInstructions()#--The "printInstructions" method is called, in order to print the game instructions to the terminal

#--2 blank lines are printed. In between those lines, the program prompts the user to press ANY KEY TO BEING, using the input function. 
#--Using "input" means that the program is paused until the user enters a key.
# #--This is to allow the player's to look at the game instructions before beginning the game
print("")
input("PRESS ANY KEY TO BEGIN")
print("")

#--Declare a variable called "round_count".
#--This variable will be used as an accumulator to keep track of how many rounds of SNAP have been played
#--during this game
round_count = 0


#--This WHILE loop code block will execute on a loop for as long as the value assigned to the "round_count" is less than 5.
#--This is because the game will only allow 5 rounds of SNAP to be played before the overall winner is declared and the game is over
#--The program will continue as long as the WHILE loop condition is True. Else the loop will be broken and the program will end
while (round_count < 5):
    
    #---The next 5 lines are executed at the beginning of every round. First, the "shuffle" method is invoked on the "main_deck" DECK object, 
    #--using dot notation. This method will perform 52 random swaps of the CARD objects within the "cards" list of the "main_deck" object. This 
    #--randomization represents the shuffling of the deck of cards before a round of SNAP.
    
    #--The next line invokes the "deal" method on the "main_deck" object. This method will divide the 52 CARD objects into 2 sets of 26 CARD objects
    #--and append each of those sets to 2 new lists. Those list are then returned from the method and assigned to the lists "p1_deck" and "p2_deck" respectively.
    #--This represents the dealing of all the cards from a deck to the 2 players before each round of SNAP. The "p2_deck" and "p2_deck" lists represent
    #--the set of 26 cards that each player has at the beginning of a round of SNAP.
   
    #--The third line assigns a boolean value of True to the "round_continue" variable. This variable is used in the next WHILE loop to determine whether
    #--or not to loop again and continue the current round. At the beginning of each round, the "round_continue" variable must be explicitly assigned
    #--a value of True to ensure that the WHILE loop will loop at least once
    
    #--The fourth line takes a value equal to the current number of items in the "scoreboard" list, plus 1, and assigns it to the "round_count" list.
    #--The "len" function is used to obtain the number of items in the "scoreboard" list
    #--This is the way the the program keeps a track of how many rounds have been played, and what number the current round is.
    #--The logic behind this is that the number of items in the "scoreboard" list must always be 1 integer value less than the current round. This is 
    #--because an additional value is always added to the "scoreboard" list at the end of every round. For example, at the end of round 3, a third
    #--value is appended to the "scoreboard" list. The next round will be round 4, which is equal to the current number of items in "scoreboard", plus 1
    
    #--Finally, the fifth line declares a variable called "last_player" and assigns an integer value of 0 to it. This variable is used to keep track
    #--of which player was the last one to play a card onto the gameboard. As SNAP is a turn-based game, this variable is needed to allow the program
    #--to ensure that players play in turn. During the game, if player 1 plays a card onto the gameboard, then "last_player" will be assigned a value
    #--of 1 to indicate to the program that player 2 must play next. The initial value of 0 means that the round has only just begun, so neither player
    #--has played a card yet, and either will be able to play the first card.
    
    main_deck.shuffle()
    p1_deck, p2_deck = main_deck.deal()
    round_continue = True
    round_count = len(scoreboard)+1
    last_player = 0   
    
    #--This nested WHILE loop code block will execute on a loop for as long as the value assigned to the "round_continue" is True.
    #--This is used to ensure that the current round of SNAP continues until either: 
    #--a) a player has won the round by successfully calling snap and matching 2 cards.
    #--b) both players have played all 26 of their cards and neither of them called snap for the entire round.
    #--Either way, this nested WHILE loop will then break, the current round will end and the first WHILE loop will be tested again, to see if another
    #--round will be played
    while round_continue == True:
        
        #--Call the "system" method of the "os" module, in order to execute the windows command prompt command "cls". This command will clear the terminal
        #--before the round begins
        os.system('cls')
        
        printControls()#--At the beginning of every round, the game controls are printed at the top of the terminal, by calling the "printControls" function
        
        #--The next 3 lines print out a "header" for the round, which informs the players which round of the game they are currently playing
        #--In order to achieve this, the integer value currently assigned to "round_count" (which is the number of the current round) is converted
        #--to a string (using the str function), and passed to the format method of the string to be printed. This will insert the "round_count" value 
        #--into the placeholder braces within the string.
        #--The header string is underlined and followed by a blank line
        print("Round: {}".format(str(round_count)))
        print("==========")
        print("")
        
        #--The purpose of the next IF ELSE statement is to print out a graphical representation of the most recent CARD object to be 
        #--played to the gameboard. This is also referred to as the "top card". 
        #--First, the IF statement checks to see if there are any cards currently on the gameboard. If not, 
        #--then the round has just begun and no cards have been played, so there is no "top card" CARD object to print to the terminal.
        #--ELSE, if there are cards on the gameboard, then the "top card" CARD object needs to be printed to the terminal. 
        #--This is a key game mechanic, as players need to be able to see the sequence of CARD objects as they are played, and attempt to 
        #--call SNAP when they believe that the face value of the current "top card" CARD object matches the face value of the previous "top card"
        
        #--IF statement code block will execute if number of items in the "gameboard" list is equal to 0.
        #--The "len" function is used to obtain the number of items in the "gameboard" list.
        #--The "gameboard" list is used to store the CARD objects that have been played, during a round of SNAP.
        #--If there are 0 items in the "gameboard" list, it means that no cards have been played.
        if len(gameboard) == 0:
            
            #--IF no cards have yet been played onto the gameboard, then there are no CARD objects to print to the terminal.
            #--The program simply prints a "Top Card:" indicator string, with nothing after it, indicating to the players that
            #--the "top card" will be shown below this string.
            print("Top Card:")
        
        #--ELSE statement code block will execute if number of items in the "gameboard" list is more than 0.
        #--The "len" function is used to obtain the number of items in the "gameboard" list.
        #--If there are more that 0 items in the "gameboard" list, it means that at least 1 card has been played to the gameboard
        #--and the most recently played card must be printed to the terminal
        else:
            #--The "Top Card:" indicator string is printed, to tell the players that the card shown below this string
            #--is the most recent card to be played to the gameboard. A blank line is printed below that string.
            print("Top Card:")
            print("")
            
            #--A graphical representation of the "top card" CARD object is printed to the terminal.
            #--The most recent CARD object that has been played is obtained by referencing the -1 index of the gameboard list.
            #--The -1 index will always contain the very last item to be appended to the list, no matter how many items
            #--are in the list. Each time a player plays a card to the gameboard, a CARD object is removed from their player deck and
            #--appended to the "gameboard" list. Therefore the very last index in the "gameboard" list always contains the most recent CARD
            #--object to be played to the gameboard.
            #--The graphical representation of the CARD object is achieved by passing the CARD object into the "print" function. The string that
            #--is returned by the function to the terminal is defined by the "__str__" method of the "CARD" object.
            #--This string has been designed in a way that resembles a real life playing card. For a more detailled description of this
            #--functionality, see the "__str__" method of the CARD class.
            print(gameboard[-1])
        
        #--The next line of code is the primary method for recording an inputted key during the game. 
        #--During each round, each player has 2 possible keys they can press, their "Deal" key and their "Snap" key.
        #--The way this mechanic works is this:
        #--At the beginning of a round, the program will wait for user input, using the "input" function and outputting the string "Press a key, then press ENTER:"
        #--When a player presses a key, the value they entered goes through 2 transformations:
        #----1. The value is converting to a string, in order to be able to call the "upper" method on the string
        #----2. The value is converted to upper case, using the "upper" method, which is called on the string. This reason for converting to upper case
        #----is to reduce the number of values to test for in the match case statement below. The match case does not also have to check for lower case
        #----values.
        #--The inputted and converted value is then assigned to the variable name "key_pressed"
        key_pressed = str(input("Press a key, then press ENTER: ")).upper()
        
        
        #--This match case statement is used to progress the game based on the key that a player pressed during the game.
        #--Each player has 2 valid keys they can press, meaning there are only 4 valid values that will progress the game
        #--Also, as this is a turn-based game, a player will not be able to press they "Deal" key twice in a row.
        #--Either player can press they "Snap" key at any point in the game
        #--The conditional variable that is tested with this match case statement is "key_pressed", which currently contains the 
        #--value of the most recent key that a player entered during the game
        #--The match case statement will only ever evaluate 1 case condition at a time, as each of the case conditions are mutually exclusive
        match key_pressed:
            #--CASE 1: If the value assigned to "key_pressed" is "D". This means that player 1 has pressed their "Deal" key.
            case "D":
                #--IF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is the integer value 1. This means that the last player that played a card to the gameboard was player 1
                #--and since player 1 is attempting to play another card again, this turn is invalid. It is player 2's
                #--turn to play a card.
                if last_player == 1:
                    #--The if statement code block will print out 2 blank lines and an error message stating that it is player 2's
                    #--turn. No cards are played to the gameboard. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round
                    print("")
                    print("ERROR - Player 2 must play a card next")
                    print("")
                    input()
                #--ELIF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 1 (IF statement evaulated to false - meaning it is player 1's turn) AND if the number of items in
                #--the "p1_deck" list is not 0. The number of items in the "p1_deck" list is obtained using the "len" function and passing the "p1_deck"
                #--list as a parameter. If the number of items in "p1_deck" is 0, this means that player 1 has played all 26 of their allocated cards
                #--and there are no CARD objects left in the "p1_deck" list. Unless the other player has a card left, then the cards will need to be
                #--re-dealt from the main_deck and this round will begin again. And since this means there was no winner to this round, 
                #--the "round_count" variable will not be incremented. For a round to be over, there must be a winner
                elif len(p1_deck) == 0:
                    #--The elif statement code block will print out 2 blank lines and an error message stating that player 1 has no more cards, and
                    #--that this round will begin again. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will NOT loop again because the boolean value assigned
                    #--to the "round_continue" variable is set to "False". Instead, the main WHILE loop will loop again, all the CARD objects will
                    #--be returned to the "cards" list of the "main_deck" object. Then they will be shuffled and re-dealt. Then the current round
                    #--will begin again.
                    print("")
                    print("ERROR - Player 1 has no more cards. Cards will be re-dealt and the round will begin again")
                    print("")
                    input()
                    round_continue = False
                #--ELSE statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 1 (IF statement evaulated to false - meaning it is player 1's turn) AND if the number of items in
                #--the "p1_deck" list is MORE than 0 (meaning player 1 still has cards in their deck). This means that player 1 can play a card.
                else:
                    #--The else statement code block will remove the last CARD object from the end of the "p1_deck" list, using the "pop" method on the list, and then
                    #--pass that CARD object to the "append" method called by the "gameboard" list. This will append the last CARD object in the player's 
                    #--deck to the end of the gameboard list. This CARD object then becomes the "top card". This represents the player taking the top card from
                    #--their deck and placing it on top of card stack on the gameboard. Since player 1 successfully played a card, an integer value of 1
                    #--is assigned to the "last_player" variable, to indicate to the program that the last player to successfully play a card was player 1, 
                    #--so it should be player 2's turn next.
                    #--Once these 2 lines have executed, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round, printing
                    #--out the new "top card" to the terminal
                    gameboard.append(p1_deck.pop())
                    last_player = 1
            #--CASE 2: If the value assigned to "key_pressed" is "K". This means that player 2 has pressed their "Deal" key.
            case "K":
                #--IF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is the integer value 2. This means that the last player that played a card to the gameboard was player 2
                #--and since player 2 is attempting to play another card again, this turn is invalid. It is player 1's
                #--turn to play a card.
                if last_player == 2:
                    #--The if statement code block will print out 2 blank lines and an error message stating that it is player 1's
                    #--turn. No cards are played to the gameboard. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round
                    print("")
                    print("ERROR - Player 1 must play a card next")
                    print("")
                    input()
                #--ELIF statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 2 (IF statement evaulated to false - meaning it is player 2's turn) AND if the number of items in
                #--the "p2_deck" list is not 0. The number of items in the "p2_deck" list is obtained using the "len" function and passing the "p2_deck"
                #--list as a parameter. If the number of items in "p2_deck" is 0, this means that player 2 has played all 26 of their allocated cards
                #--and there are no CARD objects left in the "p2_deck" list. Unless the other player has a card left, then the cards will need to be
                #--re-dealt from the main_deck and this round will begin again. And since this means there was no winner to this round, 
                #--the "round_count" variable will not be incremented. For a round to be over, there must be a winner
                elif len(p2_deck) == 0:
                    #--The elif statement code block will print out 2 blank lines and an error message stating that player 2 has no more cards, and
                    #--that this round will begin again. The "input" command is used to pause the program until a player
                    #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                    #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will NOT loop again because the boolean value assigned
                    #--to the "round_continue" variable is set to "False". Instead, the main WHILE loop will loop again, all the CARD objects will
                    #--be returned to the "cards" list of the "main_deck" object. Then they will be shuffled and re-dealt. Then the current round
                    #--will begin again.
                    print("")
                    print("ERROR - Player 2 has no more cards. Cards will be re-dealt and the round will begin again")
                    print("")
                    input()
                    round_continue = False
                #--ELSE statement code block will execute if the value currently assigned to the variable "last_player"
                #--is not integer value 2 (IF statement evaulated to false - meaning it is player 1's turn) AND if the number of items in
                #--the "p2_deck" list is MORE than 0 (meaning player 2 still has cards in their deck). This means that player 2 can play a card.
                else:
                    #--The else statement code block will remove the last CARD object from the end of the "p2_deck" list, using the "pop" method on the list, and then
                    #--pass that CARD object to the "append" method called by the "gameboard" list. This will append the last CARD object in the player's 
                    #--deck to the end of the gameboard list. This CARD object then becomes the "top card". This represents the player taking the top card from
                    #--their deck and placing it on top of card stack on the gameboard. Since player 2 successfully played a card, an integer value of 2
                    #--is assigned to the "last_player" variable, to indicate to the program that the last player to successfully play a card was player 2, 
                    #--so it should be player 1's turn next.
                    #--Once these 2 lines have executed, the game will continue. None of the other case conditions will evaluate to True 
                    #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round, printing
                    #--out the new "top card" to the terminal
                    gameboard.append(p2_deck.pop())
                    last_player = 2
            #--CASE 3: If the value assigned to "key_pressed" is "P". This means that player 2 has pressed their "Snap" key.
            case "P":
                #--If player 2 pressed their snap key, then they have attempted to call Snap! because they believe that the face value of the 
                #--current "top card" matches the face value of the previous "top card"
                #--In order to check if they have correctly called Snap!, the "check_snap" function is called, and an integer value of 2 is passed.
                #--This value will indicate to the function which player called snap! and, if they are correct, which player to allocate a point
                #--to on the scoreboard.
                #--The "check_snap" function will also return a boolean value which will be assigned to the "round_continue" variable.
                #--This is to indicate to the program whether to continue the current round or start a new one. If the "check_snap" function identifies
                #--that the player did NOT correctly call snap, then a value of True will be returned and the nested WHILE loop will loop again 
                #--and continue the current round. If the "check_snap" function identifies that the player DID correctly call snap, then a value of 
                #--False will be returned and the nested WHILE loop will NOT loop again. The main WHILE loop will loop again and a new round will begin.
                round_continue = check_snap(2)
                #The "input" command is used to pause the program until a player
                #--presses a key to continue. The pause is to allow the players to read the "congratulations - successful snap" message 
                #--before the program continues. (This message is printed by the "check_snap" function.
                #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                #--so the match case statement will end
                input()
            #--CASE 4: If the value assigned to "key_pressed" is "Q". This means that player 1 has pressed their "Snap" key.
            case "Q":
                #--If player 1 pressed their snap key, then they have attempted to call Snap! because they believe that the face value of the 
                #--current "top card" matches the face value of the previous "top card"
                #--In order to check if they have correctly called Snap!, the "check_snap" function is called, and an integer value of 1 is passed.
                #--This value will indicate to the function which player called snap! and, if they are correct, which player to allocate a point
                #--to on the scoreboard.
                #--The "check_snap" function will also return a boolean value which will be assigned to the "round_continue" variable.
                #--This is to indicate to the program whether to continue the current round or start a new one. If the "check_snap" function identifies
                #--that the player did NOT correctly call snap, then a value of True will be returned and the nested WHILE loop will loop again 
                #--and continue the current round. If the "check_snap" function identifies that the player DID correctly call snap, then a value of 
                #--False will be returned and the nested WHILE loop will NOT loop again. The main WHILE loop will loop again and a new round will begin.
                round_continue = check_snap(1)
                #The "input" command is used to pause the program until a player
                #--presses a key to continue. The pause is to allow the players to read the "congratulations - successful snap" message 
                #--before the program continues. (This message is printed by the "check_snap" function.
                #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                #--so the match case statement will end
                input()
            #--CASE 5 - default case: This case condition is the "default", meaning it will evaluate to True if
            #--none of the other case statement evaluated to true. If none of the other case statements evaluated to true, then a player 
            #--has inputted an invalid key. Only 4 keys are valid, namely D, K, Q and P.
            case default:
                #--The case statement code block will print out 2 blank lines and an error message stating that a player
                #--has inputted an invalid key. No cards are played to the gameboard. The "input" command is used to pause the program until a player
                #--presses a key to continue. The pause is to allow the players to read the error message before the program continues.
                #--When a player presses a key, the game will continue. None of the other case conditions will evaluate to True 
                #--so the match case statement will end and the nested WHILE loop will loop again and continue the current round
                print("")
                print("ERROR - Invalid key pressed. Only 'D', 'K', 'Q' and 'P' are valid")
                print("")
                input()       
    
    #--The following 4 lines of code are executed at the end of every round, after the nested WHILE loop has been broken out of. There are only 2 
    #--reasons that the nested WHILE loop will be broken. Either a player has correctly called snap! and won a round, or both players have run out of
    #--cards and neither has successfully called snap! during the round. Either way, all of the CARD objects must be returned to the "main_deck", 
    #--then reshuffled, and re-dealt.
    #--The first 3 lines are for returning all CARD objects from the current round back to the "cards" list of the "main_deck" list object. This is done
    #--by calling the "returnCard" method for the "DECK" class, on the "main_deck" DECK object, and passing each list that may contain CARD objects, in turn.
    #--The 3 lists that may contain CARD objects are "gameboard", "p1_deck" and "p2_deck". The "returnCards" function then appends any CARD objects contained
    #--in the passed list object to the "cards" list of the DECK object that called the "returnCards" method, namely the "main_deck" object, in this instance
    #--Then, each time the "returnCards" method is called, it returns a blank list object, which is then assigned to the same list object that was passed
    #--to the function. This is in order to "empty" those lists, ready for the next round.
    #--Finally, the "printScoreboard" function is called, which will print a graphical representation of the current scoreboard to the terminal
    #--The scoreboard will be shown at the end of every round
    #--The main WHILE loop will then loop again, re-shuffle and re-deal the CARD objects from the "main_deck" object's list into the "p1_deck" and "p2_deck"
    #--lists, ready for another round to begin            
    gameboard = main_deck.returnCards(gameboard)
    p1_deck = main_deck.returnCards(p1_deck)
    p2_deck = main_deck.returnCards(p2_deck)  
    printScoreboard()  

#--The following 10 lines will execute after the main WHILE loop has been broken out of. If the main WHILE loop has been broken out of, then
#--the value of "round_count" currently equals integer 5. This means that 5 successful rounds of Snap! have been played, and it is time to declare
#--the overall winner and end the game.

#--The first 4 lines print out 3 blank lines and a "GAME OVER" message to the terminal
print("")
print("")
print("GAME OVER")
print("")

#--The next 3 line print out 2 divider lines and a congratulating message, informing the players who is the overall winner of the game.
#--In order to calculate and display the overall winner to the terminal, the "getWinner" function is called.
#--This function evaluates the "scoreboard" list and returns an integer value equal to the number of the player who is the overall winner
#--THen the integer value is converted to a string (using the str function), and passed to the format method of the string to be printed. 
#--This will insert the integer value into the placeholder braces within the string.
print("=====================================================================")
print("||After 5 rounds, the overall winner is Player {}! Congratulations!||".format(str(getWinner())))
print("=====================================================================")

#--Finally, 2 more blank lines are printed to the terminal, then the "input" command is used to pause the program until a player
#--presses a key to continue. The prompt string "Press ENTER to quit" is outputted to the terminal.
#--The pause is to allow the players to read the "congratulations" message before the program ends.
#--When a player presses a key, the program will end. 
print("")
print("")
>>>>>>> Stashed changes
input("Press ENTER to quit")    
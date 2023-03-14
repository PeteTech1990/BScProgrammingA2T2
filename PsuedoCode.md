#program start

#CLASS deck (3 objects of this class will be needed)
    list cards

#CLASS card (52 CARD objects will exist in the game)
    string "SUIT"
    string "VALUE"
    int ID
    #FUNCTION setsuit(string):
        SUIT = string
    #FUNCTION setval(string):
        VAL = string

#CLASS gameboard
    LIST (card) p1_space
    LIST (card) p2_space

#LIST suits = ["♠", "♥", "♣", "♦"]
#LIST values = ["J", "Q", "K", "A"]

#MAINDECK object and all initial cards will be hard coded
main_deck = deck

#P1Deck object to hold player 1's deck
p1_deck = deck

#P2Deck object to hold player 2's deck
p2_deck = deck

#MAINBOARD object to act as game board
main_board = gameboard

LIST scoreboard = []

#POPULATEDECK function (ROUND_COUNT)
    if (ROUND_COUNT == 0):
        int ID = 1
        FOR SUIT in suits (FOR EACH OF THE SUITS):
            FOR count in range(13) (FOR EACH OF THE VALUES):
                current_card = card
                current_card.setsuit(SUIT)
                if count < 10:
                    current_card.setval(count)
                else:
                    current_card.setval(values[count-9])
                
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

bool ROUND_COUNT = 0

MAIN PROGRAM START

while ROUND_COUNT < 6

    POPULATEDECK(ROUND_COUNT)

    SHUFFLEDECK

    DEAL

    INPUT("PRESS ANY KEY TO BEGIN)

    bool ROUND_CONTINUE == True

    while ROUND_CONTINUE == TRUE
        
        if main_board.p1_space.empty() == TRUE:
            PRINT: Player 1 card:
        else:
            PRINT: Player 1 card: {}{}.format(main_board.p1_space[-1].SUIT, main_board.p1_space[-1].VALUE)
        if main_board.p2_space.empty() == TRUE:
            PRINT: Player 2 card:
        else:
            PRINT: Player 2 card: {}{}.format(main_board.p2_space[-1].SUIT, main_board.p2_space[-1].VALUE)

        INPUT(KEYPRESS)

        match KEYPRESS:
            case D:
                if len(p1_deck.cards) > len(p2_deck.cards):
                    ERROR - Player 2 must play a card next
                else:
                    main_board.p1_space.append(p1_deck.cards.pop())
            case K:
                main_board.p2_space.append(p2_deck.cards.pop())
            case Q:
                if p1_space.empty() == TRUE:
                    ERROR
                elif p2_space.empty() == TRUE:
                    ERROR
                elif main_board.p1_space[-1].VALUE == main_board.p2_space[-1].VALUE:
                    SNAP
                    scoreboard.append(1)
                    ROUND_CONTINUE = FALSE
                    ROUND_COUNT += 1
                else:
                    NO SNAP
            case P:
                if p1_space.empty() == TRUE:
                    ERROR
                elif p2_space.empty() == TRUE:
                    ERROR
                elif main_board.p2_space[-1].VALUE == main_board.p1_space[-1].VALUE:
                    SNAP
                    scoreboard.append(2)
                    ROUND_CONTINUE = FALSE
                    ROUND_COUNT += 1
                else:
                    NO SNAP

            PRINT: Player 1 card:
            PRINT: Player 2 card:

player1score = scoreboard.count(1)
player2score = scoreboard.count(2)

PRINT("GAME OVER")
PRINT Player 1 won + player1score + rounds
PRINT Player 2 won + player2score + rounds

match >:
    Case player1score:
        PRINT congratulations player 1, you are the winner
    case: player2score:
        PRINT congratulations player 2, you are the winner
#program start
##Potential addition - CALL function to start new ticket

variable items_so_far (list)
variable discountpercentage (float)
variable discountamount (float)
variable total_cost (float)
variable ticketnumber = 1 (integer)

while loop = true... continue/repeat the programme
    print welcome message
    print menu
    wait for user input (select a menu item)
        if user input = <1 - 3>
            print tickettypes/daytypes (if applicable)
            itemname = wait for user input (select tickettype/daytype)
            print costperticket
            amount = wait for user input (select number of people/children/family/day)
            Add item type, number of items and total to "items_so_far" list TUPLE(itemname, amount, number of people/children/families/days * costperticket)
            ##Potential addition - CALL "Ticket" class Method to ADD total to items_so_far attribute (PASS (number of people/children/families/days * costperticket))
        elif user input = <4 - 5>
            print beveragetype/foodtype
            itemname = wait for user input (select beveragetype/foodtype)
            print costperfood/drink
            amount = wait for user input (enter number of items required)
            Add item type, number of items and total to "items_so_far" list TUPLE(itemname, amount, foodtype/drinktype * costperticket)
            ##Potential addition - CALL "Ticket" class Method to ADD total to items_so_far attribute (PASS (foodtype/drinktype * costperticket))
        elif user input = 6
            print discountoptions
            wait for user input (select discount type)
            Assign discount amount to variable "discountpercentage"
        elif user input = 7
            wait for user input (are you sure you want to print your ticket?)
            CALL function to calculate total price
            CALL function to PRINT TICKET to screen
            ticketnumber += 1
            loop = wait for user input (do you want to print another ticket?)
            ##Potential addition - CALL function to start new ticket
        elif user input = 9
            loop = wait for user input (are you sure you want to quit?)
            loop = false
clear screen
Loop back to menu if loop remains true

 
function for calculating ticket total
    running_total = 0
    for each item in items_so_far
        running_total = running_total + item[2]
    discountamount = (1 - discountpercentage/100)
    total_cost = discountamount * running_total

function for printing ticket
    print "Ticket number {ddmmyy}{####}".format(datetime.now(), ticket_serial)
    for each item in items_so_far
        print "Item 1: {} x {} - Total: {£0.00}".format(item[0], item[1], item[2])
    print "{} discount added: {}".format(discountpercentage, discountamount)
    print "Total cost: {£0.00}".format(total_cost)

#------Potential to add "Ticket" class later--------
class Ticket
    variable items_so_far (list)
    variable total
    
    function for calculating ticket total
        for each item in items_so_far
            total = total + item
        discounted_Total = total / discount
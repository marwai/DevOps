TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100


# Creat the calculate_price Main. It takes number of tickets and returns
# num_tickets * TICKET_PRICE

def calculate_price(number_of_tickets):
    # create a new constant for a £2 service charge
    # add the service charge to result
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining:
    print("There are {} tickets remaining".format(tickets_remaining))

    name = input("What is your name? ")
    num_tickets = input("Okay, {} how many tickets would you like?  ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        # Include the error text in the output
        print("Oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("Total due is ${}".format(amount_due))
        confirm_price = input("Do you want to proceed?  Y/N  ")
        if "y" in confirm_price.lower():
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
print("Sorry the tickets are all sold out! ")
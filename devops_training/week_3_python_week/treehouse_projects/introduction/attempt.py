TICKET_PRICE = 10
tickets_remaining = 100
SERVICE_CHARGE = 2


def calculate_price(number_of_tickets):
    return (TICKET_PRICE * tickets_remaining) + SERVICE_CHARGE


while tickets_remaining:
    print("You have {} tickets remaining. ".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("Hello {}, how many tickets do you want? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
    else:

        total_tickets = calculate_price(num_tickets)
        print("Total amount is £{}".format(total_tickets))
        confirm_price = input("Do you want to proceed?  Y/N ")
        if confirm_price.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
print("Sorry the tickets are all sold out! ")


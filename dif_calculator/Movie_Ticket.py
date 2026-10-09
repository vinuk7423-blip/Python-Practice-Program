total_tickets = 0
total_amount = 0
number_of_people = int(input("Enter number of people:"))
for person in range(number_of_people):
    print("\nPerson",person + 1)
    age = int(input("Enter age:"))
    if age < 5:
        ticket_price = 0
        category = "Free"
    elif age <= 12:
        ticket_price = 120
        category = "Child"
    elif age <= 59:
        ticket_price = 200
        category = "Adult"
    else:
        ticket_price = 100
        category = "Senior Citizen"
    total_tickets = total_tickets + 1
    total_amount = total_amount + ticket_price
    print("Category:",category)
    print("Ticket Price:",ticket_price)
    print("\n -----BOOKIN SUMMERY -----")
    print("Total Tickets:",total_tickets)
    print("Total Amount:",total_amount)
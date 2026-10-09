total = 0
while True:
    print("\n----- MENU -----")
    print("1. Pizza - ₹250")
    print("2.  burger - ₹150")
    print("3. Pasta - ₹200")
    print("4. Coffee - ₹80")
    print("5. Finish Order")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        quantity = int(input("Enter quantity:"))
        price = 250
        total = total + (price * quantity)
    elif choice == 2:
        quantity = int(input("Enter quantity:"))
        price = 150
        total = total + (price * quantity)
    elif choice == 3:
        quantity = int(input("Enter quantity:"))
        price = 200
        total = total + (price * quantity)
    elif choice == 4:
        quantity = int(input("Enter quantity:"))
        price = 80
        total = total + (price * quantity)
    elif choice == 5:
        break
    else:
        print("invalid choice.")
gst = total * 0.05
final_amount = total + gst
print("\n----- FINAL BILL -----")
print("Food Total:",total)
print("GST:",gst)
print("Final Amount:",final_amount)
balance = 5000
transactions = []
while True:
    print("\n===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transactions")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current Balance:", balance)
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            transactions.append("Deposited ₹" + str(amount))
            print("Deposit successful.")
        else:
            print("Invalid amount.")
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            transactions.append("Withdrawn ₹" + str(amount))
            print("Withdrawal successful.")
        else:
            print("Invalid amount or insufficient balance.")
    elif choice == 4:
        print("\n----- TRANSACTIONS -----")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)
    elif choice == 5:
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid choice.")
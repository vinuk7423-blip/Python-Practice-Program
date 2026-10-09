balance = 10000
pin = 1234
entered_pin = int(input("Enter your PIN:"))
if entered_pin == pin:
    while True:
        print("\n-----ATM Menu-----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            print("Your balance is:",balance)
        elif choice == 2:
            deposit = float(input("Enter deposit amount:"))
            balance = balance + deposit
            print("Money Deposited Successfully.")
            print("New Balance:",balance)
        elif choice == 3:
            withdrawal=float(input("Enter Withdrawal Amount:"))
            if withdrawal <= balance:
                balance = balance - withdrawal
                print("Please collect your cash.")
                print("Remaining balance:",balance)
                print("Insufficient balance.")
            elif choice == 4:
                print("Thank you for using this ATM.")
                break
            else:
                print("Invalid Choice,")
        else:
            print("Incorrect PIN.")
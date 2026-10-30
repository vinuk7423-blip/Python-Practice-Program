try:
    balance = 5000
    amount = int(input("Enter withdrawal amount:"))
    if amount <= 0:
        print("Amount must be positive")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:",balance)
except Exception as e:
    print("Error:",e)
else:
    print("Transaction process completed without exceptions.")
finally:
    print("Thank you for using our banking system.")                        
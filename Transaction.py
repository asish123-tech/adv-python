#TRANSACTION MANAGEMENT SYSTEM
balance = 0

transaction=[]

while True :
    print("\n 1: Deposit")
    print("2: withdraw")
    print("3: transaction history")
    print("4: check balance")
    print("5 exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        transaction.append(f"Deposited: Rs {amount:.2f}")
        print(f"Rs {amount:.2f} deposited successfully.")
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            transaction.append(f"Withdrew: Rs {amount:.2f}")
            print(f"Rs {amount:.2f} withdrawn successfully.")
    elif choice == 3:
        print("\nTransaction History:")
        if len(transaction) == 0:
            print("No transactions yet.")
        else:
            for i in transaction:
                print(i)
    elif choice == 4:
        print(f"Current Balance: Rs {balance:.2f}")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice ! Please try again.")      


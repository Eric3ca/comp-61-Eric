def atm_simulator():
    balance = 1000.0
    print("Welcome to Simple ATM Simulator!")
    
    while True:
        print(f"\nBalance: ${balance:.2f}")
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
    
        choice = input("Enter choice: ")
        
        if choice == "1":
            print(f"Balance: ${balance:.2f}")
        elif choice == "2":
            amount = float(input("Deposit amount: "))
            if amount > 0:
                balance += amount
                print(f"New balance: ${balance:.2f}")
            else:
                print("Invalid deposit.")
        elif choice == "3":
            amount = float(input("Withdraw amount: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"New balance: ${balance:.2f}")
            else:
                print("Invalid amount or insufficient funds.")
        elif choice == "4":
            print("Thank you! Goodbye!")
            break
        else:
            print("Invalid choice.")

atm_simulator()

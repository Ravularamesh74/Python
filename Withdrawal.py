user_pin = "1998"
account_balance = {
    "savings": 10000,
    "current": 5000
}

def atm_simulation():
    print("Welcome to the ATM Simulation\n")

    # Step 1: PIN Verification
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin != user_pin:
        print(" Incorrect PIN. Transaction terminated.")
        return

    # Step 2: Transaction Type
    print("\nSelect Transaction Type:")
    print("1. Withdraw Cash")
    print("2. Check Balance")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "3":
        print("Thank you for using the ATM. Goodbye!")
        return

    # Step 3: Account Type
    print("\nSelect Account Type:")
    print("1. Savings")
    print("2. Current")
    account_choice = input("Enter your choice (1/2): ")

    account_type = "savings" if account_choice == "1" else "current"

    # Step 4: Withdrawal or Balance Check
    if choice == "1":
        amount = int(input(f" Enter amount to withdraw from {account_type} account: ₹"))
        if amount > account_balance[account_type]:
            print("Insufficient balance.")
        else:
            account_balance[account_type] -= amount
            print(f" ₹{amount} withdrawn successfully.")
            print(f" Remaining balance: ₹{account_balance[account_type]}")
    elif choice == "2":
        print(f" Your {account_type} account balance is: ₹{account_balance[account_type]}")
    else:
        print("Invalid transaction type.")

    print("\n Transaction complete. Please take your card.")

# Run the simulation
atm_simulation()
# This code is a simple ATM simulation that allows users to withdraw cash or check their account balance.
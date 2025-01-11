import hashlib

# Create user sample card number and PIN pair, add initial balances.
user_database = {
    "475100": {"pin": hashlib.sha256("58008".encode()).hexdigest(), "balance": 1000.00},
    "475201": {"pin": hashlib.sha256("pswrd".encode()).hexdigest(), "balance": 500.00},
    "476000": {"pin": hashlib.sha256("csu25".encode()).hexdigest(), "balance": 0.00}
}

# Define a function to hash a password for validation
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

# Create a dictionary to track any locked accounts
locked_accounts = {}

# Define a function to validate if the card account is locked
def is_account_locked(card_number):
    return card_number in locked_accounts

# Define a function for ATM feature: Check Balance
def check_balance(card_number):
    balance = user_database[card_number]["balance"]
    print(f"Your current balance is: ${balance:.2f}")
    if balance == 0:
        print("Warning: Your account balance is $0!")

# Define a function for ATM feature: Deposit
def deposit(card_number, amount):
    if amount > 0:
        user_database[card_number]["balance"] += amount
        print(f"Successfully deposited ${amount:.2f}.")
    else:
        print("Deposit cannot be $0.")

# Define a function for ATM feature: Withdrawal
def withdraw(card_number, amount):
    balance = user_database[card_number]["balance"]
    if amount <= 0:
        print("Withdrawal amount cannot be $0.")
    elif amount % 20 != 0:
        print("Withdrawal amount must be in $20 increments.")
    elif amount > balance:
        print("Insufficient funds for this withdrawal.")
    else:
        user_database[card_number]["balance"] -= amount
        print(f"Successfully withdrew ${amount:.2f}.")

# Define a function that handles the login process
def login():
    print("Welcome to the CSU Global ATM!")
    print("To continue, please insert your CARD.")
    card_number_input = input()

# Check if the account is locked
    if is_account_locked(card_number_input):
        print("This card is locked due to too many failed PIN attempts.")
        return False

# Create login attempt metrics and counter
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        pin_input = input("Enter your PIN: ")
        
        # Check if the card number exists and verify the hashed PIN
        if card_number_input in user_database and user_database[card_number_input]["pin"] == hash_pin(pin_input):
            print("Account access granted.")
            return card_number_input
        else:
            attempts += 1
            print(f"Account access failed! You have {max_attempts - attempts} attempt(s) left.")
    
    # Lock the card if max attempts reached
    locked_accounts[card_number_input] = True
    print("Card locked due to too many failed PIN attempts.")
    return False

# Define the main ATM operations menu
def atm_operations(card_number):
    while True:
        print("\nCSU Golbal ATM Operations Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            check_balance(card_number)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            deposit(card_number, amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw ($20 increments): "))
            withdraw(card_number, amount)
        elif choice == '4':
            print("Thank you for using the CSU Global ATM. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option.")

# Example usage
card_number = login()
if card_number:
    atm_operations(card_number)
else:
    print("Exiting the ATM application.")
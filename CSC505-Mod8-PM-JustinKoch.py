# Module 8: Portfolio Milestone (ATM).
# Write a Python script to develop a basic ATM program.

# Import hashlib for hashing the user's password
import hashlib

# Create sample card number and PIN pairs for testing 
user_database = {
    "475100": hashlib.sha256("58008".encode()).hexdigest(),
    "475201": hashlib.sha256("pswrd".encode()).hexdigest(),
    "476000": hashlib.sha256("CSU25".encode()).hexdigest()
}

# Define a function to hash a password for validation
def hash_PIN(PIN):
    return hashlib.sha256(PIN.encode()).hexdigest()

# Create a dictionary to tracked any locked accounts
locked_accounts = {}

# Define a function to validate username account is not locked
def account_locked(card_number):
    return card_number in locked_accounts

# Define a function that handles the login process
def login():
    print("Welcome to the CSU Global ATM!")
    print("To continue, please insert your CARD now:")
    card_number_input = input()
    
    if account_locked(card_number_input):
        print("This account has been locked due to too many failed attempts.")
        return False
    
    # Create login attempt counter
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        PIN_input = input("Enter your PIN: ")
        
        # Validate the card number exists and verify the hashed PIN
        if card_number_input in user_database and user_database[card_number_input] == hash_PIN(PIN_input):
            print("Login successful! Access granted.")
            return True
        else:
            attempts += 1
            print(f"Card number and PIN do not match! You have {max_attempts - attempts} attempt(s) left.")
    
    # Lock the account if max attempts reached
    locked_accounts[card_number_input] = True
    print("This account will be locked due to too many failed attempts.")
    return False

# Run the login function
if login():
    print("You can now access your account.")
else:
    print("Exiting the ATM application.")
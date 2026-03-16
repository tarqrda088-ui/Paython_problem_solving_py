# Project: Full ATM Transaction System
# Logic: Secure withdrawal using indexing and nested lists

accounts = [["tarek", 1000, 1111], ["ezz", 2000, 2222]]

print("--- Welcome to Logicxia Bank ---")
# Correct spelling: choice instead of choise
choice = int(input("Enter your account number (1 or 2): "))

index = choice - 1
current_account = accounts[index]

name = current_account[0]
balance = current_account[1]
correct_pin = current_account[2]

user_pin = int(input(f"Hello {name}, enter your PIN: "))

if user_pin == correct_pin:
    print("Correct PIN!")
    print(f"Your current balance is: {balance}")
    
    withdraw_amount = int(input("How much do you want to withdraw? "))
    
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Success! Your new balance is: {balance}")
    else:
        print("Error: Insufficient funds.")
else:
    print("Error: Wrong PIN.")

print("Thank you for using our service!")

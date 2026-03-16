# Project: Nested Password Verification
# Logic: Using nested lists for security levels

# Correct spelling: passwords instead of basswords
passwords = [["kk", "jj"], ["hh", "gg", "ff"]]
user_input = input("Enter the password: ")

if user_input in passwords[0] or user_input in passwords[1]:
    print("Welcome back!")
else:
    print("Access Denied. Try again.")

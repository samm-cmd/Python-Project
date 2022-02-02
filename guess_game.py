# Guessing Game
# Ask the user to enter a number
# Secret Number is 50
secret_number = 50

# Variable
num = input("Hello, Please Guess the secret number between 1 and 100: ")
# Convert the user input into an integer
num = int(num)

# LOOP / Condition
# 1. Not Equal to secret number, then check if the number is lower or higher
while not (num == secret_number):
    if num > secret_number:
        print("Too High!")
    else:
        print("Too Low")
        # Ask the user for another guess
    num = input("Guess the secret number again between 1 and 100: ")
    num = int(num)
print("Woohoo...Congratulations - You got it right")

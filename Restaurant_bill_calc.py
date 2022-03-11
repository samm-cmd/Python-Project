# Restaurant Bill Calculator

# Ask the Person about the Total Bill
bill_amount = int(input("What is the total on the bill?: "))

# Ask the Person About the Tip S/He Would Like to Give
tip_percent = int(input("what % tip would you like to give?: "))

# Ask For the Total Number of People Sharing the Bill
number_of_people = int(input("How many people are sharing the bill?: "))

# Calculation
tip_amount = bill_amount * (tip_percent / 100)
total_amount = bill_amount + tip_amount

# Results
print("Tip amount per person is: ", tip_amount / number_of_people)
print("Total amount per person is: ", total_amount / number_of_people)

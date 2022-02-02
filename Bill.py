# Restaurant Bill Calculator

bill_amount = int(input("What is the total on the bill?: "))
tip_percent = int(input("what % tip would you like to give?: "))
number_of_people = int(input("How many people are sharing the bill?: "))
tip_amount = bill_amount * (tip_percent / 100)
total_amount = bill_amount + tip_amount
print("Tip amount per person is: ", tip_amount / number_of_people)
print("Total amount per person is: ", total_amount / number_of_people)

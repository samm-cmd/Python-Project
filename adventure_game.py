# Adventure Game
# - Step 1: Importing the - TIME MODULE - to add pauses to the story/game
import time

# - Step 2 - Add an Introduction to the Game -
print("**************************************************")
print("Welcome to the Santa Cruz Mountain Adventure Game!")
print("**************************************************")
print("You're visiting Santa Cruz, California.")
print("You go on an evening hike alone in the mountains.")
print("You can pick one item to take with you - ")
time.sleep(2)
print("map(m), flashlight(f), chocolate(c), rope(r), or stick(s): ")
item = input("What do you choose: ")
print("You hear a hamming sound.")
choise1 = input("Do you follow the sound? Enter y or n: ")

# Step2: WHILE LOOP to Check the user INPUT for Errors - User Should enter either Y or N
while not (choise1 == 'y' or choise1 == 'n'):
    choise1 = input("That is an invalid input. Enter y or n: ")

# - Step 3 - IF Statement -
if choise1 == 'y':
    print("You keep moving closer to the sound.")
    print("The sound suddenly stops.")
    time.sleep(3)
    print("You are now lost! ...")
    time.sleep(3)
    print("You try to call on your phone, but there is no signal!")

# ADD a Choice of Direction using - IF STATEMENT -
    direction = input("Which direction do you go? north, south, east, west: ")
    if direction == 'north':
        print("You reach on abandoned cabin.")
        if item == 'm':
            print("You use the map and find your way home.")
            print("CONGRATULATIONS! Yon won the game.")
        else:
            print("If you had a map, you could find your way from here.")
            print("--- You are still lost. You lost the game. ---")

    elif direction == 'south':
        print("You reach a river with a broken bridge.")
        if item == 'r' or item == 's':
            print("You chose an item that can fix the bridge.")
            print("You fix the bridge, cross over, and find your way home")
            print("CONGRATULATIONS! You won the game.")
        else:
            print("If you had a rope or a stick, you could fix the bridge.")
            print("--- You are still lost. You lost the game. ---")

    elif direction == 'west':
        print("You are walking and trip over a fallen log.")
        print("You have hurt your foot. You sit down and wait for help.")
        print("This could be a long time. You are still lost.")
        print("--- You lost the game. ---")
    else:
        print("You reach the side of the highway. It is dark.")
        if item == 'f':
            print(" You use the flashlight to signal.")
            print("A car stops and gives you a ride home.")
            print("CONGRATULATIONS! You got out safely. You won the game.")
        else:
            print("If you had a flashlight, you could signal for help.")
            print("--- You are still lost. You lost the game. ---")

else:
    print("Good idea. You are not taking risks.")
    print("You start walking back to the starting point.")
    print("You realize you are LOST! ")
    time.sleep(3)
    print("The sound is behind you and is getting louder. You Panic! ")

# - Step 4 - WHILE LOOP
action = input("Do you start running (r), stop to make a call (c)?: ")
while action == 'c':
    print("The call does not go through")
    action = input("Do you want to run (r), or try calling again (c)?: ")
print("You are running fast. The sound gets really loud.")
time.sleep(2)


# - Step 5 - Make the user answer a question to determine next action -
print("A Woman on an electric scooter comes up behind you.")
time.sleep(2)
answer = input('She says, "Name my favorite computer programming language.": ')
if answer.lower() == 'python':
    time.sleep(2)
    print('She says, "Yes, Python is my favorite programming language."')
    print('"If you have some chocolate, I can help you."')
    if item == 'c':
        print("Luckily you did choose correctly!")
        print("You give her the chocolate.")
        print("She helps you get home")
        print("CONGRATULATIONS! You got out safely. You won the game.")
    else:
        print("You should have chosen that chocolate")
        print("She rides away, leaving you alone and lost.")
        print("You lost the game.")
else:
    print("She did not like your answer.")
    print("She rides away. Leaving you lost!")
    print("You lost the game.")

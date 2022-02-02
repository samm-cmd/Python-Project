# 1. Create a small ChatBot
print("Hello. I am Zyx0 64. I am a Chatbot")
print("I like animals and I love to talk about food")

# 2. Get User Input
name = input("What is your name?: ")
print("Hello", name, "Nice to meet you")
year = input("I am not very good at dates. What is the year?: ")
print("Yes. I think that is correct. Thanks!")

# 3. Guess Age
my_age = input("Can you guess my age? - Enter a number: ")
print("Yes you are right. I am", my_age)

# 4. Calculate age
my_age = int(my_age)
new_year = 100 - my_age
print("I will be 100 in", new_year, "years")
print("That will be the year", int(year) + new_year)

# 5. Food Conversation
print("I love chocolate and I also like trying out new kinds of food")
food = input("How about you? What is your favorite food?: ")
print("I like", food, "too.")
question = "how often do you eat " + food + "?: "
howoften = input(question)
print("Interesting. I wonder if that is good for your health")

# 6. Animal Conversation
animal = input("My favorite animal is a giraffe. What is yours?: ")
print(animal, "! I do not like them.")
print("I wonder if a", animal, "likes to eat", food, "?")

# 7. Add a conversation about Feelings
feeling = input("How are you feeling today?: ")
print("Why are you feeling", feeling, "now?")
reason = input("Please tell me: ")
print("I understand. Thanks for sharing")

# 8. GoodBye Message
print("It has been a long day!")
print("I am too tired to talk. We can chat again later.")
print("Goodbye", name, "I liked chatting with you.")

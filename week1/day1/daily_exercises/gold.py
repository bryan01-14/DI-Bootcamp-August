# # Exercise 1


# 1. Ask the user to input a month (1 to 12).
# 2. Display the season of the month received:
# - Spring runs from March (3) to May (5)
# - Summer runs from June (6) to August (8)
# - Autumn runs from September (9) to November (11)
# - Winter runs from December (12) to February (2)

month = int(input("Enter a month (1-12): "))

if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Autumn")
else:
    print("Winter")

# # Exercise 2

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even. 

for i in range(1, 21):
    print(i)

for i in range(1, 21, 2):
    print(i)

# # Exercise 3
# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name. 

name = input("Enter your name: ")

while name != "AKA":
    name = input("Enter your name: ")

print("Hello, AKA!")

# # Exercise 4


# Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.
# Example: if input is Cortana we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Enter your name: ")

if name in names:
    index = names.index(name)
    print(f"{name} is at index {index}")

# # Exercise 5

# Ask the user for 3 numbers and print the greatest number.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    greatest = num1
elif num2 > num1 and num2 > num3:
    greatest = num2
else:
    greatest = num3
print(f"The greatest number is: {greatest}")

# # Exercise 6

# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says “Winner”.
# If the user guesses the wrong number print a message that says “Better luck next time.”
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop, tally up and display total games won and lost.

import random

number = int(input("Enter a number from 1 to 9: "))
random_number = random.randint(1, 9)

while True:
    if number == random_number:
        print("Winner!")
        break
    else:
        print("Better luck next time.")
        break
    


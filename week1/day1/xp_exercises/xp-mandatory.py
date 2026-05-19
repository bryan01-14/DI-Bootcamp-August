# # Exercise 1
# Print the following output using one line of code

print("Hello World \n" *4) 




# # Exercise 2
# Write code that calculates the result of

# (99**3)*8
result2 = (99**3)*8
print(result2)

# # Exercise 3

# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare

5 < 3 # False
3 > 5 # False
3 == 3 # True
3 == "3" # False
"3" > 3 # True
"Hello" == "hello" # False


# # Exercise 4

# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following

computer_brand = "HP"
print(f"I have a {computer_brand} computer")

# # Exercise 5

name = "AKA"
age = 24
shoe_size = 42


info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}"
print(info)

# # Exercise 6

# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World"
a = 10
b = 5
if a > b:
    print("Hello World")

# # Exercise 7

# Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# # Exercise 8

# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
name = input("What is your name? ")
if name == "AKA":    
    print("We have the same name!")
else:
    print("We don't have the same name.")

# # Exercise 9
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.
height = int(input("What is your height in centimeters? "))
if height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")    
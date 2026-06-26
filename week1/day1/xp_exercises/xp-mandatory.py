# # Exercise 1
# Print the following output using one line of code

print("Hello world\n" * 4)




# # Exercise 2
# Write code that calculates the result of

# (99**3)*8
result2 = (99**3)*8
print(result2)

# # Exercise 3

# Predict the output of the following code snippets:
# Comment what is your guess, then run the code and compare

5 < 3   # Prediction: False  — Result: False
3 > 5   # Prediction: False  — Result: False
3 == 3  # Prediction: True   — Result: True
3 == "3"  # Prediction: False  — Result: False
# "3" > 3   # Prediction: True  — CORRECTION: raises TypeError in Python 3
            # Python 3 does not allow comparing a string and an integer with < or >.
            # Running this line produces: TypeError: '>' not supported between instances of 'str' and 'int'
            # The comparison "3" > 3 would only be valid in Python 2 (where it returned True).
"Hello" == "hello"  # Prediction: False  — Result: False


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
# Each variable's value should be a number.
# If a is bigger than b, have your code print "Hello World"
a = 10
b = 5
if a > b:
    print("Hello World")

# # Exercise 7

# Write code that asks the user for a number and determines whether this number is odd or even.

try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("Please enter a valid number.")

# # Exercise 8

# Write code that asks the user for their name and determines whether or not you have the same name.
# Print out a funny message based on the outcome.

try:
    user_name = input("What is your name? ")
    if not user_name.strip():
        raise ValueError("Name cannot be empty.")
    if user_name.strip() == "AKA":
        print("No way, we have the same name! Are you my long-lost twin?!")
    else:
        print(f"Nice to meet you, {user_name.strip()}! We don't share a name, but we can still be friends.")
except ValueError as e:
    print(f"Invalid input: {e}")

# # Exercise 9
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

try:
    height = int(input("What is your height in centimeters? "))
    if height > 145:
        print("You are tall enough to ride.")
    else:
        print("You need to grow some more to ride.")
except ValueError:
    print("Please enter a valid height in centimeters.")

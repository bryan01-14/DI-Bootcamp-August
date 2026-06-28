# Challenge 1



#     Ask the user for a number and a length.
#     Create a program that prints a list of multiples of the number until the list length reaches length.


try:
    number = int(input("Enter a number: "))
    length = int(input("Enter a length: "))
except ValueError:
    print("Please enter valid whole numbers for both the number and the length.")
else:
    liste = []

    for i in range(1, length + 1):
        liste.append(number * i)
    print(liste)


# Challenge 2

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.


string = input("Enter a string: ")
new_chars = []

for i in range(len(string)):
    if i == 0 or string[i] != string[i - 1]:
        new_chars.append(string[i])
new_string = ''.join(new_chars)
print(new_string)





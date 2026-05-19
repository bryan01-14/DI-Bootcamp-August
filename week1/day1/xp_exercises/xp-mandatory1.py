# Challenge 1



#     Ask the user for a number and a length.
#     Create a program that prints a list of multiples of the number until the list length reaches length.


number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

for i in range(1, length + 1):
    print(number * i)


# Challenge 2

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

word = input("Enter a word: ")
new_word = ""

for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        new_word += word[i]
print(new_word)



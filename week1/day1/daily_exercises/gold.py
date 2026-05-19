
#     Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#     Display a little cake as seen below:

#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
day, month, year = map(int, birthdate.split('/'))
age = 2023 - year
candles = age % 100
if candles == 0:
    candles = 100
print("___iiiii___")
print("|:H:a:p:p:y:|")
print("|:B:i:r:t:h:d:a:y:|")        
print(f"~{'~' * candles}~") 


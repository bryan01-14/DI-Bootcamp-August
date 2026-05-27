

# Exercice 1 : Recherche d’anniversaire
# Créez une variable appelée . Sa valeur devrait être un dictionnaire.birthdays
# Initialisez cette variable avec les dates de naissance de 5 personnes de votre choix. Pour chaque entrée du dictionnaire, la clé doit être le nom de la personne, et la valeur doit être sa date de naissance. Conseil : Utilisez le format ."YYYY/MM/DD"
# Imprimez un message de bienvenue pour l’utilisateur. Puis dites-leur : « Vous pouvez chercher les dates de naissance des personnes sur la liste ! »
# Demandez à l’utilisateur de vous donner un et de stocker la réponse dans une variable.person's name
# Obtenez le nom fourni par l’utilisateur.birthday
# Imprimez-le avec un message bien formaté.birthday

birthdays = {
    "Alice": "1990/01/01",
    "Bob": "1995/02/02",    
    "Charlie": "1998/03/03",
    "David": "2001/04/04",
    "Eve": "2004/05/05"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")      
for name in birthdays:
    print(name) 

person_name = input("Who's birthday do you want to look up? ")

if person_name in birthdays:
    birthday = birthdays[person_name]
    print(f"{person_name}'s birthday is {birthday}.")    
else:
    print(f"Sorry, we don't have the birthday information for {person_name}.")


# Exercice 2 : Anniversaires avancés
# Avant de demander à l’utilisateur d’entrer un , imprimez tous les noms dans le dictionnaire.person's name
# Si la personne que l’utilisateur tape n’apparaît pas dans le dictionnaire, imprimez un message d’erreur (« Désolé, nous n’avons pas les informations de date de naissance »).person's name

birthdays = {
    "Alice": "1990/01/01",
    "Bob": "1995/02/02",    
    "Charlie": "1998/03/03",
    "David": "2001/04/04",
    "Eve": "2004/05/05"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")      
for name in birthdays:
    print(name) 

person_name = input("Who's birthday do you want to look up? ")

if person_name in birthdays:
    birthday = birthdays[person_name]
    print(f"{person_name}'s birthday is {birthday}.")    
else:    print(f"Sorry, we don't have the birthday information for {person_name}.") 


# nstructions
# Utilisation de cette variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Demandez son nom à un utilisateur, si son nom figure dans la liste des noms, imprimez l’index de la première apparition du nom.

# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    index = names.index(user_name)
    print(f"{user_name} is found at index {index}.")
else:    print(f"{user_name} is not found in the list.")


# Exercice 4 : Double Dé
# Créez une fonction qui simule le lancer d’un dé. Appelez ça . Il devrait retourner un entier compris entre 1 et 6.throw_dice
# Créer une fonction appelée .
# Il devrait continuer à lancer 2 dés (en utilisant votre fonction) jusqu’à ce qu’ils atteignent le même nombre, c’est-à-dire jusqu’à ce que nous atteignions les doubles.
# Par exemple : (1, 2), (3, 1), (5, 5) → alors arrêter de lancer, car des doubles ont été atteints.
# Cette fonction devrait restituer le nombre total de fois où elle a lancé les dés. Dans l’exemple ci-dessus, il devrait retourner 3.throw_until_doublesthrow_dice
# Créez une fonction principale. Il devrait lancer des doubles 100 fois (c’est-à-dire appeler votre fonction 100 fois), et stocker les résultats de ces appels de fonction (en d’autres termes, combien de lancers il a fallu avant que les doubles soient lancés, à chaque fois) dans une collection. (Quel genre de collection ? Lisez ci-dessous pour comprendre à quoi nous aurons besoin des données, et cela devrait vous aider à décider quelle structure de données utiliser).throw_until_doubles
# Après avoir lancé les 100 doubles, imprimez un message indiquant à l’utilisateur combien de lancers il a fallu au total pour atteindre 100 doubles.
# Imprimez aussi un message indiquant à l’utilisateur le nombre moyen de lancers nécessaires pour atteindre les doubles. Arrondis cela à deux décimales.
# Par exemple :

# Si les résultats des lancers étaient les suivants (votre code ferait 100 doubles, pas seulement 3) :

# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)
# Ensuite, ma sortie affichait quelque chose comme ceci :

# Total throws: 8
# Average throws to reach doubles: 2.67.

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:
            return count
def main():
    total_throws = 0
    for _ in range(100):
        throws = throw_until_doubles()
        total_throws += throws
    average_throws = total_throws / 100
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()

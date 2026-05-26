
# Exercice 1 : Voitures
# Copiez la chaîne suivante dans votre code : .Volkswagen, Toyota, Ford Motor, Honda, Chevrolet
# Convertissez-le en liste avec Python (ne le faites pas à la main !).
# Imprimez un message indiquant combien de fabricants/entreprises figurent sur la liste.
# Imprimez la liste des fabricants dans l’ordre inverse/décroissant (Z-A).
# Utilisation de boucles ou de compréhension de liste :
# Découvrez combien contiennent la lettre.manufacturers’ nameso
# Découvrez combien n’ont pas la lettre dedans.manufacturers’ namesi

manufacturers = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
manufacturers_list = manufacturers.split(", ")
print("There are", len(manufacturers_list), "manufacturers.")
manufacturers_list.reverse()
print(manufacturers_list)   

manufacturers_with_a = [m for m in manufacturers_list if 'a' in m]
print("Manufacturers with 'a':", manufacturers_with_a)
manufacturers_without_a = [m for m in manufacturers_list if 'a' not in m]
print("Manufacturers without 'a':", manufacturers_without_a) 


# Bonus :

# Il y a quelques doublons dans cette liste : ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Supprimez-les de façon programmatique. (Indice : vous pouvez utiliser un ensemble pour vous aider).
# Imprimez les entreprises sans doublons, dans une chaîne séparée par des virgules sans sauts de ligne (par exemple, « Acura, Alfa Romeo, Aston Martin, ... »), et imprimez également un message indiquant combien d’entreprises figurent désormais dans la liste.

manufacturers_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_manufacturers = set(manufacturers_with_duplicates)
unique_manufacturers_list = list(unique_manufacturers)
print("Unique manufacturers:", ", ".join(unique_manufacturers_list))
print("There are", len(unique_manufacturers_list), "unique manufacturers.")



# Bonus :

# Imprimez la liste des fabricants dans l’ordre croissant (A à Z), mais inversez les lettres du nom de chaque fabricant.

reversed_manufacturers = [m[::-1] for m in manufacturers_list]
reversed_manufacturers.sort()
print("Reversed manufacturers in ascending order:", reversed_manufacturers)



# Exercice 2 : Comment vous appelez-vous ?
# Écrivons une fonction appelée qui prend trois arguments : 1 : , 2 : , 3 : .get_full_name()first_namemiddle_namelast_name
# middle_name devrait être optionnel ; Si l’utilisateur l’omet, le nom retourné ne doit contenir que le prénom et le nom de famille.
# Par exemple, il retournera « John Hooker Lee ».
# Mais il reviendra « Bruce Lee ».get_full_name(first_name="john", middle_name="hooker", last_name="lee")get_full_name(first_name="bruce", last_name="lee")

def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"
    
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))

# Exercice 3 : De l’anglais au morse
# Écrivez une fonction qui convertit le texte anglais en code Morse et une autre qui fait l’inverse.
# Indice : Cherchez sur internet un tableau de traduction, chaque lettre est séparée par un espace et chaque mot par une barre oblique /.

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    ' ': '/'
}    

def english_to_morse(text):
    morse_code = ' '.join([morse_code_dict[char.upper()] for char in text])
    return morse_code    

def morse_to_english(morse_code):    
    inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}
    english_text = ''.join([inverse_morse_code_dict[code] for code in morse_code.split()])
    return english_text    

print(english_to_morse("Hello, world!"))    
print(morse_to_english(".- .-.. .-.. .. -.-. -.-")) 
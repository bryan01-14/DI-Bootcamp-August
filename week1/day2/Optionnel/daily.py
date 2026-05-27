
# Défi quotidien Or : Résoudre la Matrice

# Ce que tu vas apprendre
# Bases de Python
# Conditions
# Boucles
# Fonctions


# Instructions
# Avec une chaîne « matrice » :

# 7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%
# ^r!


# La matrice est une grille de chaînes de caractères (caractères alphanumériques et espaces) avec un message caché à l’intérieur.
# Une grille signifie que vous pourriez potentiellement la diviser en lignes et colonnes, comme ici :

# 7	i	i
# T	s	x
# h	%	?
# i		#
# s	M	
# $	a	
# #	t	%
# ^	r	!


# Matrice : Une matrice est un tableau bidimensionnel. C’est une grille de chiffres disposés en rangées et colonnes.
# Pour reproduire la grille, la matrice doit être une liste 2D, pas une chaîne



# Pour déchiffrer la matrice, Neo lit chaque colonne de haut en bas, en commençant par la colonne la plus à gauche, ne sélectionnant que les caractères alpha et les reliant. Ensuite, il remplace chaque groupe de symboles entre deux caractères alpha par un espace.

# En utilisant sa technique, essayez de décoder cette matrice.

# Indices :

# Utilisation

# ● listes pour stocker les données
# ● Boucles pour passer en revue les données
# ● instructions if/else pour vérifier les données
# ● Chaîne pour la sortie du message secret

matrix = [
    "7ii",
    "Tsx",    
    "h%?",
    "i #",    
    "sM",
    "$a",
    "#t%",
    "^r!"
]    
secret_message = ""
for i in range(len(matrix[0])):
    for row in matrix:
        if i < len(row) and row[i].isalpha():
            secret_message += row[i]
        elif secret_message and not secret_message[-1].isspace():
            secret_message += " "   
secret_message = ' '.join(secret_message.split())
print("Secret message:", secret_message)

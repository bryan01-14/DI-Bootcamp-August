
# Exercice 1


# Écrivez une classe appelée qui reçoit un rayon comme argument (par défaut est 1.0).Circle
class Circle:
    def __init__(seft, rayon=1.0):
        seft.rayon = rayon
    def perimetre(seft):
        return 2 * 3.14 * seft.rayon
    def surface(seft):
        return 3.14 * seft.rayon ** 2
    def afficher_rayon(seft):
        print(f"Le rayon du cercle est : {seft.rayon}")

rayon = Circle(5)
rayon.afficher_rayon()


# Exercice 2

class MyList:
    list = []
    def __init__(self, list):
        self.list = list   
    def inverse(self):
        inv =  self.list[::-1]
        print(f"La liste inversée est : {inv}")
    def tri(self):
        tr =  sorted(self.list)
        print(f"La liste triée est : {tr}")
    def afficher(self):
        print(f"La liste est : {self.list}")

mylist = MyList([3, 1, 4, 2])
mylist.afficher()
mylist.inverse()
mylist.tri()


# Exercice 3


class MenuManager:
    def __init__(self):
        self.menu = {}
    def ajouter_plat(self, nom, prix):
        self.menu[nom] = prix
    def afficher_menu(self):
        print("Menu :")
        for nom, prix in self.menu.items():
            print(f"{nom} : {prix}€")


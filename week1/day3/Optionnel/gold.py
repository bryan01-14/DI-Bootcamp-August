
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
    """A class to manage a restaurant menu."""

    def __init__(self):
        """Initialize the MenuManager with a default menu."""
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

    def add_item(self, name, price, spice, gluten):
        """Add a new dish to the menu."""
        new_item = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_item)
        print(f"{name} has been added to the menu.")

    def update_item(self, name, price, spice, gluten):
        """Update an existing dish on the menu."""
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                print(f"{name} has been updated.")
                print(self.menu)
                return
        print(f"{name} is not on the menu.")

    def remove_item(self, name):
        """Remove a dish from the menu if it exists."""
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"{name} has been removed from the menu.")
                print(self.menu)
                return
        print(f"{name} is not on the menu.")


def main():
    """Main function to test the MenuManager class."""
    manager = MenuManager()

    # Test add_item
    print("--- Add Item ---")
    manager.add_item("Pizza", 20, "A", True)
    manager.add_item("Tacos", 12, "C", False)

    # Test update_item
    print("\n--- Update Item ---")
    manager.update_item("Soup", 12, "A", False)
    manager.update_item("Pasta", 18, "B", True)  # Not on menu

    # Test remove_item
    print("\n--- Remove Item ---")
    manager.remove_item("Salad")
    manager.remove_item("Sushi")  # Not on menu


if __name__ == "__main__":
    main()
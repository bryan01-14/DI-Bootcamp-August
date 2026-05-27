class Animal:
    """Classe de base représentant un animal."""

    # Attribut de classe (partagé par tous les objets)
    kingdom = "Animalia"

    def __init__(self, name, age):
        """Constructeur : appelé automatiquement à la création."""
        # Attributs d'instance (propres à chaque objet)
        self.name = name
        self.age = age

    def speak(self):
        """Méthode de base — sera overridée par les enfants."""
        return f"{self.name} makes a sound."




class Dog(Animal):
    """Chien — hérite de Animal et override speak()."""

    def speak(self):
        """Override de la méthode speak() du parent."""
        return f"{self.name} barks!"


class Cat(Animal):
    """Chat — hérite de Animal et override speak()."""

    def speak(self):
        """Override de la méthode speak() du parent."""
        return f"{self.name} meows!"




class PoliceDog(Dog):
    """Chien policier — hérite de Dog, ajoute un attribut badge."""

    def __init__(self, name, age, badge):
        """Appelle __init__ du parent avec super(), puis ajoute badge."""
        super().__init__(name, age)  # Appelle Dog -> Animal __init__
        self.badge = badge




class Circle:
    """Cercle — démontre les principales méthodes dunder."""

    def __init__(self, radius):
        """Initialise le rayon du cercle."""
        self.radius = radius

    def __str__(self):
        """Appelé par print(obj) — affichage convivial."""
        return f"Circle(r={self.radius})"

    def __repr__(self):
        """Appelé par repr(obj) — affichage technique."""
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """Appelé par obj1 + obj2 — retourne un nouveau cercle."""
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        """Appelé par obj1 == obj2 — compare les rayons."""
        return self.radius == other.radius

    def __gt__(self, other):
        """Appelé par obj1 > obj2 — compare les rayons."""
        return self.radius > other.radius

    def __lt__(self, other):
        """Appelé par obj1 < obj2 — permet aussi sorted()."""
        return self.radius < other.radius




class Species:
    """Démontre la différence entre attribut de classe et d'instance."""

    # Attribut de CLASSE : commun à tous les objets
    category = "Mammal"

    def __init__(self, name):
        # Attribut d'INSTANCE : propre à chaque objet
        self.name = name




def main():
    """Teste tous les concepts OOP."""

    # --- 1. Classe de base ---
    print("=" * 50)
    print("1. Classe de base")
    print("=" * 50)
    animal = Animal("Generic", 5)
    print(animal.speak())        # Generic makes a sound.
    print(animal.kingdom)        # Animalia  ← attribut de classe

    # --- 2. Héritage + Polymorphisme ---
    print("\n" + "=" * 50)
    print("2. Héritage + Polymorphisme")
    print("=" * 50)
    dog = Dog("Rex", 3)
    cat = Cat("Luna", 2)
    print(dog.speak())           # Rex barks!
    print(cat.speak())           # Luna meows!
    print(dog.name)              # Rex  ← hérité de Animal
    print(dog.kingdom)           # Animalia  ← hérité de Animal

    # --- 3. super() ---
    print("\n" + "=" * 50)
    print("3. super()")
    print("=" * 50)
    police = PoliceDog("Max", 4, "K9-007")
    print(police.name)           # Max   ← hérité via super()
    print(police.age)            # 4     ← hérité via super()
    print(police.badge)          # K9-007 ← propre à PoliceDog
    print(police.speak())        # Max barks! ← hérité de Dog

    # --- 4. Dunder Methods ---
    print("\n" + "=" * 50)
    print("4. Méthodes Dunder")
    print("=" * 50)
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(7)

    print(c1)                    # Circle(r=5)   ← __str__
    print(repr(c1))              # Circle(radius=5) ← __repr__
    print(c1 + c2)               # Circle(r=8)   ← __add__
    print(c1 == c2)              # False         ← __eq__
    print(c1 == Circle(5))       # True          ← __eq__
    print(c1 > c2)               # True          ← __gt__
    print(c2 < c3)               # True          ← __lt__

    # sorted() utilise __lt__
    circles = [c3, c1, c2]
    print(sorted(circles))       # [r=3, r=5, r=7] ← __lt__

    # --- 5. Attribut de classe vs d'instance ---
    print("\n" + "=" * 50)
    print("5. Attribut de classe vs d'instance")
    print("=" * 50)
    s1 = Species("Lion")
    s2 = Species("Tiger")
    print(s1.category)           # Mammal ← attribut de CLASSE
    print(s2.category)           # Mammal ← même pour tous
    print(s1.name)               # Lion   ← attribut d'INSTANCE
    print(s2.name)               # Tiger  ← différent par objet

    # --- Résumé des dunder ---
    print("\n" + "=" * 50)
    print("Résumé Dunder")
    print("=" * 50)
    print("__init__  → Dog('Rex', 3)")
    print("__str__   → print(obj)")
    print("__repr__  → repr(obj)")
    print("__add__   → obj1 + obj2")
    print("__eq__    → obj1 == obj2")
    print("__gt__    → obj1 > obj2")
    print("__lt__    → obj1 < obj2 / sorted()")


if __name__ == "__main__":
    main()
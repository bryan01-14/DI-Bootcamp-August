"""Exercise 1: Pets - Inheritance and Polymorphism."""


class Pets:
    """A class to represent a collection of pets."""

    def __init__(self, animals):
        """Initialize with a list of animals."""
        self.animals = animals

    def walk(self):
        """Walk all animals."""
        for animal in self.animals:
            print(animal.walk())


class Cat:
    """A class to represent a cat."""

    is_lazy = True

    def __init__(self, name, age):
        """Initialize a new Cat instance."""
        self.name = name
        self.age = age

    def walk(self):
        """Return a walking message."""
        return f'{self.name} is just walking around'


class Bengal(Cat):
    """A class to represent a Bengal cat."""

    def sing(self, sounds):
        """Make the Bengal cat sing."""
        return f'{sounds}'


class Chartreux(Cat):
    """A class to represent a Chartreux cat."""

    def sing(self, sounds):
        """Make the Chartreux cat sing."""
        return f'{sounds}'


class Siamese(Cat):
    """A class to represent a Siamese cat, inherits from Cat."""

    def sing(self, sounds):
        """Make the Siamese cat sing."""
        return f'{sounds}'


def main():
    """Main function to test Exercise 1."""
    # Step 2: Create cat instances
    bengal = Bengal("Simba", 3)
    chartreux = Chartreux("Luna", 5)
    siamese = Siamese("Milo", 2)

    all_cats = [bengal, chartreux, siamese]

    # Step 3: Create Pets instance
    sara_pets = Pets(all_cats)

    # Step 4: Walk the cats
    sara_pets.walk()


if __name__ == "__main__":
    main()
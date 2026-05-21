import random


# ============================================================
# Exercice 1 : Animaux de compagnie
# ============================================================

class Pets:
    """A class to represent a collection of pets."""

    def __init__(self, animals):
        """Initialize with a list of animals."""
        self.animals = animals

    def walk(self):
        """Walk all animals in the collection."""
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
    """A class to represent a Bengal cat, inherits from Cat."""

    def sing(self, sounds):
        """Make the Bengal cat sing."""
        return f'{sounds}'


class Chartreux(Cat):
    """A class to represent a Chartreux cat, inherits from Cat."""

    def sing(self, sounds):
        """Make the Chartreux cat sing."""
        return f'{sounds}'


class Siamese(Cat):
    """A class to represent a Siamese cat, inherits from Cat."""

    def sing(self, sounds):
        """Make the Siamese cat sing."""
        return f'{sounds}'


# ============================================================
# Exercice 2 : Les chiens
# ============================================================

class Dog:
    """A class to represent a dog."""

    def __init__(self, name, age, weight):
        """Initialize a new Dog instance."""
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        """Return a barking message."""
        return f'{self.name} is barking.'

    def run_speed(self):
        """Return the run speed of the dog."""
        return self.weight / self.age * 10

    def fight(self, other_dog):
        """Determine the winner of a fight between two dogs."""
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f'{self.name} wins the fight!'
        elif other_power > my_power:
            return f'{other_dog.name} wins the fight!'
        else:
            return "It's a tie!"


# ============================================================
# Exercice 3 : Les chiens domestiques
# ============================================================

class PetDog(Dog):
    """A class to represent a pet dog, inherits from Dog."""

    def __init__(self, name, age, weight):
        """Initialize a new PetDog instance."""
        super().__init__(name, age, weight)
        self.trained = False  # Default: not trained

    def train(self):
        """Train the dog and mark it as trained."""
        print(self.bark())
        self.trained = True

    def play(self, *args):
        """Play with other dogs."""
        # Collect all dog names including self
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dog_names)} are all playing together.")

    def do_a_trick(self):
        """Perform a random trick if the dog is trained."""
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet.")


# ============================================================
# Exercice 4 : Classes Famille et Personne
# ============================================================

class Person:
    """A class to represent a person."""

    def __init__(self, first_name, age):
        """Initialize a new Person instance."""
        self.first_name = first_name
        self.age = age
        self.last_name = ""  # Initialized as empty string

    def is_18(self):
        """Return True if the person is 18 or older, otherwise False."""
        return self.age >= 18


class Family:
    """A class to represent a family."""

    def __init__(self, last_name):
        """Initialize a new Family instance."""
        self.last_name = last_name
        self.members = []  # Empty list to store Person objects

    def born(self, first_name, age):
        """Create a new Person and add them to the family."""
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        """Check if a family member is 18 or older."""
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"{first_name} is not a member of the family.")

    def family_presentation(self):
        """Print the family name and all members' details."""
        print(f"Family name: {self.last_name}")
        for member in self.members:
            print(f"  {member.first_name} - Age: {member.age}")


# ============================================================
# Main : Tests de tous les exercices
# ============================================================

def main():
    """Main function to test all exercises."""

    # --- Exercice 1 ---
    print("=" * 40)
    print("Exercice 1 : Animaux de compagnie")
    print("=" * 40)

    bengal = Bengal("Bengal", 3)
    chartreux = Chartreux("Chartreux", 5)
    siamese = Siamese("Siamese", 2)

    all_cats = [bengal, chartreux, siamese]
    sara_pets = Pets(all_cats)
    sara_pets.walk()

    # --- Exercice 2 ---
    print("\n" + "=" * 40)
    print("Exercice 2 : Les chiens")
    print("=" * 40)

    dog1 = Dog("Rex", 3, 30)
    dog2 = Dog("Bella", 5, 20)
    dog3 = Dog("Max", 4, 25)

    print(dog1.bark())
    print(f"{dog2.name} run speed: {dog2.run_speed()}")
    print(dog1.fight(dog2))
    print(dog2.fight(dog3))

    # --- Exercice 3 ---
    print("\n" + "=" * 40)
    print("Exercice 3 : Les chiens domestiques")
    print("=" * 40)

    pet1 = PetDog("Fido", 2, 10)
    pet2 = PetDog("Buddy", 3, 15)
    pet3 = PetDog("Max", 4, 20)

    # Test do_a_trick before training
    pet1.do_a_trick()

    # Train and test
    pet1.train()
    pet1.do_a_trick()

    # Test play with multiple dogs
    pet1.play(pet2, pet3)

    # --- Exercice 4 ---
    print("\n" + "=" * 40)
    print("Exercice 4 : Famille et Personne")
    print("=" * 40)

    family = Family("Smith")
    family.born("Alice", 20)
    family.born("Bob", 15)
    family.born("Charlie", 18)

    family.family_presentation()

    print()
    family.check_majority("Alice")    # Over 18
    family.check_majority("Bob")      # Under 18
    family.check_majority("Charlie")  # Exactly 18
    family.check_majority("Diana")    # Not a member


if __name__ == "__main__":
    main()
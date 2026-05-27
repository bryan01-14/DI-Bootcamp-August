"""Exercise 3: PetDog - Inheritance from Dog."""

import random
from exercise2_dogs import Dog


class PetDog(Dog):
    """A class to represent a pet dog, inherits from Dog."""

    def __init__(self, name, age, weight):
        """Initialize a new PetDog instance."""
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        """Train the dog and mark it as trained."""
        print(self.bark())
        self.trained = True

    def play(self, *args):
        """Play with other dogs."""
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


def main():
    """Main function to test Exercise 3."""
    pet1 = PetDog("Fido", 2, 10)
    pet2 = PetDog("Buddy", 3, 15)
    pet3 = PetDog("Max", 4, 20)

    # Test before training
    pet1.do_a_trick()

    # Train and test
    pet1.train()
    pet1.do_a_trick()

    # Play together
    pet1.play(pet2, pet3)


if __name__ == "__main__":
    main()
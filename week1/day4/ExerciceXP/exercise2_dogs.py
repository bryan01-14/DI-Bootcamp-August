"""Exercise 2: Dogs - Classes and Methods."""


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


def main():
    """Main function to test Exercise 2."""
    dog1 = Dog("Rex", 3, 30)
    dog2 = Dog("Bella", 5, 20)
    dog3 = Dog("Max", 4, 25)

    print(dog1.bark())
    print(f"{dog2.name} run speed: {dog2.run_speed()}")
    print(dog1.fight(dog2))
    print(dog2.fight(dog3))


if __name__ == "__main__":
    main()
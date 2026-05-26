"""Exercise 4: Person and Family classes."""


class Person:
    """A class to represent a person."""

    def __init__(self, first_name, age):
        """Initialize a new Person instance."""
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        """Return True if the person is 18 or older."""
        return self.age >= 18


class Family:
    """A class to represent a family."""

    def __init__(self, last_name):
        """Initialize a new Family instance."""
        self.last_name = last_name
        self.members = []

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


def main():
    """Main function to test Exercise 4."""
    family = Family("Smith")
    family.born("Alice", 20)
    family.born("Bob", 15)
    family.born("Charlie", 18)

    family.family_presentation()
    print()
    family.check_majority("Alice")
    family.check_majority("Bob")
    family.check_majority("Charlie")
    family.check_majority("Diana")


if __name__ == "__main__":
    main()
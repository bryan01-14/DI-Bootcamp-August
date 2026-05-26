"""game.py - Game class for Rock Paper Scissors."""

import random


class Game:
    """A class to represent a single Rock Paper Scissors game."""

    ITEMS = ["rock", "paper", "scissors"]

    # Winning combinations: key beats value
    WINS = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    def get_user_item(self):
        """
        Ask the user to select rock, paper, or scissors.
        Keep asking until a valid choice is made.
        Returns the user's choice as a string.
        """
        while True:
            user_input = input("\nChoose your item (rock / paper / scissors): ").strip().lower()
            if user_input in self.ITEMS:
                return user_input
            print(f"  Invalid choice '{user_input}'. Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        """
        Randomly select rock, paper, or scissors for the computer.
        Returns the computer's choice as a string.
        """
        return random.choice(self.ITEMS)

    def get_game_result(self, user_item, computer_item):
        """
        Determine the result of the game.
        Parameters:
            user_item     : the item chosen by the user
            computer_item : the item chosen by the computer
        Returns:
            'win'  - user wins
            'draw' - both chose the same item
            'loss' - user loses
        """
        if user_item == computer_item:
            return "draw"
        elif self.WINS[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        Play a single round of Rock Paper Scissors.
        - Gets user item
        - Gets computer item
        - Determines result
        - Prints the round output
        Returns:
            result as string: 'win', 'draw', or 'loss'
        """
        # Get both items
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        # Determine result
        result = self.get_game_result(user_item, computer_item)

        # Print round summary
        print(f"\n  You chose     : {user_item}")
        print(f"  Computer chose: {computer_item}")

        if result == "win":
            print("  🎉 You win!")
        elif result == "draw":
            print("  🤝 It's a draw!")
        else:
            print("  💻 Computer wins! You lose.")

        return result
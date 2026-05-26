"""rock-paper-scissors.py - Main file to run the Rock Paper Scissors game."""

from game import Game


def get_user_menu_choice():
    """
    Display the main menu and get the user's choice.
    No looping here — just display, get input, and return.
    Valid options:
        '1' - Play a new game
        '2' - Show scores
        'q' - Quit
    Returns the user's choice as a string.
    """
    print("\n" + "=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("=" * 40)
    print("  1. Play a new game")
    print("  2. Show scores")
    print("  q. Quit")
    print("=" * 40)

    choice = input("  Your choice: ").strip().lower()
    return choice


def print_results(results):
    """
    Print a friendly summary of all games played.
    Parameters:
        results : dict with keys 'win', 'loss', 'draw' and int values
                  Example: {'win': 2, 'loss': 4, 'draw': 3}
    """
    total = results["win"] + results["loss"] + results["draw"]

    print("\n" + "=" * 40)
    print("        GAME SUMMARY")
    print("=" * 40)
    print(f"  Total games played : {total}")
    print(f"   Wins            : {results['win']}")
    print(f"   Losses          : {results['loss']}")
    print(f"   Draws           : {results['draw']}")
    print("=" * 40)

    # Friendly conclusion
    if results["win"] > results["loss"]:
        print("   Great job! You beat the computer overall!")
    elif results["loss"] > results["win"]:
        print("   The computer won overall. Better luck next time!")
    else:
        print("    It's overall a draw. Well played!")

    print("\n  Thanks for playing Rock Paper Scissors! Goodbye! 👋")
    print("=" * 40)


def main():
    """
    Main function:
    - Shows the menu repeatedly until the user quits
    - Plays games and tracks results
    - Prints a summary when the user quits
    """
    # Initialize results tracker
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }

    print("\n  Welcome to Rock Paper Scissors! 🎮")

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            # Play a new game
            game = Game()
            result = game.play()

            # Update results tracker
            if result in results:
                results[result] += 1
            else:
                print(f"  Unexpected result: {result}")

        elif choice == "2":
            # Show current scores
            total = results["win"] + results["loss"] + results["draw"]
            if total == 0:
                print("\n  No games played yet. Start playing!")
            else:
                print("\n  --- Current Scores ---")
                print(f"   Wins  : {results['win']}")
                print(f"   Losses: {results['loss']}")
                print(f"   Draws : {results['draw']}")

        elif choice == "q":
            # Quit and show final summary
            print_results(results)
            break

        else:
            print(f"\n  Invalid option '{choice}'. Please choose 1, 2, or q.")


if __name__ == "__main__":
    main()
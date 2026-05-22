import sys



class BankAccount:
    """A class to represent a bank account."""

    def __init__(self, balance, username, password):
        """Initialize a new BankAccount instance."""
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False  # Default: not authenticated

    def authenticate(self, username, password):
        """Authenticate the user with username and password."""
        if self.username == username and self.password == password:
            self.authenticated = True
            print("Authentication successful.")
        else:
            print("Invalid username or password.")

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if not self.authenticated:
            raise Exception("You must be authenticated to deposit.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw a positive amount from the account."""
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# ============================================================
# Partie II : Classe MinimumBalanceAccount
# ============================================================

class MinimumBalanceAccount(BankAccount):
    """A class to represent a bank account with a minimum balance."""

    def __init__(self, balance, username, password, minimum_balance=0):
        """Initialize a new MinimumBalanceAccount instance."""
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        """Withdraw only if balance stays above minimum balance."""
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(
                f"Cannot withdraw. Balance would go below minimum balance of {self.minimum_balance}."
            )
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# ============================================================
# Partie IV : BONUS - Classe ATM
# ============================================================

class ATM:
    """A class to represent an ATM machine."""

    def __init__(self, account_list, try_limit):
        """Initialize a new ATM instance."""
        # Validate account_list contains only BankAccount or MinimumBalanceAccount
        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise Exception("account_list must contain BankAccount or MinimumBalanceAccount instances.")

        self.account_list = account_list

        # Validate try_limit is a positive number
        try:
            if try_limit <= 0:
                raise Exception("try_limit must be a positive number.")
            self.try_limit = try_limit
        except Exception:
            print("Invalid try_limit. Setting try_limit to 2.")
            self.try_limit = 2

        self.current_tries = 0

        # Start the main menu
        self.show_main_menu()

    def show_main_menu(self):
        """Display the main menu and handle user selection."""
        while True:
            print("\n====== ATM Main Menu ======")
            print("1. Login")
            print("2. Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                self.log_in(username, password)
            elif choice == "2":
                print("Thank you for using the ATM. Goodbye!")
                sys.exit()
            else:
                print("Invalid option. Please try again.")

    def log_in(self, username, password):
        """Log in with username and password."""
        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticate(username, password)
                self.current_tries = 0  # Reset tries on success
                self.show_account_menu(account)
                return

        # No match found
        self.current_tries += 1
        remaining = self.try_limit - self.current_tries
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            sys.exit()
        else:
            print(f"Invalid credentials. {remaining} attempt(s) remaining.")

    def show_account_menu(self, account):
        """Display the account menu for deposit, withdraw, or exit."""
        while True:
            print(f"\n====== Account Menu (Balance: {account.balance}) ======")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                try:
                    amount = int(input("Enter deposit amount: ").strip())
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = int(input("Enter withdrawal amount: ").strip())
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                print("Logging out...")
                account.authenticated = False  # Reset authentication on logout
                break
            else:
                print("Invalid option. Please try again.")


# ============================================================
# Main : Tests
# ============================================================

def main():
    """Main function to test all parts."""

    # --- Partie I & III : BankAccount ---
    print("=" * 40)
    print("Test BankAccount")
    print("=" * 40)

    account1 = BankAccount(1000, "alice", "pass123")

    # Test sans authentification
    try:
        account1.deposit(500)
    except Exception as e:
        print(f"Error: {e}")

    # Authentification
    account1.authenticate("alice", "pass123")
    account1.deposit(500)
    account1.withdraw(200)

    # Test montant négatif
    try:
        account1.deposit(-100)
    except Exception as e:
        print(f"Error: {e}")

    # --- Partie II : MinimumBalanceAccount ---
    print("\n" + "=" * 40)
    print("Test MinimumBalanceAccount")
    print("=" * 40)

    account2 = MinimumBalanceAccount(500, "bob", "securepass", minimum_balance=100)
    account2.authenticate("bob", "securepass")
    account2.deposit(200)

    # Retrait qui passe
    account2.withdraw(100)

    # Retrait qui échoue (solde trop bas)
    try:
        account2.withdraw(600)
    except Exception as e:
        print(f"Error: {e}")

    # --- Partie IV : ATM (décommenté pour tester interactivement) ---
    # print("\n" + "=" * 40)
    # print("Test ATM")
    # print("=" * 40)
    # atm = ATM([account1, account2], try_limit=3)


if __name__ == "__main__":
    main()
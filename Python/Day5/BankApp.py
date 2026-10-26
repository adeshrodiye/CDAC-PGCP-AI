from Accounts import (
    Account,
    SavingAccount,
    CurrentAccount,
    InvalidAmountError,
    ExceedsDepositLimitError,
    InsufficientBalanceError,
)

class Transaction:
    @staticmethod
    def withdraw_from_account(account: Account, amount: float) -> float:
        return account.withdraw(amount)

    @staticmethod
    def deposit_to_account(account: Account, amount: float) -> float:
        return account.deposit(amount)


class User:
    def __init__(self, account: Account):
        self.account = account
        self.transaction_history = []

    def run_menu(self):
        print("\n=========================================")
        print(f" Welcome, {self.account.name} (Acc ID: {self.account.acc_id})")
        print(f" Initial Balance: ₹{self.account.balance:,.2f}")
        print("=========================================")

        while True:
            print("\nMenu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit & Show Statement")

            try:
                choice = int(input("Enter your choice (1-3): "))
            except ValueError:
                print("Invalid input! Please enter a number (1, 2, or 3).")
                continue

            if choice == 1:
                try:
                    amount = float(input("Enter Amount to Deposit: ₹"))
                    new_balance = Transaction.deposit_to_account(self.account, amount)
                    log = f"Deposited: ₹{amount:,.2f} | Updated Balance: ₹{new_balance:,.2f}"
                    self.transaction_history.append(log)
                    print(f"SUCCESS -> {log}")
                except (InvalidAmountError, ExceedsDepositLimitError) as e:
                    print(f"TRANSACTION FAILED: {e}")
                except ValueError:
                    print("Invalid amount format!")

            elif choice == 2:
                try:
                    amount = float(input("Enter Amount to Withdraw: ₹"))
                    new_balance = Transaction.withdraw_from_account(self.account, amount)
                    log = f"Withdrew: ₹{amount:,.2f} | Updated Balance: ₹{new_balance:,.2f}"
                    self.transaction_history.append(log)
                    print(f"SUCCESS -> {log}")
                except (InvalidAmountError, InsufficientBalanceError) as e:
                    print(f"TRANSACTION FAILED: {e}")
                except ValueError:
                    print("Invalid amount format!")

            elif choice == 3:
                self.display_statement()
                break
            else:
                print("Invalid option selected. Please enter 1, 2, or 3.")

    def display_statement(self):
        print("\n=========================================")
        print("          TRANSACTION STATEMENT          ")
        print("=========================================")
        if not self.transaction_history:
            print("No transactions performed during this session.")
        else:
            for idx, item in enumerate(self.transaction_history, 1):
                print(f"{idx}. {item}")
        print("-----------------------------------------")
        print(f"FINAL CLOSING BALANCE: ₹{self.account.balance:,.2f}")
        print("=========================================\n")

account = SavingAccount(acc_id="ACC101", name="John Doe", balance=15000.0, acc_type="Personal")
user = User(account)
user.run_menu()
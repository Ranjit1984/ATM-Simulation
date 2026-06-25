class Account:
    def __init__(self, acc_num, pin, balance=0.0):
        self.acc_num = acc_num
        self.pin = pin
        self.balance = float(balance)
        self.history = []  # List to track live session history


class ATMSystem:
    def __init__(self):
        # Dictionary of pre-existing accounts
        self.accounts = {
            "112233": Account("112233", "1234", 500.0),
            "445566": Account("445566", "5678", 1500.0)
        }
        self.log_file = "atm_logs.txt"

    def log_transaction(self, acc_num, message):
        with open(self.log_file, "a") as file:
            file.write(f"Account {acc_num}: {message}\n")

    def authenticate(self, acc_num, pin):
        if acc_num in self.accounts and self.accounts[acc_num].pin == pin:
            return self.accounts[acc_num]
        return None

    def start_atm(self, acc_num, pin):
        account = self.authenticate(acc_num, pin)
        if not account:
            print("❌ Invalid Account Number or PIN.")
            return

        print(f"\nWelcome, Account Holder {acc_num}!")

        while True:  # Control loop
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                print(f"Current Balance: ${account.balance:.2f}")
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                if amount > 0:
                    account.balance += amount
                    msg = f"Deposited ${amount:.2f}"
                    account.history.append(msg)
                    self.log_transaction(acc_num, msg)
                    print("Success!")
                else:
                    print("Invalid amount.")
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                if 0 < amount <= account.balance:  # Conditional validation
                    account.balance -= amount
                    msg = f"Withdrew ${amount:.2f}"
                    account.history.append(msg)
                    self.log_transaction(acc_num, msg)
                    print("Success!")
                else:
                    print("❌ Insufficient funds or invalid amount.")
            elif choice == "4":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid option selected.")


# --- Demonstration Run ---
if __name__ == "__main__":
    atm = ATMSystem()
    # Try logging in with Account: 112233, PIN: 1234
    atm.start_atm("112233", "1234")
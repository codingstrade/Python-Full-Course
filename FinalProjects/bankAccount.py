import os

balance_file = 'balance_file.txt'

class BankAccount:
    def __init__(self):
        if not os.path.exists(balance_file):
            with open(balance_file, 'w') as f:
                f.write('0')
        with open(balance_file,'r') as f:
            self.balance = float(f.read())

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount  # amount = balance + amount
        self.save_balance()
        print(f"Deposited {amount} successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount # amount = balance - amount
        self.save_balance()
        print(f"Withdraw {amount} successfully. Current balance: {self.balance}")

    def save_balance(self):
        with open(balance_file, 'w') as f:
            f.write(str(self.balance))

def main():
    account = BankAccount()

    while True:
        print("Select an Option")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Checkout")

        choice = input("> ")
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount you want to Withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance: {account.balance}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again")

if __name__ == '__main__':
    main()


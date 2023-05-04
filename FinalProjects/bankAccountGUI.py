"""
Tkinter is a standard GUI (Graphical User Interface) package for Python.
It is a built-in module in Python's standard library,
which allows Python programmers to create GUI applications with ease.
"""

import os
import tkinter as tk
from tkinter import simpledialog, messagebox
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
            messagebox.showerror("Invalid amount")
            return
        self.balance += amount  # amount = balance + amount
        self.save_balance()
        messagebox.showinfo(f"Deposited {amount} successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            messagebox.showerror("Invalid amount")
            return
        if amount > self.balance:
            messagebox.showerror("Insufficient balance")
            return
        self.balance -= amount # amount = balance - amount
        self.save_balance()
        messagebox.showinfo(f"Withdraw {amount} successfully. Current balance: {self.balance}")

    def save_balance(self):
        with open(balance_file, 'w') as f:
            f.write(str(self.balance))

class BankAccountGUI:
    def __init__(self, root):
        self.account = BankAccount()

        # create GUI Elements
        self.label = tk.Label(root, text=f"Current balance: {self.account.balance}")
        self.label.pack()

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

    def deposit(self):
        amount = float(simpledialog.askstring("Deposit","Enter the amount to deposit: "))
        if amount is not None:
            self.account.deposit(amount)
            self.label.config(text=f"Current balance: {self.account.balance}")

    def withdraw(self):
        amount = float(simpledialog.askstring("Withdraw","Enter the amount you want to withdraw: "))
        if amount is not None:
            self.account.withdraw(amount)
            self.label.config(text=f"Current balance: {self.account.balance}")




if __name__ == '__main__':
    root = tk.Tk()
    app = BankAccountGUI(root)
    root.mainloop()


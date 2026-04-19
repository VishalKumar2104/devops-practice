from flask import Flask, request, jsonify

app = Flask(__name__)

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print("Amount Deposited Successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def show_transactions(self):
        print("Transaction History:")
        for t in self.transactions:
            print(t)


# Storage (like HashMap in Java)
accounts = {}


def create_account():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in accounts:
        print("Username already exists!")
        return

    accounts[username] = Account(username, password)
    print("Account Created Successfully!")


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in accounts and accounts[username].password == password:
        print("Login Successful!")
        user_menu(accounts[username])
    else:
        print("Invalid Credentials!")


def user_menu(acc):
    while True:
        print("\n--- USER MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transactions")
        print("5. Logout")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if choice == 1:
            amount = float(input("Enter Amount: "))
            acc.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter Amount: "))
            acc.withdraw(amount)
        elif choice == 3:
            acc.check_balance()
        elif choice == 4:
            acc.show_transactions()
        elif choice == 5:
            return
        else:
            print("Invalid Choice!")


# MAIN PROGRAM
if __name__ == "__main__":
    while True:
        print("\n--- BANK SYSTEM ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if choice == 1:
            create_account()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

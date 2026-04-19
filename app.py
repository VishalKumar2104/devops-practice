from flask import Flask, request, jsonify

app = Flask(__name__)

# Account class
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.transactions = []

accounts = {}

# Home route
@app.route("/")
def home():
    return "Bank System Running on AWS 🚀"


# Create account
@app.route("/create", methods=["POST"])
def create_account():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if username in accounts:
        return jsonify({"msg": "User already exists"})

    accounts[username] = Account(username, password)
    return jsonify({"msg": "Account created successfully"})


# Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if username in accounts and accounts[username].password == password:
        return jsonify({"msg": "Login successful"})
    else:
        return jsonify({"msg": "Invalid credentials"})


# Deposit
@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()
    username = data["username"]
    amount = float(data["amount"])

    if username in accounts:
        acc = accounts[username]
        acc.balance += amount
        acc.transactions.append(f"Deposited {amount}")
        return jsonify({"msg": "Deposited", "balance": acc.balance})
    
    return jsonify({"msg": "User not found"})


# Withdraw
@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    username = data["username"]
    amount = float(data["amount"])

    if username in accounts:
        acc = accounts[username]
        if amount <= acc.balance:
            acc.balance -= amount
            acc.transactions.append(f"Withdrawn {amount}")
            return jsonify({"msg": "Withdrawn", "balance": acc.balance})
        else:
            return jsonify({"msg": "Insufficient balance"})
    
    return jsonify({"msg": "User not found"})


# Check balance
@app.route("/balance/<username>")
def balance(username):
    if username in accounts:
        return jsonify({"balance": accounts[username].balance})
    return jsonify({"msg": "User not found"})


# Transactions
@app.route("/transactions/<username>")
def transactions(username):
    if username in accounts:
        return jsonify(accounts[username].transactions)
    return jsonify({"msg": "User not found"})


# Run server on AWS
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

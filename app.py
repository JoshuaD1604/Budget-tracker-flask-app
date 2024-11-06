from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory data store
transactions = []

class Transaction:
    def __init__(self, date, category, amount, transaction_type):
        self.date = date
        self.category = category
        self.amount = amount
        self.transaction_type = transaction_type

    def __repr__(self):
        return f"Transaction({self.date}, {self.category}, {self.amount}, {self.transaction_type})"

@app.route('/')
def index():
    total_income = sum(t.amount for t in transactions if t.transaction_type == 'Income')
    total_expenses = sum(t.amount for t in transactions if t.transaction_type == 'Expense')
    balance = total_income - total_expenses

    return render_template('index.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, balance=balance)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction_type = request.form['transaction_type']
        category = request.form['category']
        amount = float(request.form['amount'])
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        transactions.append(Transaction(date=date, category=category, amount=amount, transaction_type=transaction_type))
        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)

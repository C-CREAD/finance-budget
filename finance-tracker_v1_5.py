import sqlite3
from flask import render_template, request, redirect, url_for, flash, Flask
from SECRET_KEYS import get_key

app = Flask(__name__)
app.config["SECRET_KEY"] = str(get_key())

# Create "finance_project.db" database
database = sqlite3.connect('data/finance_project.db')


def create_tables():
    """
    Creates the expense, income, and budget tables in the database.
    """
    # Create cursor object to execute queries
    cursor = database.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 
        Expenses(ID INTEGER PRIMARY KEY, Expense TEXT, Amount REAL, Category TEXT)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 
        Incomes(ID INTEGER PRIMARY KEY, Income TEXT, Amount REAL, Category TEXT)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 
        Budgets(ID INTEGER PRIMARY KEY, Budget TEXT, Amount REAL, 
        Remainder REAL, Remainder_Percentage REAL, Category TEXT)
    ''')

    # Save changes
    database.commit()

# Create Tables
create_tables()


@app.route('/')
@app.route('/home')
def index():
    """
    This function will render the homepage template i.e. index.html

    :return: Render template object
    """
    return render_template('index.html')


@app.route('/incomes')
def incomes():
    """
    This function will render the income page template (i.e. income.html)
    and display all the records from the income table, and the links to
    insert, update, and delete records from the income table

    :return: Render template object
    """
    with sqlite3.connect('data/finance_project.db') as connection:
        cursor = connection.cursor()
        all_records = cursor.execute('''SELECT * FROM Incomes''').fetchall()

        return render_template('incomes.html', incomes=all_records, title="Incomes")


@app.route('/incomes/add', methods=["GET", "POST"])
def insert_income():
    """
    This function will render the template to insert incomes
    into the database.

    :return: Render template object
    """
    with sqlite3.connect("data/finance_project.db") as connection:
        if request.method == "POST":
            income_name = request.form['name']
            income_amount = float(request.form['amount'])
            income_category = request.form['category']

            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO Incomes(Income, Amount, Category)
                VALUES(?, ?, ?)
            ''', (income_name, income_amount, income_category))

            # Save changes
            connection.commit()

            return redirect(url_for("incomes"))
        else:
            return render_template("insert income.html")


@app.route('/income/<int:income_ID>/update', methods=["GET", "POST"])
def update_income(income_ID):
    """
    This function will render the template to update income records
    from the database.

    :return: Render template object
    """

    with sqlite3.connect("data/finance_project.db") as connection:
        cursor = connection.cursor()
        income_record = cursor.execute(
            '''SELECT * FROM Incomes WHERE ID = ?''', (income_ID,)).fetchone()

        if request.method == "POST":
            income_name = request.form['name']
            income_amount = float(request.form['amount'])
            income_category = request.form['category']

            cursor.execute('''
                UPDATE Incomes SET Income = ?, Amount = ?, Category = ? WHERE ID = ?
            ''', (income_name, income_amount, income_category, income_ID, ))

            # Save changes
            connection.commit()

            # Display message and redirect to Incomes page
            flash("Income record updated successfully!")
            return redirect(url_for("incomes"))
        else:
            return render_template("update income.html", income_record=income_record)


@app.route('/income/<int:income_ID>/delete', methods=["GET", "POST"])
def delete_income(income_ID):
    """
    This function will render the template to delete income records
    from the database.

    :return: Render template object
    """

    with sqlite3.connect("data/finance_project.db") as connection:
        cursor = connection.cursor()
        income_record = cursor.execute(
            '''SELECT * FROM Incomes WHERE ID = ?''', (income_ID,)).fetchone()

        if request.method == "POST":
            cursor.execute('''
                DELETE FROM Incomes WHERE ID = ?''', (income_ID, ))

            # Save changes
            connection.commit()

            # Display message and redirect to Incomes page
            flash("Income record deleted successfully!")
            return redirect(url_for("incomes"))
        else:
            return render_template("delete income.html", income_record=income_record)

@app.route('/expenses/add', methods=["GET", "POST"])
def insert_expense():
    """
    This function will render the template to insert expenses
    into the database.

    :return: Render template object
    """
    with sqlite3.connect("data/finance_project.db") as connection:
        if request.method == "POST":
            expense_name = request.form['name']
            expense_amount = float(request.form['amount'])
            expense_category = request.form['category']

            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO Expenses(Expense, Amount, Category)
                VALUES(?, ?, ?)
            ''', (expense_name, expense_amount, expense_category))

            # Save changes
            connection.commit()

            return redirect(url_for("expenses"))
        else:
            return render_template("insert expense.html")


@app.route('/expense/<int:expense_ID>/update', methods=["GET", "POST"])
def update_expense(expense_ID):
    """
    This function will render the template to update expense records
    from the database.

    :return: Render template object
    """

    with sqlite3.connect("data/finance_project.db") as connection:
        cursor = connection.cursor()
        expense_record = cursor.execute(
            '''SELECT * FROM Expenses WHERE ID = ?''', (expense_ID,)).fetchone()

        if request.method == "POST":
            expense_name = request.form['name']
            expense_amount = float(request.form['amount'])
            expense_category = request.form['category']

            cursor.execute('''
                UPDATE Expenses SET Expense = ?, Amount = ?, Category = ? WHERE ID = ?
            ''', (expense_name, expense_amount, expense_category, expense_ID, ))

            # Save changes
            connection.commit()

            # Display message and redirect to Expense page
            flash("Expense record updated successfully!")
            return redirect(url_for("expenses"))
        else:
            return render_template("update expense.html", expense_record=expense_record)


@app.route('/expense/<int:expense_ID>/delete', methods=["GET", "POST"])
def delete_expense(expense_ID):
    """
    This function will render the template to delete income records
    from the database.

    :return: Render template object
    """

    with sqlite3.connect("data/finance_project.db") as connection:
        cursor = connection.cursor()
        expense_record = cursor.execute(
            '''SELECT * FROM Expenses WHERE ID = ?''', (expense_ID,)).fetchone()

        if request.method == "POST":
            cursor.execute('''
                DELETE FROM Expenses WHERE ID = ?''', (expense_ID, ))

            # Save changes
            connection.commit()

            # Display message and redirect to Incomes page
            flash("Income record deleted successfully!")
            return redirect(url_for("expenses"))
        else:
            return render_template("delete expense.html", expense_record=expense_record)


@app.route('/budgets')
def budgets():
    """
    This function will render the budget page template (i.e. budgets.html)
    and display all the records from the budget table and the links to
    insert and update records from the budget table

    :return: Render template object
    """
    with sqlite3.connect('data/finance_project.db') as connection:
        cursor = connection.cursor()
        all_records = cursor.execute('''SELECT * FROM Budgets''').fetchall()

        return render_template('budgets.html', budgets=all_records, title="Budgets")


@app.route('/budgets/add', methods=["GET", "POST"])
def insert_budget():
    """
    This function will render the template to insert budgets
    into the database.

    :return: Render template object
    """
    with sqlite3.connect("data/finance_project.db") as connection:
        if request.method == "POST":
            budget_name = request.form['name']
            budget_amount = float(request.form['amount'])
            budget_category = request.form['category']

            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO Budgets(Budget, Amount, Category)
                VALUES(?, ?, ?)
            ''', (budget_name, budget_amount, budget_category))

            # Save changes
            connection.commit()

            return redirect(url_for("budgets"))
        else:
            return render_template("insert budget.html")


@app.route('/budgets/<int:budget_ID>/update', methods=["GET", "POST"])
def update_budget(budget_ID):
    """
    This function will render the template to update budget records
    from the database.

    :return: Render template object
    """
    with sqlite3.connect("data/finance_project.db") as connection:
        cursor = connection.cursor()
        budget_record = cursor.execute(
            '''SELECT * FROM Budgets WHERE ID = ?''', (budget_ID,)).fetchone()

        print(budget_record)

        if request.method == "POST":
            budget_name = request.form['name']
            budget_amount = float(request.form['amount'])
            budget_category = request.form['category']

            cursor.execute('''
                UPDATE Budgets SET Budget = ?, Amount = ?, Category = ? WHERE ID = ?
            ''', (budget_name, budget_amount, budget_category, budget_ID,))

            cursor.execute('''
                UPDATE Budgets SET Remainder = Amount + 
                    (SELECT SUM(Amount) FROM Incomes WHERE Category = ?) - 
                    (SELECT SUM(Amount) FROM Expenses WHERE Category = ?)
                WHERE Category = ?''',
                           (budget_category, budget_category, budget_category))

            cursor.execute('''
            UPDATE Budgets SET Remainder_Percentage = 
                (SELECT ((Remainder / Amount)) FROM Budgets WHERE Category = ?)
            WHERE Category = ?''', (budget_category, budget_category))


            # Save Changes
            connection.commit()

            return redirect(url_for("budgets"))
        else:
            return render_template("update budget.html", budget_record=budget_record)


@app.route('/budgets/<int:budget_ID>/delete', methods=["GET", "POST"])
def delete_budget(budget_ID):
    """
    This function will render the template to delete budget records
    from the database.

    :return: Render template object
    """

    with sqlite3.connect("data/finance_project.db") as connection:
        cursor = connection.cursor()
        budget_record = cursor.execute(
            '''SELECT * FROM Budgets WHERE ID = ?''', (budget_ID,)).fetchone()

        if request.method == "POST":
            cursor.execute('''
                DELETE FROM Budgets WHERE ID = ?''', (budget_ID, ))

            # Save changes
            connection.commit()

            # Display message and redirect to Incomes page
            flash("Budget record deleted successfully!")
            return redirect(url_for("budgets"))
        else:
            return render_template("delete budget.html", budget_record=budget_record)


@app.route('/budgets/<int:budget_ID>')
def selected_budget(budget_ID):
    """
    This function will render all the information related to the selected
    budget record, such as:
    - incomes and expenses related by category
    - percentage increases/decreases of the remainder values from the initial budget

    :param budget_ID: Budget ID
    :return: Render template object
    """
    with sqlite3.connect("data/finance_project.db") as connection:
        cursor = connection.cursor()
        budget_record = cursor.execute('''SELECT * FROM Budgets WHERE ID = ?''',
                                       (budget_ID,)).fetchone()
        budget_category = budget_record[5]

        related_incomes = cursor.execute('''SELECT * FROM Incomes WHERE Category = ?''',
                                        (budget_category,)).fetchall()

        related_expenses = cursor.execute('''SELECT * FROM Expenses WHERE Category = ?''',
                                         (budget_category,)).fetchall()

        return render_template("advanced budget.html", budget_record=budget_record,
                               incomes=related_incomes, expenses=related_expenses)


if __name__ == "__main__":
    app.run(debug=True)

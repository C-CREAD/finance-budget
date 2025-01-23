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
    if request.method == "POST":
        income_name = request.form['name']
        income_amount = float(request.form['amount'])
        income_category = request.form['category']

        with sqlite3.connect("data/finance_project.db") as connection:
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

if __name__ == "__main__":
    app.run(debug=True)

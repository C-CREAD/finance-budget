import sqlite3
from tabulate import tabulate

# Create "finance_project.db" database
database = sqlite3.connect('data/finance_project.db')

# Create cursor object to execute queries
cursor = database.cursor()

# Currency symbol to represent amount values
currency_symbol = "R"


def create_tables():
    """
    Creates the expense, income, and budget tables in the database.
    """

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


def insert_expense():
    """
    This function will request the user to enter their expense information
    and the data will be inserted into the Expense table.
    """

    print("Please enter the following information for the expense below:")
    while True:
        try:
            expense_name = input("Expense Name: ")
            expense_amount = float(input(f"Expense Amount: {currency_symbol}"))
            expense_category = input("Expense Category: ")

            if expense_name == "" or expense_category == "":
                print("Invalid Entry!\nExpense Name and Category cannot be empty.")

            if expense_amount < 0:
                print(f"Invalid Entry!\nExpense Amount cannot be less than {currency_symbol}0.00")

            if expense_amount >= 0 and expense_name != "" and expense_category != "":
                cursor.execute('''
                    INSERT INTO Expenses(Expense, Amount, Category)
                    VALUES(?, ?, ?)
                ''', (expense_name, expense_amount, expense_category))

                # Save changes
                database.commit()
                break

        except ValueError:
            print(f"Invalid Entry!\nExpense Amount must be a number.\ne.g. {currency_symbol}50.4 or {currency_symbol}25")


def insert_income():
    """
    This function will request the user to enter their income information
    and the data will be inserted into the Income table.
    """

    print("Please enter the following information for the income below:")
    while True:
        try:
            income_name = input("income Name: ")
            income_amount = float(input(f"income Amount: {currency_symbol}"))
            income_category = input("income Category: ")

            if income_name == "" or income_category == "":
                print("Invalid Entry!\nincome Name and Category cannot be empty.")

            if income_amount < 0:
                print(f"Invalid Entry!\nincome Amount cannot be less than {currency_symbol}0.00")

            if income_amount >= 0 and income_name != "" and income_category !="":
                cursor.execute('''
                    INSERT INTO Incomes(Income, Amount, Category)
                    VALUES(?, ?, ?)
                ''', (income_name, income_amount, income_category))

                # Save changes
                database.commit()
                break

        except ValueError:
            print(f"Invalid Entry!\nIncome Amount must be a number.\ne.g. {currency_symbol}73.8 or {currency_symbol}38")


def insert_budget():
    """
    This function will request the user to enter their budget information
    and the data will be inserted into the Budget table.
    """

    print("Please enter the following information for the budget below:")
    while True:
        try:
            budget_name = input("Budget Name: ")
            budget_amount = float(input(f"Budget Amount: {currency_symbol}"))
            budget_category = input("Budget Category: ")

            if budget_name == "" or budget_category == "":
                print("Invalid Entry!\nBudget Name and Category cannot be empty.")

            if budget_amount < 0:
                print(f"Invalid Entry!\nBudget Limmit cannot be less than {currency_symbol}0.00")


            if budget_amount >= 0 and budget_name != "" and budget_category != "":
                cursor.execute('''
                    INSERT INTO Budgets(Budget, Amount, Category)
                    VALUES(?, ?, ?)
                ''', (budget_name, budget_amount, budget_category))

                # Save changes
                database.commit()
                break


        except ValueError:
            print(
                f"Invalid Entry!\nBudget Limit must be a number.\ne.g. {currency_symbol}50.4 or {currency_symbol}25")


def update_expense():
    """
    This function will update the expense values from the expense table
    """

    # Displaying all expense information in table format
    all_expenses = cursor.execute('''SELECT * FROM Expenses''')
    expense_table = tabulate(all_expenses, headers=["ID", "Expense", "Amount"],tablefmt="grid")
    print(expense_table)

    # Fetch Valid IDs
    all_IDs = cursor.execute('''SELECT ID FROM Expenses''')

    try:
        print("Please select an expense to update by ID:")
        select_ID = int(input("ID: "))

        if (select_ID,) not in all_IDs.fetchall():
            print("Invalid Entry!\nThis ID does not exist.")
            print("Try to create a new budget category first before updating it.")
        else:
            print("Select the following options to update: (Numbers Only)"
                  "\n1. Expense\n2. Amount\n3. Category\n")
            option = input(": ")

            # Update Expense Name
            if option == "1" or option == "1." or option.capitalize() == "Expense" or option == "1. Expense":
                expense_name = input("Enter new expense name: ")

                if expense_name == "":
                    print("Invalid Entry!\nExpense Name cannot be empty.")
                else:
                    cursor.execute('''
                        UPDATE Expenses SET Income = ? WHERE ID = ?
                    ''', (expense_name, select_ID))

            # Update Expense Amount
            elif option == "2" or option == "2." or option.capitalize() == "Amount" or option == "2. Amount":
                try:
                    amount = float(input("Enter new expense amount: "))

                    if amount < 0:
                        print(f"Invalid Entry!\nExpense Amount cannot be less than {currency_symbol}0.00")

                    else:
                        cursor.execute('''
                            UPDATE Expenses SET Amount = ? WHERE ID = ?
                        ''', (amount, select_ID))

                        # Fetch the category of updated record
                        category = cursor.execute('''SELECT Category FROM Expenses WHERE ID = ?''',
                                                      (select_ID,)).fetchone()[0]

                        # Update Budget records to reflect changes made from Incomes amounts ⬇️
                        cursor.execute('''
                                    UPDATE Budget SET Remainder = 
                                    (Amount - ABS((SELECT SUM(Amount) FROM Incomes WHERE Category Like ?) - 
                                    (SELECT SUM(Amount) FROM Expenses WHERE Category = ?))) WHERE Category LIKE ?
                                    ''', (category, category, category))

                        cursor.execute('''
                                    UPDATE Budgets SET Remainder_Percentage = 
                                    (SELECT (SUM(Remainder) / Amount) AS PERCENTAGE FROM Budgets WHERE Category LIKE ?)
                                    WHERE Category Like ?''',(category, category,))

                # Catch invalid user input
                except ValueError:
                    print(f"Invalid Entry!\nIncome Amount must be a number. e.g. {currency_symbol}55.78")

            # Update Expense Category
            elif option == "3" or option == "3." or option.capitalize() == "Category" or option == "3. Category":

                # Fetch old category before updating it
                old_category = cursor.execute('''SELECT Category FROM Income WHERE ID = ?''',
                               (select_ID,)).fetchone()[0]

                # Set new category
                new_category = input("Enter new expense category: ")
                cursor.execute('''
                    UPDATE Expenses SET Category = ? WHERE ID = ?
                ''', (new_category, select_ID))

                # Update Budget records to reflect changed category, based on old category
                cursor.execute('''
                UPDATE Budgets SET Category = ? WHERE Category = ?''',
                               (new_category, old_category))

            else:
                print("Invalid Entry!\nPlease select the three valid options")

            # Save Changes
            database.commit()

    except ValueError:
        print("Invalid Entry!\nID must be a number.")


def update_income():
    """
    This function will update the income values from the income table
    """

    # Displaying all income information in table format
    all_incomes = cursor.execute('''SELECT * FROM Incomes''')
    income_table = tabulate(all_incomes, headers=["ID", "Income", "Amount"],tablefmt="grid")
    print(income_table)

    # Fetch Valid IDs
    all_IDs = cursor.execute('''SELECT ID FROM Incomes''')

    try:
        print("Please select an income to update by ID:")
        select_ID = int(input("ID: "))

        if (select_ID,) not in all_IDs.fetchall():
            print("Invalid Entry!\nThis ID does not exist.")
            print("Try to create a new budget category first before updating it.")
        else:
            print("Select the following options to update: (Numbers Only)"
                  "\n1. Income\n2. Amount\n3. Category\n")
            option = input(": ")

            # Update Income Name
            if option == "1" or option == "1." or option.capitalize() == "Income" or option == "1. Income":
                income_name = input("Enter new income name: ")

                if income_name == "":
                    print("Invalid Entry!\nExpense Name cannot be empty.")
                else:
                    cursor.execute('''
                        UPDATE Incomes SET Income = ? WHERE ID = ?
                    ''', (income_name, select_ID))

            # Update Income Amount
            elif option == "2" or option == "2." or option.capitalize() == "Amount" or option == "2. Amount":
                try:
                    amount = float(input("Enter new income amount: "))

                    if amount < 0:
                        print(f"Invalid Entry!\nExpense Amount cannot be less than {currency_symbol}0.00")

                    else:
                        cursor.execute('''
                            UPDATE Incomes SET Amount = ? WHERE ID = ?
                        ''', (amount, select_ID))

                        # Fetch the category of updated record
                        category = cursor.execute('''SELECT Category FROM Incomes WHERE ID = ?''',
                                                      (select_ID,)).fetchone()[0]

                        # Update Budget records to reflect changes made from Incomes amounts ⬇️
                        cursor.execute('''
                                    UPDATE Budgets SET Remainder = 
                                    (Amount - ABS((SELECT SUM(Amount) FROM Incomes WHERE Category Like ?) - 
                                    (SELECT SUM(Amount) FROM Expenses WHERE Category = ?))) WHERE Category LIKE ?
                                    ''', (category, category, category))

                        cursor.execute('''
                                    UPDATE Budgets SET Remainder_Percentage = 
                                    (SELECT (SUM(Remainder) / Amount) AS PERCENTAGE FROM Budgets WHERE Category LIKE ?)
                                    WHERE Category Like ?''', (category, category,))

                # Catch invalid user input
                except ValueError:
                    print(f"Invalid Entry!\nIncome Amount must be a number. e.g. {currency_symbol}55.78")

            # Update Income Category
            elif option == "3" or option == "3." or option.capitalize() == "Category" or option == "3. Category":

                # Fetch old category before updating it
                old_category = cursor.execute('''SELECT Category FROM Incomes WHERE ID = ?''',
                               (select_ID,)).fetchone()[0]

                # Set new category
                new_category = input("Enter new income category: ")
                cursor.execute('''
                    UPDATE Incomes SET Category = ? WHERE ID = ?
                ''', (new_category, select_ID))

                # Update Budget records to reflect changed category, based on old category
                cursor.execute('''
                UPDATE Budgets SET Category = ? WHERE Category = ?''',
                               (new_category, old_category))

            else:
                print("Invalid Entry!\nPlease select the three valid options")

            # Save Changes
            database.commit()

    except ValueError:
        print("Invalid Entry!\nID must be a number.")


def update_budget():
    """
    This function will update the remainder values and remainder percentages
    from the budget table in case the user has not added the corresponding
    incomes and expenses with the same category.
    """

    # Displaying all budget information in table format
    all_budgets = cursor.execute('''SELECT * FROM Budgets''')
    budget_table = tabulate(all_budgets, headers=["ID", "Budget", "Amount",
                                                  "Remainder", "Remainder Percentage", "Category"],
                            tablefmt="grid")
    print(budget_table)

    # Fetch Categories
    all_categories = cursor.execute('''SELECT Category FROM Budgets''')

    print("Please enter the existing category you would like to update:")
    update_category = input("Category: ")

    if (f"{update_category}",) not in all_categories.fetchall():
        print(f"Invalid Entry!\nThe category '{update_category}' does not exist.")
        print("Try to create a new budget category first before updating it.")
    else:
        cursor.execute('''
        UPDATE Budgets SET Remainder = 
        (Amount - ABS((SELECT SUM(Amount) FROM Incomes WHERE Category Like ?) - 
        (SELECT SUM(Amount) FROM Expenses WHERE Category = ?))) WHERE Category LIKE ?''',
                        (update_category, update_category, update_category))

        cursor.execute('''
        UPDATE Budgets SET Remainder_Percentage = 
        (SELECT (SUM(Remainder) / Amount) AS PERCENTAGE FROM Budgets WHERE Category LIKE ?)
        WHERE Category Like ?''', (update_category, update_category,))

        results = cursor.execute(''' SELECT * FROM Budgets WHERE Category = ?
        ''', (update_category))

        result_table = tabulate(results, headers=["ID", "Budget", "Amount",
                                                      "Remainder", "Remainder Percentage", "Category"],
                                tablefmt="grid")
        print(result_table)

        # Save Changes
        database.commit()


def delete_expense():
    """
    This function will delete specific records from the Expense table
    """

    # Displaying all expense information in table format
    all_expenses = cursor.execute('''SELECT * FROM Expenses''')
    expense_table = tabulate(all_expenses, headers=["ID", "Expense", "Amount"], tablefmt="grid")
    print(expense_table)

    # Fetch Valid IDs
    all_IDs = cursor.execute('''SELECT ID FROM Expenses''')

    try:
        print("Please enter the expense you wish to delete")
        select_ID = int(input("Expense ID: "))

        if (select_ID,) not in all_IDs.fetchall():
                print("Invalid Entry!\nThis ID does not exist.")
                print("Please try again.")
        else:
            print("ID:", select_ID, "found")
            print("Confirm Deletion?\n 1. Yes\n2. No")
            option = input(": ")

            if option == "1" or option == "1." or option.capitalize() == "Yes" or option == "1. Yes":
                cursor.execute('''
                DELETE FROM Expenses WHERE ID = ?''', (select_ID,))

                # Save Changes
                database.commit()
                print("Expense Deleted")

            elif option == "2" or option == "2." or option.capitalize() == "No" or option == "2. No":
                print("Deletion Cancelled.")

            else:
                print("Invalid Entry!\nPlease select the two valid options")

    except ValueError:
        print("Invalid Entry!\nID must be a number.")


def delete_income():
    """
    This function will delete specific records from the Income table
    """

    # Displaying all income information in table format
    all_incomes = cursor.execute('''SELECT * FROM Incomes''')
    income_table = tabulate(all_incomes, headers=["ID", "Expense", "Amount", "Category"], tablefmt="grid")
    print(income_table)

    # Fetch Valid IDs
    all_IDs = cursor.execute('''SELECT ID FROM Incomes''')

    try:
        print("Please enter the income you wish to delete")
        select_ID = int(input("Expense ID: "))

        if (select_ID,) not in all_IDs.fetchall():
            print("Invalid Entry!\nThis ID does not exist.")
            print("Please try again.")
        else:
            print("ID:", select_ID, "found")
            print("Confirm Deletion?\n 1. Yes\n2. No")
            option = input(": ")

            if option == "1" or option == "1." or option.capitalize() == "Yes" or option == "1. Yes":
                cursor.execute('''
                DELETE FROM Incomes WHERE ID = ?''', (select_ID,))

                # Save Changes
                database.commit()
                print("Income Deleted")

            elif option == "2" or option == "2." or option.capitalize() == "No" or option == "2. No":
                print("Deletion Cancelled.")

            else:
                print("Invalid Entry!\nPlease select the two valid options")

    except ValueError:
        print("Invalid Entry!\nID must be a number.")


def view_table():
    """
    This function will view all the tables in the database
    """

    print("Please select between these tables to display:\n"
          "1. Income\n2. Expense\n3. Budget\n")
    option = input(": ")

    # Displaying all income information in table format
    if option == "1" or option == "1." or option.capitalize() == "Income" or option == "1. Income":

        all_incomes = cursor.execute('''SELECT * FROM Incomes''')
        income_table = tabulate(all_incomes, headers=["ID", "Income", "Amount", "Category"], tablefmt="grid")
        print(income_table)

    # Displaying all expense information in table format
    elif option == "2" or option == "2." or option.capitalize() == "Expense" or option == "2. Expense":

        all_expenses = cursor.execute('''SELECT * FROM Expenses''')
        expense_table = tabulate(all_expenses, headers=["ID", "Expense", "Amount", "Category"], tablefmt="grid")
        print(expense_table)

    # Displaying all budget information in table format
    elif option == "3" or option == "3." or option.capitalize() == "Budget" or option == "3. Budget":

        all_budgets = cursor.execute('''SELECT * FROM Budgets''')
        budget_table = tabulate(all_budgets, headers=["ID", "Budget", "Amount",
                                                      "Remainder", "Remainder Percentage", "Category"],
                                tablefmt="grid")
        print(budget_table)

    else:
        print("Invalid Entry!\nPlease select the three valid options")


def main():
    """
    Main function to run the program.
    """
    print("----WELCOME TO FINANCIAL TRACKER!----\n\n")

    print("Please select an option: (Numbers Only)\n"
          "1. Add a new Income\n"
          "2. Update existing Income\n"
          "3. Delete existing Income\n"
          "\n"
          "4. Add a new expense\n"
          "5. Update existing expense\n"
          "6. Delete existing expense\n"
          "\n"
          "7. Add a new Budget\n"
          "8 Update existing Budget\n"
          "\n"
          "9. View Tables\n"
          "\n"
          "0. Exit Application")

    # Create the tables before running the application:
    create_tables()
    while True:
        try:
            user_input = int(input(": "))

            if user_input == 0:
                print("Exiting Program...Thank You.")
                break
            elif user_input == 1:
                insert_income()
            elif user_input == 2:
                update_income()
            elif user_input == 3:
                delete_income()
            elif user_input == 4:
                insert_expense()
            elif user_input == 5:
                update_expense()
            elif user_input == 6:
                delete_expense()
            elif user_input == 7:
                insert_budget()
            elif user_input == 8:
                update_budget()
            elif user_input == 9:
                view_table()

        except ValueError:
            print(f"Invalid Entry!\nPlease enter the numbers only between 0 - 11.")

# Run Program
main()
# Finance Budget Tracker (Terminal Version)
This is my Python mini-project that represents a financial budget tracker.


## Description
This terminal mini-project lets users create different incomes, expenses, and budgets using Python and SQLite. 
The user can create, update, and delete incomes and expenses but can only create and update budgets. The user can also view the incomes, expenses, and budgets in a table format for neatness and readability.
Each income and expense will have its amounts and categories, while the budget will have an initial amount and calculated remainder amount and percentage based on the net income of incomes and expenses that share the same category. 

To visit the Flask variation of this project, go to the v1.5 branch or click [here](https://github.com/C-CREAD/finance-budget/tree/v1.5).

## Installation
To install this project on your computer, follow the instructions below:
1. Create a directory (folder) where you wish to install the project.
2. Open your terminal/command prompt and navigate to the selected directory
3. In this directory, type the following command:
     ```sh
     git clone https://github.com/C-CREAD/finance-budget
     ```
4. Navigate to the project folder inside the directory from above:
     ```sh
     cd (folder)
     ```
5. Run the program using the following command:
     ```sh
     python finance-tracker.py 
     ```



## Use Cases

0. Welcome Menu
   When running the program, the user will see the following menu options:
     1. Add a new Income
     2. Update existing Income
     3. Delete existing Income

     4. Add a new expense
     5. Update existing expense
     6. Delete existing expense

     7. Add a new Budget
     8. Update existing Budget

     9. View Tables

     0. Exit Application

![image](https://github.com/user-attachments/assets/b2d249dd-d886-4fb5-8b6a-233e31661753)


2. Creating Incomes and Expenses
   To add a new income/expense, the user will need to enter the name of the income/expense, the amount of money, and the category of the record.

![image](https://github.com/user-attachments/assets/82d22e72-9f38-4b2c-b68a-c0b6b9924079)
![image](https://github.com/user-attachments/assets/4aae5dd8-fd40-4b3a-8c4b-6c5077d4883c)


4. Updating Incomes and Expenses
   To update the income/expense, the user must enter the ID number of the record. A table will display all valid records to choose from.

![image](https://github.com/user-attachments/assets/d9015cd1-2f73-412e-84ea-2ac3d926074f)
![image](https://github.com/user-attachments/assets/4e354fe9-58e6-473f-85f8-3dc92922c5fe)


6. Deleting Incomes and Expenses
   To delete the income/expense, the user must enter the ID number of the record. A table will display all valid records to choose from.

![image](https://github.com/user-attachments/assets/31b1bd53-e788-4eba-8455-ca3baa17ff89)
![image](https://github.com/user-attachments/assets/10efe2ee-103e-4d18-865f-1f4b2e239066)

   
8. Creating Budgets
   To add a new budget, the user will need to enter the budget name, the amount of money, and the category of the record.
   (NOTE: The Remainder Amounts and Percentages will be calculated once the record is updated)

![image](https://github.com/user-attachments/assets/0330a983-c184-48b3-bb23-e1389088b911)

10. Updating Budgets
   To update the budget, the user must enter a valid category from the budget table. The remainder amounts and percentages will be calculated based on the net income of the incomes and expenses that share the same category.
   For example:
   Income M = 1000   &   Expense M = 850
   Net Income M = Income M - Expense M = 150

   Therefore, 
   Budget M Amount - Net Income M = 1500 - 150 = 1350 

![image](https://github.com/user-attachments/assets/3a9ae3f6-2b25-4a0b-85f3-25a809218922)
    

12. Viewing Incomes, Expenses, and Budgets
    To view all the incomes, expenses, and budgets, the user must select the options provided to them below.

![image](https://github.com/user-attachments/assets/c8b39f6c-c614-4b03-839d-707ccbcb1976)

Income Table:

![image](https://github.com/user-attachments/assets/a058f742-85b3-489c-b60c-9f75595d9479)

Expense Table:

![image](https://github.com/user-attachments/assets/4b27ff19-800c-4c83-a259-6eac68fa926f)

Budget Table:

![image](https://github.com/user-attachments/assets/0ed0ee51-633c-4552-9018-78bba35759ea)
    
Credit: 
Shingai Dzinotyiweyi

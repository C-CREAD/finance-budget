# Finance Budget Tracker (v1.5 Flask)
This is my Python mini-project that represents a financial budget tracker using the Flask framework.


## Description
This full-stack development mini-project lets users create incomes, expenses, and budgets using Python, Flask, and SQLite. 
The user can create/update/delete/view incomes, expenses, and budgets.

## Installation
### Git Repo
To install this project on your computer, follow the instructions below:
1. Create a directory (folder_name) where you wish to install the project.
2. Open your terminal/command prompt and navigate to the selected directory
3. In this directory, type the following command:
     ```sh
     git clone https://github.com/C-CREAD/finance-budget
     ```
4. Navigate to the project folder inside the directory from above:
     ```sh
     cd (folder_name)
     ```
5. Create a virtual environment:
     ```sh
     python -m venv .venv  
     ```
6. Install the required packages:
     ```sh
     pip install -r requirements.txt
     ```
7. Run the program using the following command:
     ```sh
     python finance-tracker.py 
     ```

## Use Cases
You can run the python file directly, then in your terminal, click on the following local host link: 
     ```
     http://127.0.0.1:5000
     ```
     ![image](https://github.com/user-attachments/assets/ea87e40a-8ba9-49d9-956b-2d4a415c8516)


0. Home Page
   The following links will be shown on your browser:
     - Incomes
     - Expenses
     - Budgets


1. Creating Incomes, Expenses, and Budgets
   To add a new income/expense/budget, you must enter the name of the income/expense/budget, the amount of money, and the category of the record.



2. Updating Incomes, Expenses, and Budgets
   To update the income/expense/budget, you must click on the green update button, and then enter the change the existing details in the textboxes. If you wish to not change anything, you can click on the update button without changing the existing details.
   


3. Deleting Incomes, Expenses, and Budgets
   To delete the income/expense/budget, you must click on the red delete button. A confirmation message will ask if you want to confirm the deletion before proceeding. 


### Docker
The docker repository containing the image can be found [here](https://hub.docker.com/repository/docker/ccread/flask_v1_5/general)
To run the Dockerfile of this project, make sure that you have Docker Desktop installed on your computer before proceeding or you can try to run the project on Docker Playground [here](https://labs.play-with-docker.com/). 

#### Docker Desktop
Once Docker Desktop is installed, follow the instructions below:
1. Create a directory (folder_name) where you wish to install the project.
2. Open your terminal/command prompt and navigate to the selected directory
3. In the directory, type the following command to pull the image from the repository:
     ```sh
     docker pull ccread/flask_v1_5:latest
     ```
4. Run the docker image:
     ```sh
     docker run -d -p 3000:3000 ccread/flask_v1_5:latest
     ```
     ![image](https://github.com/user-attachments/assets/08b66f0d-2a71-483c-858a-d719e7b5ba54)

   In your Docker Desktop, you will see the container of the image running. Click on the port 3000:3000 to be redirected to your browser.
     ![image](https://github.com/user-attachments/assets/1722b9e4-42b1-49de-b81e-f173750373ea)

   Alternatively, you can still go to your browser and enter this link:
     ```
     http://localhost:3000/
     ```

#### Docker Playground
1. To pull the docker image:
     ```sh
     docker pull ccread/flask_v1_5:latest
     ```
     ![image](https://github.com/user-attachments/assets/b337bb1a-8f21-4b71-959b-f40882be50e0)
     ![image](https://github.com/user-attachments/assets/9ac42364-99b7-4d08-bb8f-797e0dc28ff0)
2. Run the docker image:
     ```sh
     docker run -d -p 3000:3000 ccread/flask_v1_5:latest
     ```
     ![image](https://github.com/user-attachments/assets/ffb9ccbf-b951-4ee5-9e87-5a41d1467b27)

3. Click on the opened port: 3000
     ![image](https://github.com/user-attachments/assets/3283e78e-8075-40dc-89e9-1fdc2bba1908)

   If you don't see a port opened, click on the "Open Port" button and enter 3000 in the prompt given by your browser. 
     ![image](https://github.com/user-attachments/assets/655748f3-c0b5-43da-b565-214583582d27)

   You should be redirected to a new tab with the image running the project.
     ![image](https://github.com/user-attachments/assets/4457d7d7-e004-40d7-b604-90d127fd1738)


## Improvements from the original terminal program:
- The user can now delete budget records from the database
- The user can now display advanced statistics of each budget record, such as:
     1. Percentage Increase/Decrease of the Remainder Amount from the Initial Amount
     2. Display all incomes and expenses related to the budget by category  

    
Credit: 
Shingai Dzinotyiweyi

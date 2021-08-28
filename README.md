# Expense-Tracker-Desktop-App
This repository contains an expense tracker application developed in python 3.9.5, with win10 GUI front-end built with pyQt 5.9.2.

This application enables the user to define different accounts, as well as establish households for combined expense tracking. It automatically classifies transactions based on the statement description. The program either reads in manually-entered transaction statements from the user, or can import bulk transaction statements downloaded from online banking platforms as csv files. Future improvements may include an API with online banking platform for automated expense classification and tracking.

Transactions are classified based on an existing repository of transaction statements (“a category index” in database format (SQLite3) using a basic search/match algorithm. The user is prompted to enter new transactions statements into the database if it is not found to improve the strength of the classification algorithm depending on the user’s spending patterns. There are opportunities to incorporate the use of machine learning algorithms rather than the simple search/match algorithm to classify transactions.
In the back-end, the program utilizes pandas for data grouping and analysis. In the results window, the user is able to view spending categories by month and by year. Options are available to export and plot the data.

Additional utilities that are provided include the ability to add more accounts/users, add/delete expense categories.
This program will create a folder directory in your computer’s desktop directory, and will store databases, plots, queries and other files required to operate the program.

A list of dependencies in the conda development environment is included in the repository. To access the main program from the python interpreter of your choice, open and run the file titled "DM_expense_tracker_v1.0". No other .py files should be required to open/run to use the program as intended. Furthermore, for those who may not wish to use python interpreter to use the application, a standalone executable (built using CXFreeze 6.6) is available upon request (the file size is too large for upload to the repository).

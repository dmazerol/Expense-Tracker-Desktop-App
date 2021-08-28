# -*- coding: utf-8 -*-
"""

Version 1.0 - Release date July 5th, 2021

@author: Dillon Mazerolle
"""

'''Importing Modules and definining Methods and Global Variables'''

#functional modules
import os
import datetime as dt
import string
import sys
import sqlite3
from sqlite3 import OperationalError
from collections import Counter

#Modules related to data processing and plotting
import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
pd.set_option('mode.chained_assignment', None)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import scipy.spatial.transform._rotation_groups #This is only included to satisfy cx_Freeze during .exe build


#Local modules related to program functionality
from local_stopwords import stopwords
from TransactionClassifier import KeywordClassifier

#UI windows
from UI_v1.mainwindow import Ui_MainWindow
from UI_v1.resultsForm import Ui_Form
from UI_v1.add_user import Ui_AddUser
from UI_v1.MessageBox import Ui_MessageBox
from UI_v1.AddTransactionS import Ui_window_addTransactionS
from UI_v1.AddTransaction import Ui_window_addTransaction
from qtpy import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QFileDialog
bold_font=QtGui.QFont()
bold_font.setBold(True)


aspect_ratio = 16/9 #conventional aspect ratio of 15" laptop screen


def text_processor(description, bow = True):
    '''
    Converts a general string bank description to a bag of words

    Parameters
    ----------
    description : TYPE string
        DESCRIPTION. Bank statement to convert to bag of words
    bow : TYPE, boolean, optional
        DESCRIPTION. True if desired to return bag of words. False to return string. 
        The default is True.

    Returns A list (bag of words) or a string
    -------
    None.

    '''

    # stop_words = stopwords.words('english')
    stop_words = stopwords
    other_stopwords = ['ottawa', 'toronto', 'ottaw', 'nepean', 'orleans', 'fpos', 'pc', 
                       'scotia', 'rbc', 'infinite', 'momentum', 'visa', 'www', 'payment']
    
    for word in other_stopwords:
        stop_words.append(word)
    
    punc_num = string.punctuation + "0123456789"
    no_punc = [c for c in str(description) if c not in punc_num]
    no_punc = ''.join(no_punc)
    if bow == False:
        return " ".join([word for word in no_punc.split() if word.lower() not in stop_words])   
    else:
        return [word for word in no_punc.split() if word.lower() not in stop_words]

'''Setting up application folder on local desktop'''

#Verifying if local area on desktop has folder for saving data, if not, will create one
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
if os.path.exists(os.path.join(desktop, "DM_Expense_Tracker")) == False:
    os.mkdir(os.path.join(desktop, "DM_Expense_Tracker"))

parentfolder = os.path.join(desktop, "DM_Expense_Tracker")

if os.path.exists(os.path.join(parentfolder, "Data")) == False:
    os.mkdir(os.path.join(parentfolder, "Data"))
    
datafolder = os.path.join(parentfolder, "Data")

if os.path.exists(os.path.join(parentfolder, "Plots")) == False:
    os.mkdir(os.path.join(parentfolder, "Plots"))
    
plotfolder = os.path.join(parentfolder, "Plots")

if os.path.exists(os.path.join(parentfolder, "Statements")) == False:
    os.mkdir(os.path.join(parentfolder, "Statements"))
    
statements_folder = os.path.join(parentfolder, "Statements")

if os.path.exists(os.path.join(parentfolder, "z_admin")) == False:
    os.mkdir(os.path.join(parentfolder, "z_admin"))
    
admin_folder = os.path.join(parentfolder, "z_admin")
    
if os.path.exists(os.path.join(statements_folder, 'csv_transactions_backup')) == False:
    os.mkdir(os.path.join(statements_folder, 'csv_transactions_backup'))

trans_backup_folder = os.path.join(statements_folder, 'csv_transactions_backup')
    

if os.path.exists(os.path.join(parentfolder, 'troubleshooting')) == False:
    os.mkdir(os.path.join(parentfolder, 'troubleshooting'))

troubleshooting_folder = os.path.join(parentfolder, 'troubleshooting')

'''Setting up databases in the local folders if not already set up'''

#starting with a blank user list with zero entries, the user will need to add them
if os.path.exists(os.path.join(admin_folder, "user_list.db")) == False:
    con = sqlite3.connect(os.path.join(admin_folder, "user_list.db"))
    c = con.cursor()
    c.execute('''CREATE TABLE users
               (Name text, Household text)''')
               
    con.commit()
    con.close()

#setting up a base expense "types" database. Used to more quickly assign an expense in certain cases
if os.path.exists(os.path.join(admin_folder, "type_index.db")) == False:
    con = sqlite3.connect(os.path.join(admin_folder, "type_index.db"))
    c = con.cursor()
    c.execute('''CREATE TABLE types
                  (Category text, Type text)''')
                  
    types = [('taxes_fees', 'service charge'),
             ('income', 'payroll deposit'),
             ('taxes_fees', 'Overdraft Protect. Fee '),
             ('income', 'federal payment'),
             ('misc_transfers', 'customer cheques'),
             ('taxes_fees', 'tax refund'),
             ('housing_extras', 'FEES/DUES'),
             ('it', 'CABLE TV BILL PMT'),
             ('insurance', 'insurance'),
             ('misc_transfers', 'bill payment')]
    c.executemany('INSERT INTO types VALUES (?, ?)', types)
    con.commit()
    con.close()
    
#The category index is the respotiry of keywords used to classify transactions based on statement description
if os.path.exists(os.path.join(admin_folder, "category_index.db")) == False:
    con = sqlite3.connect(os.path.join(admin_folder, "category_index.db"))
    c = con.cursor()
    c.execute('''CREATE TABLE categories
                  (Category text, Statement text)''')
                  
    from categories import base_categories
    c.executemany('INSERT INTO categories VALUES (?, ?)', base_categories)
    con.commit()
    con.close()
    
#Expense type refers to variable, fixed, etc. Used to calculate certain spending metrics
if os.path.exists(os.path.join(admin_folder, "expense_type_index.db")) == False:
    con = sqlite3.connect(os.path.join(admin_folder, "expense_type_index.db"))
    c = con.cursor()
    c.execute('''CREATE TABLE expense_type
                  (Category text, ExpenseType text)''')
                  
    from categories import base_expense_type
    c.executemany('INSERT INTO expense_type VALUES (?, ?)', base_expense_type)
    con.commit()
    con.close()
 

'''Establishing class used for database manipulation'''  
class request_db():
    def __init__(self, db_filename):
        self.db_filename = db_filename
        
    def fetch_all(self, table_name):
        '''
        Returns a list of rows (as tuples) of the table in the database that is specified

        Parameters
        ----------
        table_name : TYPE String
            DESCRIPTION. Name of the table in the database

        Returns
        -------
        temp : TYPE List
            DESCRIPTION. Has format [(row 1 col 1, row 1 col 2), ...]

        '''
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()
        
        #Below is not ideal since it leaves the database open to corruption or "injection attacks"
        # if sql_statement != None:
        temp = self.c.execute('SELECT * FROM {}'.format(table_name)).fetchall()

         
        self.conn.close()
        return temp
    
    
    def get_users(self, sql_override=False, sql_statement = None, sql_var = None):
        '''
        Returns current list of users in the admin db user_list

        Parameters
        ----------
        sql_override : TYPE Boolean, optional
            DESCRIPTION. Allows user to enter custom SQL statement if set to TRUE. The default is False.
        sql_statement : TYPE string, optional
            DESCRIPTION. The SQL statement if sql_override set to TRUE. The default is None.
        sql_var : TYPE string, optional
            DESCRIPTION. simple filter critera for SQL selection. The default is None.

        Returns
        -------
        user_list : TYPE
            DESCRIPTION.

        '''
        
        self.conn = sqlite3.connect(os.path.join(admin_folder, self.db_filename))
        self.c = self.conn.cursor()
        user_list = []
        if sql_override == True:
            if sql_var != None:
                for row in self.c.execute(sql_statement, sql_var):
                    user_list.append(row[0])
            else:
                for row in self.c.execute(sql_statement):
                    user_list.append(row[0])
        else:
            for row in self.c.execute("SELECT Name FROM users"):
                user_list.append(row[0])
                
        self.conn.close()
        
        return user_list    
        
    
    def get_households(self, sql_override=False, sql_statement = None, sql_var = None):
        
        '''
        Returns current list of distinct households in the admin db user_list

        Parameters
        ----------
        sql_override : TYPE Boolean, optional
            DESCRIPTION. Allows user to enter custom SQL statement if set to TRUE. The default is False.
        sql_statement : TYPE string, optional
            DESCRIPTION. The SQL statement if sql_override set to TRUE. The default is None.
        sql_var : TYPE string, optional
            DESCRIPTION. simple filter critera for SQL selection. The default is None.

        Returns
        -------
        user_list : TYPE
            DESCRIPTION.

        '''
        self.conn = sqlite3.connect(os.path.join(admin_folder, self.db_filename))
        self.c = self.conn.cursor()
        
        household_list = []
        if sql_override == True:
            if sql_var != None:
               for row in self.c.execute(sql_statement, (sql_var,)):
                household_list.append(row[0])
            else:
                for row in self.c.execute(sql_statement):
                    household_list.append(row[0])
        else:
            for row in self.c.execute("SELECT DISTINCT Household FROM users"):
                household_list.append(row[0])
                
        self.conn.close()
        
        return household_list
    
    def get_transactions(self, user_var, sql_override=False, sql_statement = None, sql_var = None):
        '''
        Request statements from database file in pandas dataframe format to be used for analysis

        Parameters
        ----------
        user_var : TYPE string
            DESCRIPTION. The user name to be written to the database
        sql_override : TYPE Boolean, optional
            DESCRIPTION. Allows user to enter custom SQL statement if set to TRUE. The default is False.
        sql_statement : TYPE string, optional
            DESCRIPTION. The SQL statement if sql_override set to TRUE. The default is None.
        sql_var : TYPE string, optional
            DESCRIPTION. simple filter critera for SQL selection. The default is None.

        Returns dataframe over statements for a user
        -------
        user_list : TYPE
            DESCRIPTION.

        '''
        
        self.conn = sqlite3.connect(self.db_filename)
        
        self.c = self.conn.cursor()
        user_list = []
        if sql_override == True:
            if sql_var != None:
                for row in self.c.execute(sql_statement, sql_var):
                    user_list.append(row)
            else:
                for row in self.c.execute(sql_statement):
                    user_list.append(row)
        else:
            for row in self.c.execute("SELECT * FROM statements WHERE Name=?", (user_var,)):
                user_list.append(row)
                
        self.conn.close()
        
        df = pd.DataFrame(data = user_list, columns = ['Name', 'Date', 'Description', 'Amount', 'Type'])
        df.drop('Name', axis=1, inplace=True)
        
        return df
    
    
    def get_statements(self, category):
        '''
        Returns list of transactionn statements that match category passed to function

        Parameters
        ----------
        category : TYPE string
            DESCRIPTION. 

        Returns
        -------
        temp : TYPE list
            DESCRIPTION.

        '''
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()
        
        temp = []
        for row in self.c.execute('SELECT * FROM categories WHERE Category =?', (category,)):
            temp.append(row)
            
        
        self.conn.close()
        return temp
        
      
    def write_db(self, col1_var, col2_var, table_name):
        '''
        

        Parameters
        ----------
        col1_var : TYPE string
            DESCRIPTION. Name of first column in two-column database to be written to
        col2_var : TYPE string
            DESCRIPTION. Name second column in two-column database to be written to
        table_name : TYPE string
            DESCRIPTION. name of table to write to in db

        Returns
        -------
        None.

        '''
        
        self.conn = sqlite3.connect(os.path.join(admin_folder, self.db_filename))
        self.c = self.conn.cursor()
        
        #Below is not ideal as it opens to "injection attacks"
        self.c.execute("INSERT INTO {} VALUES (?, ?)".format(table_name), (col1_var, col2_var))
        
        self.conn.commit()    
        self.conn.close()
        
    
    def write_transactions(self, df):
        '''
        Write transactions to an existing database file from a dataframe

        Parameters
        ----------
        df : TYPE dataframe
            DESCRIPTION. Dataframe of statements to convert. Column must be in order of:
                Name, Date, Description, Amount, Type

        Returns
        -------
        None.

        '''
        
        self.conn = sqlite3.connect(self.db_filename)
        # self.c = self.conn.cursor()
        
        #Adding a extra column if missing the "type" column (ex. visa statements)
        if len(df.columns) < 5:
            df.loc[:, '3'] = None
        df.columns = ['Name', 'Date', 'Description', 'Amount', 'Type']
        #Converting description column to remove stopwords and numbers
        df.loc[:, 'Description'] = df.loc[:, 'Description'].apply(text_processor, args = (False,))
        

        
        df.to_sql(name = 'statements', con = self.conn, if_exists = 'append', index = False)
                  
        self.conn.commit()
        self.conn.close() 
        

    def delete_cat(self, table_name, cat_name):
        '''
        
        Remove all entries in a database based on category name

        Parameters
        ----------
        table_name : TYPE string
            DESCRIPTION. Name of table in database
        cat_name : TYPE string
            DESCRIPTION. Name of category to be removed

        Returns
        -------
        None.

        '''    
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()
        
        #Below is not ideal as it opens to "injection attacks"
        self.c.execute('DELETE FROM {} WHERE Category = ?'.format(table_name), (cat_name,))
        
        self.conn.commit()
        self.conn.close()
        
    def delete_statement(self, table_name, statement_name):
        '''
        
        Remove all entries in a database based on statement name

        Parameters
        ----------
        table_name : TYPE string
            DESCRIPTION. Name of table in database
        statement_name : TYPE string
            DESCRIPTION. Name of transaction statement to be removed

        Returns
        -------
        None.

        ''' 

        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()
        
        #Below is not ideal as it opens to "injection attacks"
        self.c.execute('DELETE FROM {} WHERE Statement = ?'.format(table_name), (statement_name,))
        
        self.conn.commit()
        self.conn.close()
        
'''Setting up GUI windows'''

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("DM Expense Tracker V.1")
        # main_width = 500
        # main_height = int(main_width / aspect_ratio)
        # self.resize(main_width, main_height)

        #Definition of class variables
        self.user_db = request_db('user_list.db')        

        #Initializing settings of features in main window
        self.ui.date_startDate.setDate(dt.datetime(2018, 1, 1))
        self.ui.date_endDate.setDate(dt.datetime.today())
        if len(self.user_db.get_users()) == 0:
            txt = "There are currently no users entered in the database. \n Select UTILITIES > ADD USER to enter a new user"
            self.msg_box = MessageBoxError(txt)
            self.msg_box.show()
        self.ui.cbo_userDropdown.addItems(self.user_db.get_users())
        self.ui.lbl_splitRatio.setVisible(False)
        self.ui.numb_ratio.setVisible(False)
        
        '''Actions of main window'''
        
        #showing additional options for household split ratio if selected
        self.ui.radio_incHousehold.toggled.connect(self.show_household)
        
        try:
            self.ui.command_analyzeExpenses.clicked.connect(self.main)
        except BaseException:
            print("error detected")
        # self.ui.command_analyzeExpenses.clicked.connect(self.open_results)
        
        #Menu bar add user clicked
        self.ui.action_addUser.triggered.connect(self.add_user)
        self.ui.action_addTransaction.triggered.connect(self.add_transaction)
        self.ui.action_addTransactionS.triggered.connect(self.add_transaction_s)
        self.ui.action_removeCat.triggered.connect(self.remove_cat)
        self.ui.action_removeCatEntry.triggered.connect(self.remove_cat_entry)
        
        #close the application if selected
        self.ui.actionExit_Application.triggered.connect(self.close)
        

    def show_household(self):
        if self.ui.cbo_userDropdown.currentText() not in self.user_db.get_users(sql_override=True, sql_statement = "SELECT Name FROM users WHERE Household != ''"):
            pass
        else:
            if self.ui.lbl_splitRatio.isVisible() == True:
                self.ui.lbl_splitRatio.hide()
            else:
                self.ui.lbl_splitRatio.show()
                
            if self.ui.numb_ratio.isVisible() == True:
                self.ui.numb_ratio.hide()
                self.ui.numb_ratio.setValue(0.0)
            else:
                self.ui.numb_ratio.show()  
                self.ui.numb_ratio.setValue(0.5)
                
    def add_user(self):
        self.add_user_window = AddUserWindow()
        self.add_user_window.show()
        self.close()
        
    def add_transaction_s(self):
        self.add_transaction_s_window = AddTransactionS()
        self.add_transaction_s_window.show()
        self.close()
        
    def add_transaction(self):
        self.add_transaction_window = AddTransaction()
        self.add_transaction_window.show()
        self.close()
        
    def remove_cat(self):
        self.remove_cat_window = MessageBoxRemoveCat()
        self.remove_cat_window.show()
        self.close()
        
    def remove_cat_entry(self):
        self.remove_cat_entry_window = MessageBoxRemoveStatement()
        self.remove_cat_entry_window.show()
        self.close()
                

    def main(self):
        '''This functions executes the main functionality of the program, and transfers
        the data to the results window'''
        
        name = self.ui.cbo_userDropdown.currentText()
            
        start_date =  self.ui.date_startDate.date().toPyDate()
        end_date = self.ui.date_endDate.date().toPyDate()
        
        if start_date > end_date:
            self.error = MessageBoxError("Please verify the date ranges specified")
            self.error.show()
            return None
        
        combine = self.ui.radio_incHousehold.isChecked()

        name = [name]
        if combine == True:
            for n in name:
                if len(self.user_db.get_households(sql_override=True, sql_statement = "SELECT Household FROM users WHERE Name == ?", sql_var = n)) > 0:
                    household_name = self.user_db.get_households(sql_override=True, sql_statement = "SELECT Household FROM users WHERE Name == ?", sql_var = n)[0]
                    name.append(household_name)
                    

        #the dict_of_names variable will be used to store the dataframes
        dict_of_names = {}
        #names = '\n'
        for n in name:
          #names = names + "\n" + n
          dict_of_names[n] = None
            
        # Building, cleaning and mofidying dataframe
        def dataframe_builder(dict_of_names, name):
            for n in name:
                if os.path.exists(os.path.join(statements_folder, "{}_statements_.db".format(n))) == False:
                    self.error = MessageBoxError('Missing statements in database to analyze for {}. \nPlease upload statements using Utilities > Add Expenses'.format(n))
                    self.error.show()
                    return None
                    
                db = request_db(os.path.join(statements_folder, "{}_statements_.db".format(n)))
                if n.lower() in [i.lower() for i in list(dict_of_names)]:
                    try:
                        dict_of_names[n] = db.get_transactions(user_var = n)
                        dict_of_names[n].loc[:, 'Owner'] = n
                    except OperationalError:
                        self.error = MessageBoxError('Missing statements in database to analyze for {}. \nPlease upload statements using Utilities > Add Expenses'.format(n))
                        self.error.show()
                        return None
                        
                        
            return {key:value for key, value in dict_of_names.items() if value is not None}
        
        dict_of_dfs = dataframe_builder(dict_of_names, name)
        if dict_of_dfs == None:
            return None
        
        #Modifying household expenses to include split ratio before creating central dataframe
        for key, value in dict_of_dfs.items():
            if key in self.user_db.get_households():
                value.loc[:, 'Amount'] *= self.ui.numb_ratio.value()
                value.loc[:, 'Owner'] = self.ui.cbo_userDropdown.currentText()
        
        
        df_raw = pd.concat([value for key, value in dict_of_dfs.items()], axis=0, ignore_index=True)
        df_raw.loc[:, 'Type'] = df_raw.loc[:, 'Type'].fillna('Credit')
        df_raw.loc[:, 'Date'] = pd.to_datetime(df_raw.loc[:, 'Date'], errors='coerce')
        df_raw.loc[:, 'Date_date'] = df_raw.loc[:, 'Date'].apply(lambda date: date.date())
        df_raw.sort_values(by='Date_date', inplace=True)
        df_raw = df_raw.loc[(df_raw['Date_date'] >= start_date) & (df_raw['Date_date'] <= end_date)]

        if len(df_raw.index) == 0:
            self.error = MessageBoxError('Missing statements in database to analyze for {}. \nPlease upload statements using Utilities > Add Expenses'.format(n))
            self.error.show()
            return None
            
        df_raw.loc[:, 'Description'].fillna(str(), inplace=True)
        df_raw.loc[:, 'Month'] = df_raw.loc[:, 'Date'].dt.to_period('M')
        df_raw.drop('Date_date', axis=1, inplace=True)

        def dataframe_cleaner(dataframe):
            '''
            This method takes in a transaction statement dataframe and cleans/adds fields for expense tracking
            ----------
            dataframe : TYPE
                DESCRIPTION.
        
            Returns improved dataframe for expense tracking
            -------
            None.
        
            '''
            dataframe_local = dataframe.copy()
            dataframe_local.loc[:, 'Description_BOW'] = dataframe_local.loc[dataframe_local['Description'].isnull() == False, 'Description'].apply(text_processor)
            dataframe_local.loc[:,'Description_BOW'] = dataframe_local.loc[dataframe_local['Description'].isnull() == False, 'Description_BOW'].apply(lambda bow: ' '.join(bow))
            dataframe_local.loc[:,'Description_BOW'] = dataframe_local.loc[dataframe_local['Description'].isnull() == False, 'Description_BOW'].apply(lambda description: description.replace('APPLE PAY', '') if 'APPLE PAY' in description else description)
        
            #Filling any description_BOW that have been rendered blank through text processor
            blanks = dataframe_local.loc[dataframe_local['Description_BOW'] == "", 'Description_BOW']
            dataframe_local.loc[blanks.index, 'Description_BOW'] = dataframe_local.loc[blanks.index, 'Type']
            del(blanks)
            dataframe_local.loc[:, 'Amount'] = dataframe_local.loc[:, 'Amount'].mul(-1)
            dataframe_local.drop('Description', axis=1, inplace=True)
            return dataframe_local
        
        #Creating new dataframe which contains the bag of words for transaction classification
        df_cleaned = dataframe_cleaner(df_raw)
        
        # Classification of transaction statements using imported module
        category_file = os.path.join(admin_folder, 'category_index.db')
        type_file = os.path.join(admin_folder, 'type_index.db')
        
        #Creating instances of local KeywordClassifier class
        classifier = KeywordClassifier(category_file, type_file, admin_folder)
        categories = classifier.category_dict()
        types = classifier.type_dict()
        
        #Applying classification algorithm to each entry in the dataframe
        df_cleaned.loc[:, 'Category'] = df_cleaned.apply(lambda x: classifier.classic_classifier(x['Type'], x['Description_BOW'], types, categories), axis=1)

        # Analyzing spending statistics for display in tabular format in the results window
        df_by_month = df_cleaned.copy()
        df_by_month = df_by_month.groupby(['Owner', 'Category', 'Month'])['Amount'].sum().reset_index(level=2).reset_index(level=1).reset_index(level=0)
        df_by_month.sort_values(by='Month', inplace=True)
        df_by_month.loc[:, 'Month'] = df_by_month.loc[:, 'Month'].apply(lambda date:str(date))
        
        df_by_year = df_cleaned.copy()
        df_by_year['Year'] = df_by_year.loc[:, 'Date'].apply(lambda x: x.year)
        df_by_year = df_by_year.groupby(['Owner', 'Category', 'Year'])['Amount'].sum().reset_index(level=2).reset_index(level=1).reset_index(level=0)
        df_by_year.sort_values(by='Year', inplace=True)
        
        #even though the function reference says days, it is actually months/years based on conversion        
        num_months = ((end_date - start_date)*12/365).days
        if num_months == 0:
            num_months = 1
        num_yrs = num_months/12
        if num_yrs == 0:
            num_yrs = 1
       
        
        def GUI_table(time_period, df):
            '''
            Creates a summary table of spending organized by month and by year

            Parameters
            ----------
            time_period : Type Int
                The number of units of time (months or year) to group spending by
            df : TYPE dataframe
            The dataframe containing the classified transactions.

            Returns
            -------
            df_local : TYPE
                DESCRIPTION.

            '''
            df_local = df.copy()
            df_local = df_local.groupby(['Owner', 'Category'])['Amount'].agg(['sum', 'median', 'std']).reset_index(1).reset_index(0)
            df_local.loc[:,'Average'] = df_local.loc[:,'sum'] / time_period
            df_local = df_local.loc[:, ['Category', 'Average', 'median', 'std']]
            df_local = df_local[df_local['Category'].str.contains(",") == False]
            return df_local
                
        df_widget_by_month = GUI_table(num_months, df_by_month)
        df_widget_by_year = GUI_table(num_yrs, df_by_year)
        
        #displaying summary stats (classification rate, fixed cost ratio, variable cost ratio, savings ratio)
        class_rate = round(100*(1-(sum(df_cleaned['Category'] == 'unclassified')/sum(df_cleaned['Category'] != 'unclassified'))), 2)
        
        expense_type_dict = dict(request_db(os.path.join(admin_folder, 'expense_type_index.db')).fetch_all('expense_type'))
        
        df_cleaned.loc[:, 'Expense_type'] = df_cleaned.loc[:, 'Category'].map(expense_type_dict)
        df_by_expense = df_cleaned.groupby('Expense_type')['Amount'].sum()
        try:
            fixed_expense_ratio = round(df_by_expense['fixed'] / df_by_expense['revenue']*-1, 2)
        except KeyError:
            fixed_expense_ratio = 'N/A'
        try:
            var_expense_ratio = round(df_by_expense['variable'] / df_by_expense['revenue']*-1, 2)
        except KeyError:
            var_expense_ratio = 'N/A'
        try:
            savings_ratio = round(df_by_expense['savings'] / df_by_expense['revenue']*-1, 2)
        except KeyError:
            savings_ratio = 'N/A'
        
        #Analyzing outlier purchases/spending patterns
        df_by_cat = df_cleaned.copy()
        df_by_cat = df_by_cat.groupby(['Owner', 'Category'])['Amount'].agg(['sum', 'median', 'count', 'std']).reset_index(1).reset_index(0)
        df_by_cat.loc[:,'Monthly_Average'] = df_by_cat.loc[:,'sum']/ num_months
        df_by_cat = df_by_cat.loc[:, ['Owner', 'Category', 'Monthly_Average', 'median', 'std', 'sum', 'count']]
        
        def identify_outliers(df, df_by_cat = df_by_cat, limit=500):
            ''' using the .iterrows method here since i have not been able
            to find a better way to filter out the outliers while using the .apply method'''
            df_outliers = pd.DataFrame(columns = df.columns)
            for index,row in df.iterrows():
                if row['Amount'] > 1.5*(df_by_cat.loc[(df_by_cat['Owner'] == row['Owner']) & (df_by_cat['Category'] == row['Category']), 'Monthly_Average'].iloc[0]) and row['Amount'] > limit:
                    df_outliers = df_outliers.append(row)    
            return df_outliers
        
        df_outliers = identify_outliers(df_cleaned)        
        df_outliers.loc[:, 'Month_str'] = df_outliers.loc[:, 'Month'].apply(lambda x: str(x))
        df_outliers.loc[:, 'Month_dt'] = pd.to_datetime(df_outliers.loc[:,'Month_str'])                                                                             
        df_outliers.drop(['Date', 'Type'], axis=1, inplace=True)
        
        #Creating a separate dataframe for plotting, to be passed to results window
        df_plot = df_by_month.copy()
        df_plot.loc[:, 'Month_dt'] = pd.to_datetime(df_plot.loc[:,'Month'])
        
        #Opening results window and passing objects to populate/display. May be better way of doing this. 
        #Did it this way since the two windows are separate classes.
        self.results_window = ResultsWindow(df_widget_by_month,
                                       df_widget_by_year,
                                       name,
                                       start_date,
                                       end_date,
                                       str(class_rate),
                                       str(fixed_expense_ratio),
                                       str(var_expense_ratio),
                                       str(savings_ratio),
                                       df_cleaned,
                                       df_by_month,
                                       df_by_year,
                                       df_plot,
                                       df_outliers)
        self.results_window.show()
        self.close()

        
        '''Troubleshooting section'''
        #Analyzing transaction statements that have been categorized twice or more
        doubles = df_cleaned.loc[:, 'Category'].apply(lambda x: len(x.split(',')))
        doubles = doubles[doubles > 1]
        doubles = df_cleaned.loc[doubles.index, :]
        doubles.to_excel(os.path.join(troubleshooting_folder, "statements_multiple_cats.xlsx"))
        
        

class ResultsWindow(QtWidgets.QWidget):
    def __init__(self,  df_widget_by_month, df_widget_by_year, name, start_date, 
                 end_date, class_rate, fixed_exp_ratio, var_exp_ratio, savings_ratio, 
                 df_cleaned, df_by_month, df_by_year, df_plot, df_outliers, parent = None):
        super().__init__()

        self.ri = Ui_Form()
        self.ri.setupUi(self)
        self.setWindowTitle('Expense Results and Analysis')
        
        
        #Setting class variables
        self.df_widget_by_month = df_widget_by_month
        self.df_widget_by_year = df_widget_by_year
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.class_rate = class_rate
        self.fixed_exp_ratio = fixed_exp_ratio
        self.var_exp_ratio = var_exp_ratio
        self.savings_ratio = savings_ratio
        self.df_cleaned = df_cleaned
        self.df_by_month = df_by_month
        self.df_by_year = df_by_year,
        self.df_plot = df_plot
        self.df_outliers = df_outliers

        
        #Initializing settings of results window
        #resizing and centering the results screen
        screen_width = 1600 #px
        screen_height = int(screen_width * 1.05 / aspect_ratio) #px
        self.resize(screen_width, screen_height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        #Setting initial table/tab dimensions which are likely to be overriden later
        tab_width = 600
        tab_height = 900
        tab_start_x = 10
        tab_start_y = 10
        self.ri.tab_byMonthYear.setGeometry(QtCore.QRect(tab_start_x, tab_start_y, tab_width, tab_height))
        self.ri.tab_byMonthYear.setTabText(0, "By Month")
        self.ri.tab_byMonthYear.setTabText(1, "By Year")
        self.ri.table_byMonth.setGeometry(QtCore.QRect(tab_start_x, tab_start_y, 640, 800))
        self.ri.table_byYear.setGeometry(QtCore.QRect(tab_start_x, tab_start_y, 640, 800))
        

        #Setting other items
        self.ri.radio_allTransactions.setChecked(True)
        self.ri.radio_byMonth.setChecked(False)
        self.ri.radio_byYear.setChecked(False)
        self.ri.check_annotateOutliers.setChecked(False)
        self.ri.check_addMedian.setChecked(False)
        self.ri.check_excUnclassified.setChecked(True)
        self.ri.check_excMisc.setChecked(True)
        self.ri.date_lowRange.setDate(self.start_date)
        self.ri.date_highRange.setDate(self.end_date)
        
        self.ri.lbl_optionSavePlot.setVisible(False)
        self.ri.cmd_savePlot.setVisible(False)

        #Setting plot area initially
        self.ri.wdg_plot = MplWidget(self)
        
        #actions
        self.ri.cmd_exportData.clicked.connect(self.export_data)
        self.ri.cmd_plotData.clicked.connect(self.plot_data)
        self.ri.cmd_savePlot.clicked.connect(self.save_plot)  
        
    def showEvent(self, event):
        '''The following method returns the user to main screen if window is exited from action bar'''
        self.display_by_month()
        self.display_by_year()
        self.display_stats()
        event.accept()
            
    def return_width(self, table, df):
            temp = {}
            for col in range(0, int(len(df.columns))):
                temp[col] = table.columnWidth(col) 
            return sum(list(temp.values())) 
        
    def display_by_month(self):
        df = self.df_widget_by_month
        for row in range(0, len(df)):
            self.ri.table_byMonth.insertRow(self.ri.table_byMonth.rowCount())
            for col in range(0, len(df.columns)):
                try:
                    if type(df.iloc[row, col]) == str:
                        self.ri.table_byMonth.setItem(row, col, QtWidgets.QTableWidgetItem(str(df.iloc[row, col])))    
                    else:
                        self.ri.table_byMonth.setItem(row, col, QtWidgets.QTableWidgetItem(str(int(df.iloc[row, col]))))
                except ValueError:
                    pass

        #Future functionality can include putting net return by month based on averages (i.e how much leftover money at end of month)
        
        #Resizing table to match df
        self.ri.table_byMonth.resizeColumnsToContents()
        self.ri.table_byMonth.setColumnWidth(0, 180)
        table_height = self.ri.table_byMonth.rowHeight(0) * int(len(df))
        table_width = self.return_width(self.ri.table_byMonth, df)
        self.ri.tab_byMonthYear.setGeometry(10,10, table_width+50, table_height+80)
        self.ri.lbl_classRate.setGeometry(40, table_height+100, 200, 50)
        
          
        #Adjusting info form below table
        form_width = self.ri.tab_byMonthYear.width()
        self.ri.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 
                                                   10 + self.ri.tab_byMonthYear.height() + 10, 
                                                   form_width, 
                                                   130))
        
        #Adjusting data export form object to reflect change in table size
        form_width = self.width() - self.ri.tab_byMonthYear.width() - 50
        export_form_height = 150
        gap = 25 #px
        self.ri.formLayoutWidget.setGeometry(QtCore.QRect(10 + self.ri.tab_byMonthYear.width() + gap, 
                                                          10, 
                                                          form_width, 
                                                          export_form_height))
        
        
        #Setting data plotting object
        self.ri.formLayoutWidget_2.setGeometry(QtCore.QRect(10 + self.ri.tab_byMonthYear.width() + gap,
                                                            self.ri.formLayoutWidget.height() + 50, 
                                                            form_width,
                                                            230))
        #setting plot area size
        self.ri.wdg_plot.setGeometry(QtCore.QRect(10 + self.ri.tab_byMonthYear.width() + gap,
                                              (self.ri.formLayoutWidget.height() + self.ri.formLayoutWidget_2.height()+ 40 + 10),
                                              form_width,
                                              int((self.height() - export_form_height - 25 - 50)*0.7)))
        

    def display_by_year(self):
        df = self.df_widget_by_year
        #Better OOP could be implemented by creating class with function above
        for row in range(0, int(len(df))):
            self.ri.table_byYear.insertRow(self.ri.table_byYear.rowCount())
            for col in range(0, int(len(df.columns))):
                try:
                    if type(df.iloc[row, col]) == str:
                        self.ri.table_byYear.setItem(row, col, QtWidgets.QTableWidgetItem(str(df.iloc[row, col])))    
                    else:
                        self.ri.table_byYear.setItem(row, col, QtWidgets.QTableWidgetItem(str(int(df.iloc[row, col]))))
                except ValueError:
                    pass
        #Future functionality can include putting net return by month based on averages (i.e how much leftover money at end of month)

        #Resizing table to match df
        self.ri.table_byYear.resizeColumnsToContents()
        self.ri.table_byYear.setColumnWidth(0, 180) 
        
        
    #Displaying summary statistics based on spending
    def display_stats(self):
        self.ri.lbl_user.setText(", ".join(self.name))
        self.ri.lbl_dateRange.setText(str(self.start_date) + "   to   " + str(self.end_date))
        self.ri.lbl_fixedExpRatio.setText(self.fixed_exp_ratio)
        self.ri.lbl_varExpRatio.setText(self.var_exp_ratio)
        self.ri.lbl_savingsRatio.setText(self.savings_ratio)
        
        self.ri.lbl_classRate.setText(self.class_rate + " %")
        self.ri.cbo_catSelectorExporting.addItems(list(self.df_widget_by_month['Category'].unique()))
        self.ri.cbo_catSelectorPlotting.addItems(list(self.df_widget_by_month['Category'].unique()))
        

        

    def export_data(self):
             
        '''Export data as excel file to local desktop folder. 
        This function is nested since I only want to export the relevant data if the 
        push_Export button is clicked.''' 
        
        radio = [self.ri.radio_allTransactions.isChecked(),
                  self.ri.radio_byMonth.isChecked(),
                  self.ri.radio_byYear.isChecked()]

        if self.ri.cbo_catSelectorExporting.currentText() == 'All Categories':
            category = 'All Categories'
            if radio[0] == True:
                df_export = self.df_cleaned
                df_name = 'df_cleaned'
            elif radio[1] == True:
                df_export = self.df_by_month
                df_name = 'df_by_month'
            elif radio[2] == True:
                df_export = self.df_by_year
                df_name = 'df_by_year'
        else:
            category = self.ri.cbo_catSelectorExporting.currentText()
            if radio[0] == True:
                df_export = self.df_cleaned.loc[self.df_cleaned['Category'] == category]
                df_name = 'df_cleaned'
            elif radio[1] == True:
                df_export = self.df_by_month.loc[self.df_by_month['Category'] == category]
                df_name = 'df_by_month'
            elif radio[2] == True:
                df_export = self.df_by_year.loc[self.df_by_year['Category'] == category]
                df_name = 'df_by_year'
  
        df_export.to_excel(os.path.join(datafolder, df_name +"_" + category.replace(" ", "_") + "_" + str(dt.datetime.now()).split(".")[0].replace(" ", "_").replace(":", "_") + ".xlsx"))
        self.msg_box = MessageBoxSuccess("Data successfully exported to: \n" + str(datafolder))
        self.msg_box.show()
        

    def plot_data(self):
        '''Plots the relevant spending data for the user'''

        tick_fontsize = 14
        label_fontsize = 16
        title_fontsize = 20
        
        #Determining which expense category is to be plotted based on user selection
        if self.ri.cbo_catSelectorPlotting.currentText() == "All Categories":
            df = self.df_plot.copy()
            if self.ri.check_excUnclassified.isChecked() == True:
                df = df.loc[df['Category'] != 'unclassified']
            if self.ri.check_excMisc.isChecked() == True:
                df = df.loc[df['Category'] != 'misc_transfers']
            self.cat = 'All Categories'
        else:
            self.cat = self.ri.cbo_catSelectorPlotting.currentText()
            df = self.df_plot.loc[self.df_plot['Category'] == self.cat]
        
        #1. Setting up and plotting the scatterplot
        self.ri.wdg_plot.figure.clear()
        self.ri.wdg_plot.canvas.draw()
        ax = self.ri.wdg_plot.figure.add_subplot(111)
        ax.grid(color = 'black', axis = 'both', which = 'major', alpha = 0.4)
        
        plt.scatter(x = df['Month_dt'], y = df['Amount'], s = 300,
                        c= [self.ri.cbo_markerColor.currentText()], 
                        marker = self.ri.cbo_markerType.currentText(), 
                        edgecolor = 'black')

        #modifying y-axis based on user entry
        if self.ri.txt_yLow.text() != "" and self.ri.txt_yHigh.text() != "":
            try:
                y_low = int(self.ri.txt_yLow.text())
                y_high = int(self.ri.txt_yHigh.text())
                ax.set_ylim(y_low, y_high)
            except ValueError:
                self.error = MessageBoxError(self, "You must enter an integer value for the y-axis range")
                self.error.show()
                return None
                
        #modifying x-axis based on user entry        
        if self.ri.date_lowRange.date().toPyDate() != self.start_date or self.ri.date_highRange.date().toPyDate() != self.end_date:
            if self.ri.date_lowRange.date() > self.ri.date_highRange.date():
                self.error = MessageBoxError("Make sure the lower end date and the higher end date are in order")
                self.error.show()
                return None
            else:
                low_date = self.ri.date_lowRange.date().toPyDate()
                hi_date = self.ri.date_highRange.date().toPyDate()
                ax.set_xlim(low_date, hi_date)
                
        if self.cat != 'All Categories':
            ax.set_title(self.cat, fontsize=title_fontsize, fontweight = 'bold', color='black')
        
        else:
            ax.set_title('All Categories', fontsize=title_fontsize, fontweight = 'bold', color='black')
        ax.set_xlabel('Month', fontsize=label_fontsize, fontweight = 'bold')
        ax.set_ylabel('Monthly Amount, CDN', fontsize=label_fontsize, fontweight = 'bold')
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)
            tick.set_fontsize(tick_fontsize)
            tick.set_fontweight('bold')
            
        for tick in ax.get_yticklabels():
            tick.set_fontsize(tick_fontsize)
            tick.set_fontweight('bold')
        
        if self.ri.check_annotateOutliers.isChecked() == True:    
            # Identifying outliers directly on the plot based on user preference
            outlier_dates = []
            [outlier_dates.append(day) for day in list(df['Month'].values) if day not in outlier_dates]
            outliers_temp = self.df_outliers[(self.df_outliers.loc[:, 'Month_str'].isin(outlier_dates)) & \
                                        (self.df_outliers.loc[:, 'Category'] == self.cat)].copy()
            if outliers_temp.empty:
                next
                
            else:
                outliers_temp.loc[:, 'Identifier'] = outliers_temp.apply(lambda x: str(x['Owner']) + str(x['Month_str']), axis=1)
            
            
                for entry in outliers_temp['Identifier'].unique():
                    #Below is using the .loc function to find the description BOW, month and amounts from outlier_temp and df_plot for annotation
                    locator = outliers_temp.where(outliers_temp['Identifier'] == entry).dropna().index[0]
                    ax.annotate(outliers_temp.loc[locator, 'Description_BOW'], 
                                  xy = (outliers_temp.loc[locator, 'Month_dt'],
                                        df.loc[df[(df['Owner'] == outliers_temp.loc[locator, 'Owner']) & \
                                                  (df['Month'] == outliers_temp.loc[locator, 'Month_str'])].index[0], 'Amount']), 
                                  fontsize=8, fontweight = 'bold')
                        
                        
        #Setting up horizontal line to represent median based on user preference
        if self.ri.check_addMedian.isChecked() == True:
            ax.hlines(y = np.median(df['Amount']), 
                        xmin = df.iloc[0]['Month_dt'],
                        xmax = df.iloc[-1]['Month_dt'], 
                        color=self.ri.cbo_markerColor.currentText())
        ax.legend('')
        self.ri.wdg_plot.figure.tight_layout()
        
        #Drawing canvas
        self.ri.wdg_plot.canvas.draw()
        
        #Showing options to allow user to save the plot
        self.ri.lbl_optionSavePlot.show()
        self.ri.cmd_savePlot.show()
        

    def save_plot(self):
        
        #This function saves the plot object in the GUI to local desktop folder
        self.ri.wdg_plot.figure.savefig(os.path.join(plotfolder, self.cat.lower().replace(" ", "_") + "_" + str(dt.datetime.now()).split(".")[0].replace(" ", "_").replace(":", "_") + ".jpeg"), dpi=200)
        self.msg_box = MessageBoxSuccess("Plot successfully exported to: \n" + str(plotfolder))
        self.msg_box.show()

        
    def closeEvent(self, event):
        '''The following method returns the user to main screen if window is exited from action bar'''
        self.main_window = MainWindow()
        self.main_window.show()
        event.accept()
        

'''The following represents the base class for matplotlib widget'''
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        self.figure = plt.figure(dpi=60)
        self.figure.set_facecolor('None')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setStyleSheet("background-color:transparent;")
        # self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()
        # vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        
        # self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)


'''Below is for the add user window and corresponding functionality'''
class AddUserWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ai = Ui_AddUser()
        self.ai.setupUi(self)
        self.setWindowTitle('Add User Form')
        
        
        #Setting class variables
        self.user_db = request_db('user_list.db')
        
        #Setting properties of features
        self.ai.lbl_householdOption.setVisible(False)
        self.ai.cbo_household.setVisible(False)
        self.ai.txt_household.setVisible(False)
        
        
        #Setting actions
        self.ai.radio_yesCombined.toggled.connect(self.show_household)
        # self.ai.push_cancel.clicked.connect(self.close_window)
        self.ai.push_register.clicked.connect(self.register_user)
        self.ai.cbo_household.addItems(self.user_db.get_households())
        
       
    #Class functions
    def show_household(self):
        if self.ai.radio_yesCombined.isChecked():
            self.ai.lbl_householdOption.show()
            self.ai.cbo_household.show()
            self.ai.txt_household.show()
        else:
            self.ai.lbl_householdOption.setVisible(False)
            self.ai.cbo_household.setVisible(False)
            self.ai.txt_household.setVisible(False)

        
    def closeEvent(self, event):
        '''The following method returns the user to main screen if window is exited from action bar'''
        self.main_window = MainWindow()
        self.main_window.show()
        event.accept()
           
    def register_user(self):
        #error handling

        #1. if user does not enter a name
        if self.ai.txt_user.text() == '':
            self.error = MessageBoxError('Please enter a valid user name')
            self.error.show()
            return None
        #2. If the user enters a name that already exists
        elif self.ai.txt_user.text() in self.user_db.get_users():
            self.error = MessageBoxError('User already exists')
            self.error.show()
            return None
        #3. If the user tries to enter a household name that already exists (prevent unintentional duplicates)
        elif self.ai.txt_household.isVisible() and self.ai.txt_household.text() in self.user_db.get_households() and self.ai.txt_household.text()!= '':
            self.error = MessageBoxError('household already exists.\nSelect the household in the dropdown box')
            self.error.show()
            return None
            self.ai.txt_household.text() == ''
        #4: fixing bug if household name set same as user name
        elif self.ai.txt_household.text() == self.ai.txt_user.text():
            self.error = MessageBoxError('Select a household name that is different from the name of the user')
            self.error.show()
            return None
            
        else:
        
            if self.ai.radio_noCombined.isChecked():
                #Adding new user to database
                self.user_db.write_db(col1_var = self.ai.txt_user.text().lower(),
                                      col2_var = '', table_name = 'users')

            #updating user list and household list simulataneously
            else:
                if self.ai.txt_household.text() == '':
                    #Adding new user and household to database if user selected existing household name
                    self.user_db.write_db(col1_var = self.ai.txt_user.text().lower(),
                                      col2_var = self.ai.cbo_household.currentText().lower(), table_name = 'users')
                    
                else:
                    #Adding new user and household to database if user types new household name
                    self.user_db.write_db(col1_var = self.ai.txt_user.text().lower(),
                                      col2_var = self.ai.txt_household.text().lower(), table_name = 'users')
    
            #Re-opening main window to refresh
            main_window = MainWindow()
            main_window.show()
            self.close()
    
                
'''Below represents the bulk transaction upload window and corresponding functionality'''
class AddTransactionS(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.bi = Ui_window_addTransactionS()
        self.bi.setupUi(self)
        self.setWindowTitle('Add Transaction Bank Statements')
        screen_width = 1200
        self.resize(screen_width, int((screen_width / aspect_ratio) * 1.2))
        
        #class variables
        self.user_db = request_db('user_list.db')
        
        #Setting features of window
        self.bi.table_file.setVisible(False)
        self.bi.cmd_upload.setVisible(False)
        self.bi.radio_personal.setVisible(False)
        self.bi.radio_combined.setVisible(False)
        self.bi.cbo_userHousehold.setVisible(False)
                
        #Setting Actions
        self.bi.push_uploadCSV.clicked.connect(self.open_csv)
        self.bi.cmd_upload.clicked.connect(self.to_db)
        self.bi.radio_personal.toggled.connect(self.populate_combo)
        self.bi.radio_combined.toggled.connect(self.populate_combo)

        
        
    def populate_combo(self):
        self.bi.cbo_userHousehold.clear()
        if self.bi.radio_personal.isChecked():
            self.bi.cbo_userHousehold.addItems(self.user_db.get_users())
        if self.bi.radio_combined.isChecked():
            self.bi.cbo_userHousehold.addItems(self.user_db.get_households())
            
        
    
    def return_width(self, table, df):
            temp = {}
            for col in range(0, int(len(df.columns))):
                temp[col] = table.columnWidth(col) 
            return sum(list(temp.values())) 
    
    
    def open_csv(self):
        '''This method opens the corresponding CSV that the user selected and displays i
        on th window'''
        
        options = QFileDialog.Options()
        file_name, file_type = QFileDialog.getOpenFileName(self,
                                                "File Explorer", 
                                                "","CSV Files (*.csv);;All Files (*)",
                                                options=options)
        
        self.file_name = file_name #to be able to use it in next method

        if file_name == "":
            return None
        elif file_type != "CSV Files (*.csv)":
            self.error = MessageBoxError('You must select a .csv file')
            self.error.show()
            return None
        else:
           
            #Clearing entries from table if already opened
            if self.bi.table_file.isVisible():
                self.bi.table_file.clearContents()
                
            #Convert csv file to pyqt table object
            self.bi.table_file.setVisible(True)
            self.table = pd.read_csv(file_name, index_col=False, delimiter = ',', header=None)
            #Eliminating any null values so that they are not entered into db
            self.table.fillna('', inplace=True)
            
            self.bi.table_file.setColumnCount(len(self.table.columns))
            
            #Setting headers of table and other properties
            self.bi.table_file.setHorizontalHeaderLabels(['Date', 'Description', 'Amount (CDN)', 'Type'])

            
            #Passing values to table and capturing any statements not in  with the use of statement_temp. To be used later in the class    
            self.statement_temp = set()
            for row in range(0, len(self.table)):
                self.bi.table_file.insertRow(self.bi.table_file.rowCount())
                for col in range(0, len(self.table.columns)):
                    try:
                        if type(self.table.iloc[row,col]) == str:
                            self.bi.table_file.setItem(row, col, QtWidgets.QTableWidgetItem(str(self.table.iloc[row,col])))    
                        else:
                            self.bi.table_file.setItem(row, col, QtWidgets.QTableWidgetItem(str(int(self.table.iloc[row,col]))))
                    except ValueError:
                        pass
                    if col == 1:
                        statement = text_processor(self.table.iloc[row, col], bow=False)
                        if str(statement) == 'nan' or str(statement) == '':
                            next
                        else:
                            temp = []
                            for i in self.list_statement():
                                if i.lower() in statement.lower():
                                    temp.append(i)
                            
                            if len(temp) == 0:
                                self.statement_temp.add(statement)
                            
                    
            self.bi.table_file.resizeColumnsToContents()
            width = self.return_width(self.bi.table_file, self.table)
            self.bi.table_file.setGeometry(QtCore.QRect(10, 160, int(width*1.1), 600))
            
            #Set other features visible
            self.bi.radio_personal.setVisible(True)
            self.bi.radio_combined.setVisible(True)
            self.bi.cbo_userHousehold.setVisible(True)
            self.bi.cmd_upload.setVisible(True)
    

    def to_db(self):
        '''convert pyqt table object to db object'''
        
        #Adding dataframe to sql database
        
        file_name = self.bi.cbo_userHousehold.currentText() + "_statements_" +  ".db"
        
        #checking if db already exists, if not, will create new one
        if os.path.exists(os.path.join(statements_folder, file_name)) == False:
            con = sqlite3.connect(os.path.join(statements_folder, file_name))
            c = con.cursor()
            c.execute('''CREATE TABLE statements
                       (Name text, Date text, Description text, Amount real, Type text)''')
            con.commit()
            con.close()
        
        
        self.statements_db = request_db(os.path.join(statements_folder, file_name))
        self.table.insert(0, '00', self.bi.cbo_userHousehold.currentText())
        self.statements_db.write_transactions(self.table)
        
        #Moving copy of the csv file into backup
        self.table.to_csv(os.path.join(trans_backup_folder, file_name.replace(".db", "") + str(dt.datetime.now()).split(".")[0].replace(" ", "_").replace(":", "_") + ".csv"), index = False)
        
        #Clearing the current table
        while self.bi.table_file.rowCount() > 0:
            self.bi.table_file.removeRow(0)
            
        while self.bi.table_file.columnCount() > 0:
            self.bi.table_file.removeColumn(0)
        self.bi.table_file.setVisible(False)

        
        #checking if the statement line is in the database. If not, prompt user to enter the statement into the database
        if len(self.statement_temp) > 0:
            self.prompt_user_box = MessageBoxPrompt(msg_txt = 'There was {} statements in the import that are not registered in the application\n' \
                              'classification dictionary. To improve performance on future expense classification,\n' \
                                  'would you like to assign categories for these one at a time? \n' \
                                      'Select OK to assign categories, or select CANCEL to skip.'.format(str(len(self.statement_temp))))
            self.prompt_user_box.show()
            
            #The QDialog .exec() function is used on conjunction with the Qdialog.done() function in the MessageBoxPrompt. This returns the value of .done()
            result = self.prompt_user_box.exec()
            #Looping through statements if user elects to enter categories
            if result == 1: #Result 1 == Yes, 0 == No
                #Creating an instance of the new category input window for every new expense statement
                for statement in self.statement_temp:
                    self.add_cat_box = MessageBoxUpdate(new_statement = statement)
                    self.add_cat_box.show()
                    self.add_cat_box.exec() #This is just used to hold window for each entry - may need to look at better way of doing this


        #indicating to the user that the move was successful
        self.msg_box = MessageBoxSuccess('Statements successfully moved to database at \n{}'.format(os.path.join(statements_folder, file_name)))
        self.msg_box.show()
        
        self.bi.cmd_upload.setVisible(False)
        
 
    def list_statement(self):
        statements = request_db(os.path.join(admin_folder, 'category_index.db')).fetch_all('categories')
        
        return [b for a,b in statements] 

        
    def closeEvent(self, event):
        '''The following method returns the user to main screen if window is exited from action bar'''
        self.main_window = MainWindow()
        self.main_window.show()
        event.accept()
    
            
'''Below is for single transaction entry by the user'''
class AddTransaction(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.ci = Ui_window_addTransaction()
        self.ci.setupUi(self)
        self.setWindowTitle('Add Transaction')

        #Setting class variables
        self.user_db = request_db('user_list.db')

        #Setting features of window
        self.ci.date_expense.setDate(dt.date.today())
        self.ci.radio_expense.setChecked(True)
        self.ci.cmd_upload.setVisible(False)
        
                
        #Setting Actions
        self.ci.radio_personal.toggled.connect(self.populate_combo)
        self.ci.radio_combined.toggled.connect(self.populate_combo)
        self.ci.radio_personal.setChecked(True)
        self.ci.txt_statement.textChanged.connect(self.show_command_button)
        self.ci.txt_amount.textChanged.connect(self.show_command_button)
        self.ci.cmd_upload.clicked.connect(self.to_db)
        
        
    def show_command_button(self):
        if self.ci.txt_statement.text() != '' and self.ci.txt_amount.text() != '':
            self.ci.cmd_upload.setVisible(True)
        else:
            self.ci.cmd_upload.setVisible(False)
        
    def populate_combo(self):
        self.ci.cbo_userHousehold.clear()
        if self.ci.radio_personal.isChecked():
            self.ci.cbo_userHousehold.addItems(self.user_db.get_users())
        if self.ci.radio_combined.isChecked():
            self.ci.cbo_userHousehold.addItems(self.user_db.get_households())
            
    def to_db(self):
        
        #error handling - things blank or amount not a number
        try:
            float(self.ci.txt_amount.text())
        except ValueError:
            self.ci.txt_amount.setText('')
            self.error = MessageBoxError('Please enter a positive numerical value for the amount')
            self.error.show()
            return None
            
        if self.ci.txt_statement.text() == '':
            self.error = MessageBoxError('Please enter a description of the transaction statement')
            self.error.show()
            return None
        
        
        file_name = self.ci.cbo_userHousehold.currentText() + "_statements_" +  ".db"
        
        #checking if db already exists, if not, will create new one
        if os.path.exists(os.path.join(statements_folder, file_name)) == False:
            con = sqlite3.connect(os.path.join(statements_folder, file_name))
            c = con.cursor()
            c.execute('''CREATE TABLE statements
                       (Name text, Date text, Description text, Amount real, Type text)''')
            con.commit()
            con.close()
        
        
        self.statements_db = request_db(os.path.join(statements_folder, file_name))
        
        #converting the text amount to float and setting to negative value to represent expense
        amount = round(float(self.ci.txt_amount.text()), 2)
        if self.ci.radio_expense.isChecked():
            amount *= -1
        
        #creating local variable for use at end of method
        statement_temp = text_processor(self.ci.txt_statement.text(), bow=False)
        
        #packaging data into dataframe for writing to db
        temp = pd.DataFrame(data = [[self.ci.cbo_userHousehold.currentText(),
                              str(self.ci.date_expense.date().toPyDate()),
                              statement_temp,
                              amount,
                              self.ci.txt_type.text()]])
        
        self.statements_db.write_transactions(temp)
        
        
        
        # Reset values
        self.ci.date_expense.setDate(dt.date.today())
        self.ci.txt_statement.setText('')
        self.ci.txt_amount.setText('')
        self.ci.txt_type.setText('')
        
        #indicating to the user that the move was successful
        self.msg_box = MessageBoxSuccess('Statements successfully moved to database at \n{}'.format(os.path.join(statements_folder, file_name)))
        self.msg_box.show()
        
        #checking if the statement line is in the database. If not, prompt user to enter the statement into the database
        temp = []
        for i in self.list_statement():
            if i.lower() in statement_temp.lower():
                temp.append(i)
        if len(temp) == 0:
            self.add_cat_box = MessageBoxUpdate(new_statement = statement_temp)
            self.add_cat_box.show()
        del(temp)

    def list_statement(self):
        statements = request_db(os.path.join(admin_folder, 'category_index.db')).fetch_all('categories')
        
        return [b for a,b in statements]


    def closeEvent(self, event):
        '''The following method returns the user to main screen if window is exited from action bar'''
        self.main_window = MainWindow()
        self.main_window.show()
        event.accept()
        
        
        
#This class is only used as a parent class for the different types of message boxes
class MessageBox(QtWidgets.QDialog):
    def __init__(self, msg_txt = None, parent = None):
        super().__init__(parent)
        
        #Setting class variables
        self.msg_text = msg_txt


        #Features of window
        self.mi = Ui_MessageBox()
        self.mi.setupUi(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        #Setting defeault features of window objects
        self.mi.cbo_cats.setVisible(False)
        self.mi.txt_newCat.setVisible(False)
        self.mi.push_cancel.setVisible(False)
        
            
class MessageBoxSuccess(MessageBox):
    def __init__(self, msg_txt = None, parent = None):
        super().__init__(msg_txt)
        self.msg_txt = msg_txt
        
        self.setWindowTitle('Success')
        self.mi.lbl_message.setText(self.msg_txt)
        self.mi.lbl_message.setFont(bold_font)
        self.mi.push_OK.clicked.connect(self.close)
        
class MessageBoxError(MessageBox):
    def __init__(self, msg_txt = None, parent = None):
        super().__init__(msg_txt)
        self.msg_txt = msg_txt
        
        self.setWindowTitle('Error')
        self.mi.lbl_message.setText(self.msg_txt)
        self.mi.lbl_message.setFont(bold_font)
        self.mi.push_OK.clicked.connect(self.close)
        
        
class MessageBoxUpdate(MessageBox):
    def __init__(self, new_statement, msg_txt = None, parent = None):
        super().__init__(msg_txt)
        self.new_statement = new_statement
        self.msg_txt = "To specify an expense category to: {}\n" \
             "Please select an existing cateogry using the dropdown on the left, \n" \
             "or register a new category by typing it in the box on the right.\n" \
             "For new categories, please select whether the category should be considered a \n" \
             "fixed expense, variable expense, other expense, revenue or savings".format(self.new_statement)
        self.new_statement = text_processor(new_statement, bow = False)
        self.cat_db = request_db(os.path.join(admin_folder, "category_index.db"))
        self.exp_db = request_db(os.path.join(admin_folder, "expense_type_index.db"))
        
        self.setWindowTitle('Update Category Dictionary')
        self.resize(600, 400)
        
        self.mi.cbo_cats.setVisible(True)
        self.mi.txt_newCat.setVisible(True)
        self.mi.push_cancel.setVisible(True)
        
        self.mi.push_cancel.setGeometry(QtCore.QRect(30, 250, 140, 40))
        self.mi.push_OK.setGeometry(QtCore.QRect(200, 250, 200, 40))
        
        self.mi.cbo_cats.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mi.txt_newCat.textChanged.connect(self.new_cat)
        
        self.mi.cbo_expenseType = QtWidgets.QComboBox(self)
        self.mi.cbo_expenseType.setGeometry(QtCore.QRect(300, 200, 250, 30))
        self.mi.cbo_expenseType.setObjectName("cbo_expense_type")
        self.mi.cbo_expenseType.setVisible(False)
        self.mi.cbo_expenseType.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        #populate combo box with the categories in the database, sorted by number of occurences
        temp_cats = [a for a,b in self.cat_db.fetch_all('categories')]
        temp_expense_types = [b for a,b in self.exp_db.fetch_all('expense_type')]
            
        #listing categories based on most popular
        self.mi.cbo_cats.addItems(sorted(set(temp_cats), key = Counter(temp_cats).get, reverse=True))
        self.mi.cbo_expenseType.addItems(set(temp_expense_types))
        self.mi.lbl_message.setText(self.msg_txt)
        self.mi.lbl_message.setFont(bold_font)
        self.mi.push_OK.clicked.connect(self.register_statement)
        self.mi.push_cancel.clicked.connect(self.close)
    
    def new_cat(self):
        if self.mi.txt_newCat.text() == '':
            self.mi.cbo_cats.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.mi.cbo_expenseType.setVisible(False)
        else:
            self.mi.cbo_cats.setStyleSheet("background-color: rgb(167, 176, 168);")
            self.mi.cbo_expenseType.setVisible(True)
            
    def register_statement(self):
    
        if self.mi.txt_newCat.text() == '':
            cat = self.mi.cbo_cats.currentText()
        else:
            cat = self.mi.txt_newCat.text()
            
        #writing category to db
        self.cat_db.write_db(col1_var = cat, 
                             col2_var = self.new_statement, table_name = 'categories')
        
        #writing expense type to db
        if self.mi.cbo_expenseType.isVisible() == True:
            self.exp_db.write_db(col1_var = cat, 
                                 col2_var = self.mi.cbo_expenseType.currentText(), 
                                 table_name = 'expense_type')
        
        self.close()
            
            
class MessageBoxPrompt(MessageBox):
    def __init__(self, msg_txt = None, parent = None):
        super().__init__(msg_txt)
        self.msg_txt = msg_txt
        self.window_return = None
        
        self.setWindowTitle('Prompt for Updating Category Dictionary')
        
        self.mi.push_cancel.setVisible(True)
        self.mi.lbl_message.setText(msg_txt)
        self.mi.lbl_message.setFont(bold_font)
        
        
        self.mi.push_OK.clicked.connect(self.prompt_OK)
        self.mi.push_cancel.clicked.connect(self.prompt_cancel)
         
    def prompt_OK(self):
        self.done(1)
        
    def prompt_cancel(self):
        self.done(0)
        

class MessageBoxRemoveCat(MessageBox):
    def __init__(self, msg_txt = None, parent = None):
        super().__init__(msg_txt)
        self.msg_txt = 'Select a Category in the drop-down list to delete it from the classifier\n' \
                        'WARNING: Removing the category will also remove any statements in\n' \
                        'the database. Select OK to remove category, or select CANCEL to exit'

                                      
        self.setWindowTitle('Remove a Category')
        self.type_db = request_db(os.path.join(admin_folder, "type_index.db"))
        self.cat_db = request_db(os.path.join(admin_folder, "category_index.db"))
        
        
        self.mi.cbo_cats.setVisible(True)
        self.mi.txt_newCat.setVisible(False)
        self.mi.push_cancel.setVisible(True)
        self.mi.cbo_cats.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        #populate combo box with the categories in the database, sorted by Alphabetical Order

        temp_cats = [a for a,b in self.cat_db.fetch_all('categories')]
        temp_cats.append('')
        temp_cats = sorted(set(temp_cats))
            
        self.mi.cbo_cats.addItems(temp_cats)
        self.mi.lbl_message.setText(self.msg_txt)
        self.mi.lbl_message.setFont(bold_font)
        self.mi.push_OK.clicked.connect(self.remove_cat)
        self.mi.push_cancel.clicked.connect(self.close)
        
        
    def remove_cat(self):
        if self.mi.cbo_cats.currentText() == '':
            self.close()
        else:
            cat = self.mi.cbo_cats.currentText()
            #Removing cat from type db
            self.type_db.delete_cat(table_name = 'types', cat_name = cat)
            
            #Removing cat from category db
            self.cat_db.delete_cat(table_name = 'categories', cat_name = cat)
            
            self.close()
            
            self.window_success = MessageBoxSuccess('Successfully removed {} from databases'.format(cat))
            self.window_success.show()
            

    def closeEvent(self, event):
        #The following method returns the user to main screen if window is exited from action bar
        self.main_window = MainWindow()
        self.main_window.show()
        event.accept()
        
class MessageBoxRemoveStatement(MessageBox):
    def __init__(self, msg_txt = None, parent = None):
        super().__init__(msg_txt)
        
        self.msg_txt = 'Select a statement in the drop-down list on the right to delete it\n' \
            'from the classifier. Use the drop-down on the left to filter by category.\n' \
                'Select OK to remove statement, or select CANCEL to exit'

                                      
        self.setWindowTitle('Remove a Statement from a Category')
        self.cat_db = request_db(os.path.join(admin_folder, "category_index.db"))
        
        
        self.mi.cbo_cats.setVisible(True)
        #In this particular instance, creating a new combo box to be used instead of the text box
        self.mi.txt_newCat.setVisible(False)
        
        self.mi.cbo_statements = QtWidgets.QComboBox(self)
        self.mi.cbo_statements.setGeometry(QtCore.QRect(300, 160, 250, 30))
        self.mi.cbo_statements.setObjectName("cbo_statements")
        self.mi.cbo_statements.setVisible(True)
        self.mi.cbo_statements.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.mi.push_cancel.setVisible(True)
        self.mi.cbo_cats.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        
        #populate combo box with the categories in the database, sorted by Alphabetical Order
        temp_cats = [a for a,b in self.cat_db.fetch_all('categories')]
        temp_cats.append('All')
        temp_cats = sorted(set(temp_cats))
        
        #Initially populating combo box with all statements
        temp_statements = sorted([b for a, b in self.cat_db.fetch_all('categories')])
        
        self.mi.cbo_cats.addItems(temp_cats)
        self.mi.cbo_statements.addItems(temp_statements)
        
        self.mi.lbl_message.setText(self.msg_txt)
        self.mi.lbl_message.setFont(bold_font)
        
        self.mi.cbo_cats.currentTextChanged.connect(self.update_statements)
        self.mi.push_OK.clicked.connect(self.remove_statement)
        self.mi.push_cancel.clicked.connect(self.close)
        
    def update_statements(self):
        cat = self.mi.cbo_cats.currentText()
        self.mi.cbo_statements.clear()
        
        if cat == 'All':
            all_statements = sorted([b for a, b in self.cat_db.fetch_all('categories')])
            self.mi.cbo_statements.addItems(all_statements)
        else:
            db_pull = self.cat_db.get_statements(category = cat)
            statements = sorted([b for a,b in db_pull])
            self.mi.cbo_statements.addItems(statements)
        
    
    def remove_statement(self):
        statement = self.mi.cbo_statements.currentText()
        
        #Removing statement from category db
        self.cat_db.delete_statement(table_name = 'categories', statement_name = statement)
        
        self.close()
        
        self.window_success = MessageBoxSuccess('Successfully removed {} from databases'.format(statement))
        self.window_success.show()
        

    def closeEvent(self, event):
            #The following method returns the user to main screen if window is exited from action bar
            self.main_window = MainWindow()
            self.main_window.show()
            event.accept()


#Initiating the main program and shutting down when closed        
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())
        
        

        
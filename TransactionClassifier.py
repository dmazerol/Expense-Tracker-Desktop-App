# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:27:35 2021

@author: Dillon Mazerolle


The content of this module contains the classifier methods used in the transaction
classification algorithm.For now, the "classic classifier" is used, which simply
looks to see if any component of the category database is in the bag of words
from the transaction.

Expanded functionality is to include more complex machine learning algorithms
for transaction classification. At this stage, not enough data is available to 
justify use of such approaches.
"""

import numpy as np
import pandas as pd
import csv
import os
import sqlite3
#from sklearn.feature_extraction.text import TfidfVectorizer

class KeywordClassifier():
    
    def __init__(self, category_db, type_db, admin_folder):
        self.category_db = category_db
        self.type_db = type_db
        self.admin_folder = admin_folder
    
    
    def category_dict(self):
        '''Returns dictionary of categories and keywords from local database'''
        
        categories = {}
        con = sqlite3.connect(self.category_db)
        c = con.cursor()
        for row in c.execute("SELECT * FROM categories"):
            if row[0] in categories.keys():
                    categories[row[0]].append(row[1].lower())
            else:
                categories[row[0]] = [row[1].lower()]
        con.close()
        return categories
                
    
    def type_dict(self):           
        '''Returns a dictionary of transaction types from local database'''
        
        types = {}
        con = sqlite3.connect(self.type_db)
        c = con.cursor()
        for row in c.execute("SELECT * FROM types"):
            if row[0] in types.keys():
                    types[row[0]].append(row[1].lower())
            else:
                types[row[0]] = [row[1].lower()]
        con.close()
        return types
    
    
    def classic_classifier(self, df_type, df_description, types, categories):
        '''
        Determines the category of a transaction statement based on established keywords
    
        Parameters
        ----------
        df_type : string
            Transaction type in row of dataframe
        df_description : string
            Transaction statement description in row of dataframe
        types : dictionary
            dictionary of transaction types as keys and keywords as values
        categories : dictonary
            dictonary of categories as keys and keywords as values
    
        Returns
        -------
        category of transaction statement based on transaction type/statement and set dictionaries
    
        '''
        temp_list = []
        for key, value in types.items():
            for i in value:
                if i in df_type.lower() and i not in temp_list:
                    if key not in temp_list:
                        temp_list.append(key)
        if len(temp_list) != 0:
            return " , ".join(temp_list)
        else:
            for key, value in categories.items():
                for i in value:
                    if i.lower() in df_description.lower() and i not in temp_list:
                        if key not in temp_list:
                            temp_list.append(key)
            if len(temp_list) == 0:
                return 'unclassified'
            else:
                return " , ".join(temp_list)
        
# class ML_classifier():
    
#     def __init__(self, df_type, df_description, df_amount):
#         self.df_type = df_type
#         self.df_description = df_description
#         self.df_amount = df_amount
        
    
    
'''
Space to build in option for statement classification algorithm.

Considerations: 
    -would need some type of pre-categorized training set anyways for ML algorithm, which is already being done in the keyword index search method
    -the keyword search index method is likely very inefficient for large data sets, and thus the use of vectorization/ML algorithms likely more suitable
    -some form of unsupervised learning algorithm may be more appropriate (# clusters = # categories), but would still need mapping after the fact
    -for supervised learning, need to find way to combine spare matrices of description, purchase type and the amount value to predict the label (category)                                                                       

classification = input('Indicate which type of classifier you would like to run: \n\n' \
                       + ' Keyword Search = 1 \n Random Forest = 2 \n NLP = 3 \n None = 4 \n\n')

for column in df_cleaned[['Description', 'Type', 'Description_BOW']]:
    vectors = TfidfVectorizer().fit_transform(df_cleaned[column].values)
    
if classification == 1:
    #simply using keyword index as classifier
    classifier = KeywordClassifier()
    categories = classifier.category_dict()
    types = classifier.type_dict()
    df_cleaned.loc[:, 'Category'] = df_cleaned.apply(lambda x: classifier.classic_classifier(x['Type'], x['Description_BOW'], types, categories), axis=1)
elif classification == 2:
    #using the random forest classifier for expenses categorization
    
elif classification == 3:
    pass
else:
    exit
'''    

   
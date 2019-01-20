
# coding: utf-8

# In[4]:


import sqlite3
import json
import requests
import sync

class Base_Calculation(object):                     # Creating Base_Calculation class
    
    
    def __init__(self):                             # initiating objects of Base_Calculation
        
        pass
    
    
    def base_calc(self):

        obj = sync.Sync()

        name = obj.db_name()

        # Creating a connection object, conn to connect our database

        conn = sqlite3.connect(str(name) + ".sqlite")

        # Creating cursor

        cursor = conn.cursor()

        # Extracting transaction_id and amount from TransactionItems table and appending to lists

        cursor.execute("""SELECT * FROM TransactionItems""")

        transaction_items = cursor.fetchall()

        transaction_id = []

        amount = []


        for i in transaction_items:

            transaction_id.append(i[1])

            amount.append(i[3])

        # Extracting date and currency in accordance to transaction_id list sequence

        date = []

        currency = []


        for i in transaction_id:

            command =  "SELECT date, currency FROM Transactions INNER JOIN TransactionItems ON TransactionItems.transactionID = Transactions.transactionID WHERE Transactions.transactionID = " + str(i)

            cursor.execute(command)

            date_currency = cursor.fetchone()

            # Appending date to the list, date

            date.append(date_currency[0])

            # Appending currency to the list, currency

            currency.append(date_currency[1])

        # Base calculation for each element of the list, amount, and appending to the new list, base

        base = []

        for i in range(len(transaction_id)):

            date_ = date[i]

            # API access key

            access_key = "bbf1c9d89395edb246b1693a2bfe4881"

            # Getting the URL sorted out

            url = str("http://data.fixer.io/api/" + date_ + "?access_key=" + access_key + "&base=EUR")

            # Getting historical currency exchange data

            response_historical = requests.get(url)

            # Making the data into json datatype

            curr_exc_historical = response_historical.json()

            # Getting the equivalent amount of the currency to EUR

            curr_to_euro = curr_exc_historical['rates'][currency[i]]

            # Calculating the amount in EUR

            base_calc = round(amount[i] / curr_to_euro, 2)

            # Appending it to the list, base

            base.append(base_calc)

        # Updating the baseAmount column of TransactionItems table

        for i in range(len(base)):

            command =  "UPDATE TransactionItems SET baseAmount = " + str(base[i]) + " WHERE transactionID = " + str(transaction_id[i])

            with conn:

                cursor.execute(command)

        conn.close()

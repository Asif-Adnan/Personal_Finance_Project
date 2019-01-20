import sqlite3
import sync

class Income(object):
    
    def __init__(self):
        pass

    def income_input(self):

        '''
                                 |||Sonya's Part for Income.py|||

        Insertion of rows to Categories and Subcategories tables is implemented in sync.py file in the part
        of creation of appropriate tables.

        P.S. The Sonya's part has been commented out in sync.py file.
        '''


        '''
                                |||Asif's Interface Part for income.py Starts Here|||
        '''

        obj = sync.Sync()

        name = obj.db_name()

        # Creating a connection object, conn to connect our database

        conn = sqlite3.connect(str(name) + ".sqlite")

        # Creating cursor

        cursor = conn.cursor()

        # Creating subcategoryID and subcategory lists to be populated with retrieved data from the database

        subcategoryID = []

        subcategory = []

        # Retrieving subcategoryID and subcategory elements from Subcategories table and appending to lists, subcategoryID and subcategory

        cursor.execute("""SELECT subcategoryID, subcategory FROM Subcategories WHERE category = 'Income'""")

        subcagtegoryID_subcategory = cursor.fetchall()

        # Populating subcategoryID and subcategory lists

        for i in range(len(subcagtegoryID_subcategory)):
            subcategoryID.append(subcagtegoryID_subcategory[i][0])

            subcategory.append(subcagtegoryID_subcategory[i][1])

        # Showing a list of subcategories for the user to choose from

        print("\nPlease enter the number of the Subcategory that you want to select. (i.e. enter 1 to select Salary)\n")

        length = len(subcategory) + 1

        turn = 1

        while turn < length:

            for i in subcategory:
                print(turn, "-", i)

                turn += 1

        # Taking the number of the chosen subcategory

        subcategory_number = int(input())

        # Getting the selected subcategory and subcategoryID from their respective lists

        for i in range(1, length):

            if subcategory_number == i:

                subcategory_selected = str(subcategory[subcategory_number - 1])

                subcategoryID_of_subcategory = str(subcategoryID[subcategory_number - 1])

            else:

                continue

        # Asking the user to enter date

        print("\nPlease enter the date in sequence.\nFirst, year.\nSecond, month.\nThird, day.\n")

        while True:

            year = input("Year (i.e. 2018) :\n", )

            if year.isdigit() == True:

                if len(year) == 4:

                    break

                elif len(year) < 4:

                    print("\nPlease enter year in four digits. (i.e. 1991)\n")

                    continue

            else:

                print("\nPlease enter year in digits within 1 to 12.\n")

                continue

        while True:

            month = input("\nMonth (i.e. 07 for July, 12 for December etc.) :\n", )

            if month.isdigit() == True and int(month) >= 1 and int(month) <= 12:

                if len(month) == 2:

                    break

                elif len(month) < 2:

                    month = "0" + month

                    break

            else:

                print("\nPlease enter month in digits.\nP.S. The number should be within and including 1 to 12.\n")

                continue

        while True:

            day = input("\nDay (i.e. 05, 22 etc) :\n", )

            if day.isdigit() == True and int(day) >= 1 and int(day) <= 31:

                if len(day) == 2:

                    break

                elif len(day) < 2:

                    day = "0" + day

                    break

            else:

                print("\nPlease enter day in digits.\nP.S. The number should be within and including 1 to 31.\n")

                continue

        date = str(year + "-" + month + "-" + day)

        # Asking the user to enter income amount

        while True:

            income_amount = input("\nEnter the amount of income: ", )

            if income_amount.isdigit() == True:

                if int(income_amount) == 0:

                    print("Please enter a valid income amount.")

                    continue

                else:

                    break

            else:

                if '.' in income_amount:

                    break

                else:

                    print("\nPlease enter income in digits. (i.e. 120)")

                    continue

        '''
                              |||Asif's Interface Part for income.py Ends Here|||
        '''

        '''
                           |||Sonya's Income Insertion into the Database Starts Here|||
        '''
        # Assigning the base currency, Euro, to currency variable

        currency = "EUR"

        # Inserting data into Transactions and TransactionItems tables

        with conn:
            cursor.execute("INSERT INTO Transactions (subcategoryID, date, description, currency) VALUES (?, ?, ?, ?)",
                           (subcategoryID_of_subcategory, date, subcategory_selected, currency))

        with conn:
            cursor.execute("INSERT INTO TransactionItems (Amount) VALUES (?)", (income_amount,))


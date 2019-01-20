from splitwise import Splitwise
import sqlite3
from splitwise.expense import Expense
from splitwise.user import ExpenseUser

class Sync(object):
    def __init__(self):
        pass

    def sync_process(self):
        #The settings dict is defined in advance as a template
        settings = {"consumer_key":'',
        "consumer_secret":'',
        "oauth_token":'',
        "oauth_token_secret":''
                    }

        # Read the settings.txt
        try:
            with open('Settings.txt', 'r') as file:
                for line in file:
                    phrases = line.split()
                    i = 0
                    while i < len(phrases):
                        if 'consumer_key:' in phrases[i]:
                            settings["consumer_key"] = str(phrases[i+1])
                        if 'consumer_secret:' in phrases[i]:
                            settings["consumer_secret"] = str(phrases[i + 1])
                        if 'oauth_token:' in phrases[i]:
                            settings["oauth_token"] = str(phrases[i + 1])
                        if 'oauth_token_secret:' in phrases[i]:
                            settings["oauth_token_secret"] = str(phrases[i + 1])
                        i += 1
        except FileNotFoundError:
            print("File doesn't exist in CWD.")
        except IOError:
            print("File is empty.")

        sObj = Splitwise(settings['consumer_key'], settings['consumer_secret'])
        oauth_info = {'oauth_token': settings['oauth_token'], 'oauth_token_secret': settings['oauth_token_secret']}
        sObj.setAccessToken(oauth_info)

        user = sObj.getCurrentUser()
        friends = sObj.getFriends()
        groups = sObj.getGroups()
        currencies = sObj.getCurrencies()
        categories = sObj.getCategories()
        expenses = sObj.getExpenses(limit=0)
        userId = user.getId()

        '''
                                                        |||Darina's part - checking whether SQlite database exists|||

                               Checks if database exists in CWD, if not - creates the database with all necessary tables
                               (sql code from manual database creation and insertion of dummy data from Sonya's part).

                               '''
        with sqlite3.connect(str(userId)+".sqlite")as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""CREATE TABLE Users
                           (userID int
                           primary key ,
                           name text
                           )""")
                conn.commit()
                cursor.execute("""INSERT INTO Users(userID,name) VALUES ("1","Sonya")""")
                conn.commit()
                cursor.execute("""INSERT INTO Users(userID, name) VALUES ("2","Darina")""")
                conn.commit()
                cursor.execute("""INSERT INTO Users(userID, name) VALUES ("3","Asif")""")
                conn.commit()
            except sqlite3.OperationalError:
                pass
            try:
                cursor.execute("""create table Groups
                (
                  groupID int
                    primary key,
                  "group" text
                )""")
                conn.commit()
                cursor.execute("""INSERT INTO Groups(groupID,"group") VALUES ("1","Birthday")""")
                conn.commit()
                cursor.execute("""INSERT INTO Groups(groupID,"group") VALUES ("2","Monthly")""")
                conn.commit()
                cursor.execute("""INSERT INTO Groups(groupID,"group") VALUES ("3","Settlement")""")
                conn.commit()
                cursor.execute("""INSERT INTO Groups(groupID,"group") VALUES ("4","Trivial")""")
                conn.commit()
            except sqlite3.OperationalError:
                pass
            try:
                cursor.execute("""create table Categories
                (
                  categoryID int
                    primary key,
                  category   text
                )""")
                conn.commit()
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("1","Entertainment")""")
                conn.commit()
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("2","Food&Drink")""")
                conn.commit()
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("3","Home")""")
                conn.commit()
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("4","Life")""")
                conn.commit()
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("5","Transportation")""")
                conn.commit()
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("6","Uncategorized")""")
                conn.commit()
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("7","Utilities")""")
                conn.commit()
                '''
                                                                |||Sonya's Part for Income.py|||

                                       Insertion of rows to Categories tables is implemented here.

                                       '''
                cursor.execute("""INSERT INTO Categories(categoryID,"category") VALUES ("100","Income")""")
                conn.commit()
            except sqlite3.OperationalError:
                pass
            try:
                cursor.execute("""create table Subcategories
                (
                  subcategoryID int
                    primary key,
                  subcategory   text,
                  category      text
                    constraint category
                    references Categories (category)
                )""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("1","Games","Entertainment")""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("2","Movies","Entertainment")""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("3","Music","Entertainment")""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("4","Other","Entertainment")""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("5","Sports","Entertainment")""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("6","Dining out","Food&Drink")""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("7","Groceries","Food&Drink")""")
                conn.commit()
                cursor.execute("""INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("8","Liquor","Food&Drink")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("9","Other","Food&Drink")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("10","Electronics","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("11","Furniture","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("12","Household supplies","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("13","Maintenance","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("14","Mortgage","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("15","Other","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("16","Pets","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("17","Rent","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("18","Services","Home")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("19","Clothing","Life")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("20","Gifts","Life")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("21","Insurance","Life")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("22","Medical expences","Life")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("23","Other","Life")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("24","Taxes","Life")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("25","Bicycle","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("26","Bus/train","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("27","Car","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("28","Gas/fuel","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("29","Hotel","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("30","Other","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("31","Parking","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("32","Plane","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("33","Taxi","Transportation")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("34","General","Uncategorized")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("35","Cleaning","Utilities")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("36","Electricity","Utilities")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("37","Heat/gas","Utilities")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("38","Other","Utilities")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("39","Trash","Utilities")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("40","TV/Phone/Internet","Utilities")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("41","Water","Utilities")""")
                conn.commit()
                '''
                                                |||Sonya's Part for Income.py|||

                       Insertion of rows to Subcategories tables is implemented here.

                       '''
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("101","Salary","Income")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("102","Business","Income")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("103","Gifts","Income")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("104","Grants","Income")""")
                conn.commit()
                cursor.execute(
                    """INSERT INTO Subcategories(subcategoryID,"subcategory",category) VALUES ("105","Other","Income")""")
                conn.commit()
            except sqlite3.OperationalError:
                pass
            try:
                cursor.execute("""create table Transactions
                (
                  transactionID int
                    primary key,
                  date          date,
                  groupID       int
                    constraint groupID
                    references Groups,
                  subcategoryID int
                    constraint subcategoryID
                    references Subcategories,
                  description   text,
                  currency      text,
                  updated       date time
                )""")
                conn.commit()
            except sqlite3.OperationalError:
                pass
            try:
                cursor.execute("""create table TransactionItems
                (
                  itemID        int
                    primary key,
                  transactionID int
                    constraint transactionID
                    references Transactions,
                  userID        int
                    constraint userID
                    references Users,
                  amount        float,
                  baseAmount    float
                )""")
                conn.commit()
            except sqlite3.OperationalError:
                pass

        #insert current User to the table Users
        with sqlite3.connect(str(userId)+".sqlite")as conn:
            Id = user.getId()
            userName = user.getFirstName() +' '+ user.getLastName()
            userUpdate = (Id, userName)
            try:
                script = "INSERT INTO Users (userID, name) VALUES (?, ?);"
                conn.execute(script, userUpdate)
            except sqlite3.IntegrityError:
                conn.execute("DELETE FROM Users WHERE Users.userID = (?)", (str(Id),))
                conn.commit()
                script = "INSERT INTO Users (userID, name) VALUES (?, ?);"
                conn.execute(script, userUpdate)
                conn.commit()
            else:
                conn.commit()

        #update groups Exception - not unique key
        with sqlite3.connect(str(userId)+".sqlite")as conn:
            for i in range(len(groups)):
                groupId = groups[i].getId()
                groupName = groups[i].getName()
                groupUpdate = (groupId, groupName)
                try:
                    script = "INSERT INTO Groups ('groupID', 'group') VALUES (?, ?);"
                    conn.execute(script, groupUpdate)
                except sqlite3.IntegrityError:
                    conn.execute("DELETE FROM Groups WHERE Groups.groupID = (?)", (str(groupId),))
                    conn.commit()
                    script = "INSERT INTO Groups ('groupID', 'group') VALUES (?, ?);"
                    conn.execute(script, groupUpdate)
                    conn.commit()
                else:
                    conn.commit()

        #update categories
        with sqlite3.connect(str(userId)+".sqlite")as conn:
            for i in range(len(categories)):
                curr_categoryId = categories[i].getId()
                categoryName = categories[i].getName()
                categoryUpdate = (curr_categoryId, categoryName)
                try:
                    script = "INSERT INTO Categories ('categoryID', 'category') VALUES (?, ?);"
                    conn.execute(script, categoryUpdate)
                except sqlite3.IntegrityError:
                    conn.execute("DELETE FROM Categories WHERE Categories.categoryID = (?)", (str(curr_categoryId),))
                    conn.commit()
                    conn.execute("DELETE FROM Categories WHERE (Categories.category = (?) AND Categories.categoryID != (?))",
                                 (str(categoryName), str(curr_categoryId)))
                    conn.commit()
                    script = "INSERT INTO Categories ('categoryID', 'category') VALUES (?, ?);"
                    conn.execute(script, categoryUpdate)
                    conn.commit()
                else:
                    conn.commit()
                    conn.execute("DELETE FROM Categories WHERE (Categories.category = (?) AND Categories.categoryID != (?))",
                                 (str(categoryName), str(curr_categoryId)))
                    conn.commit()

        #update subcategories
        with sqlite3.connect(str(userId)+".sqlite")as conn:
            for i in range(len(categories)):
                subcategories = categories[i].getSubcategories()
                for j in range(len(subcategories)):
                    subcategoryId = subcategories[j].getId()
                    subcategoryName = subcategories[j].getName()
                    categoryName = categories[i].getName()
                    subcategoryUpdate = (subcategoryId, subcategoryName, categoryName)
                    try:
                        script = "INSERT INTO Subcategories (subcategoryID, subcategory, category) VALUES (?, ?, ?);"
                        conn.execute(script, subcategoryUpdate)
                    except sqlite3.IntegrityError:
                        conn.execute("DELETE FROM Subcategories WHERE Subcategories.subcategoryID = (?)", (str(subcategoryId),))
                        conn.commit()
                        conn.execute("DELETE FROM Subcategories WHERE (Subcategories.subcategory = (?) AND Subcategories.subcategoryID != (?) AND Subcategories.category = (?))",
                            (str(subcategoryName), str(subcategoryId), str(categoryName)))
                        conn.commit()
                        script = "INSERT INTO Subcategories (subcategoryID, subcategory, category) VALUES (?, ?, ?);"
                        conn.execute(script, subcategoryUpdate)
                        conn.commit()
                    else:
                        conn.commit()
                        conn.execute(
                            "DELETE FROM Subcategories WHERE (Subcategories.subcategory = (?) AND Subcategories.subcategoryID != (?) AND Subcategories.category = (?))",
                            (str(subcategoryName), str(subcategoryId), str(categoryName)))
                        conn.commit()

        # insert new expense records (table Transactions)
        with sqlite3.connect(str(userId)+".sqlite")as conn:
            for i in range(len(expenses)):
                if expenses[i].getDeletedAt() == None:

                    expenseId = expenses[i].getId()
                    date = expenses[i].getDate()[0:10]
                    groupId = expenses[i].getGroupId()
                    subcategoryId = expenses[i].getCategory().getId()
                    description = expenses[i].getDescription()
                    currency = expenses[i].getCurrencyCode()
                    updated = expenses[i].getUpdatedAt()

                    expensesUpdate = (expenseId, date, groupId, subcategoryId, description, currency, updated)
                    try:
                        script = "INSERT INTO Transactions (transactionID, date, groupID, subcategoryID, description, currency, updated) VALUES (?, ?, ?, ?, ?, ?, ?);"
                        conn.execute(script, expensesUpdate)
                    except sqlite3.IntegrityError:
                        conn.execute("DELETE FROM Transactions WHERE Transactions.transactionID = (?)", (str(expenseId),))
                        conn.commit()
                        script = "INSERT INTO Transactions (transactionID, date, groupID, subcategoryID, description, currency, updated) VALUES (?, ?, ?, ?, ?, ?, ?);"
                        conn.execute(script, expensesUpdate)
                        conn.commit()
                    else:
                        conn.commit()
                else:
                    continue

        # insert entries in table TransactionItems
        with sqlite3.connect(str(userId)+".sqlite")as conn:
            itemId = 0
            for i in range(len(expenses)):
                if expenses[i].getDeletedAt() == None:
                    itemId += 1
                    expenseId = expenses[i].getId()
                    userId = Id#expenses[i].getCreatedBy().getId()
                    expenseUser = expenses[i].getCreatedBy()
                    for j in range(len(expenses[i].users)):
                        if userId != expenses[i].users[j].getId():
                            amount = 0
                        else:
                            amount = expenses[i].users[j].getPaidShare()
                            break
                    itemUpdate = (itemId, expenseId, userId, amount, 0)
                    try:
                        script = "INSERT INTO TransactionItems (itemID, transactionID, userID, amount, baseAmount) VALUES (?, ?, ?, ?, ?);"
                        conn.execute(script, itemUpdate)
                    except sqlite3.IntegrityError:
                        conn.execute("DELETE FROM TransactionItems WHERE TransactionItems.itemID = (?)", (str(itemId),))
                        conn.commit()
                        script = "INSERT INTO TransactionItems (itemID, transactionID, userID, amount, baseAmount) VALUES (?, ?, ?, ?, ?);"
                        conn.execute(script, itemUpdate)
                        conn.commit()
                    else:
                        conn.commit()
                else:
                    expenseId = expenses[i].getId()
                    conn.execute("DELETE FROM TransactionItems WHERE TransactionItems.transactionID = (?)", (str(expenseId),))
                    conn.commit()
                    continue

    def db_name(self):
        # The settings dict is defined in advance as a template
        settings = {"consumer_key": '',
                    "consumer_secret": '',
                    "oauth_token": '',
                    "oauth_token_secret": ''
                    }

        # Read the settings.txt
        try:
            with open('Settings.txt', 'r') as file:
                for line in file:
                    phrases = line.split()
                    i = 0
                    while i < len(phrases):
                        if 'consumer_key:' in phrases[i]:
                            settings["consumer_key"] = str(phrases[i + 1])
                        if 'consumer_secret:' in phrases[i]:
                            settings["consumer_secret"] = str(phrases[i + 1])
                        if 'oauth_token:' in phrases[i]:
                            settings["oauth_token"] = str(phrases[i + 1])
                        if 'oauth_token_secret:' in phrases[i]:
                            settings["oauth_token_secret"] = str(phrases[i + 1])
                        i += 1
        except FileNotFoundError:
            print("File doesn't exist in CWD.")
        except IOError:
            print("File is empty.")
        sObj = Splitwise(settings['consumer_key'], settings['consumer_secret'])
        oauth_info = {'oauth_token': settings['oauth_token'], 'oauth_token_secret': settings['oauth_token_secret']}
        sObj.setAccessToken(oauth_info)
        user = sObj.getCurrentUser()
        userId = user.getId()

        return userId
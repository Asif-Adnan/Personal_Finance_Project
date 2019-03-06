import sqlite3
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sync

class Reporting(object):
    
    def __init__(self):
        
        pass
    
    def create_report(self):
        
        obj = sync.Sync()

        name = obj.db_name()
        
        with sqlite3.connect(str(name) + ".sqlite") as conn:
            # income data
            cursor = conn.cursor()
            cursor.execute(
                """SELECT description FROM main.Transactions WHERE subcategoryID >= 101 and date >= '2018-06-01' and date <= '2018-06-31';""")
            incdeskj = cursor.fetchall()

            cursor.execute(
                """SELECT description FROM main.Transactions WHERE subcategoryID >= 101 and date >= '2018-05-01' and date <= '2018-05-31';""")
            incdeskm = cursor.fetchall()

            cursor.execute(
                """SELECT description FROM main.Transactions WHERE subcategoryID >= 101 and date >= '2018-04-01' and date <= '2018-04-31';""")
            incdeska = cursor.fetchall()

            cursor.execute("""SELECT amount FROM main.TransactionItems WHERE transactionID isnull;""")
            seq = cursor.fetchall()


            # expenses data
            cursor.execute(
                """SELECT description, amount FROM main.Transactions INNER JOIN TransactionItems I on Transactions.transactionID = I.transactionID WHERE date >= '2018-06-01' and date <= '2018-06-31' and amount>0;""")
            expj = cursor.fetchall()

            cursor.execute(
                """SELECT description, amount FROM main.Transactions INNER JOIN TransactionItems I on Transactions.transactionID = I.transactionID WHERE date >= '2018-05-01' and date <= '2018-05-31' and amount>0;""")
            expm = cursor.fetchall()

            cursor.execute(
                """SELECT description, amount FROM main.Transactions INNER JOIN TransactionItems I on Transactions.transactionID = I.transactionID WHERE date >= '2018-04-01' and date <= '2018-04-31' and amount>0;""")
            expa = cursor.fetchall()


        # Saving report to pdf
        a = str(datetime.date.today())
        t = str(datetime.datetime.now().time())

        hour = t[:2]
        min = t[3:5]
        sec = t[6:8]

        time = hour + "-" + min + "-" + sec

        with PdfPages(a + ' ' + time + '.pdf') as pdf:
            # Creation of pie charts of expenses for the last 3 months
            plt.figure(figsize=(3, 3))
            dfj = pd.DataFrame(expj, columns=['subcategory', 'amount'])
            june = dfj.plot(kind='pie', y='amount', autopct='%1.1f%%', startangle=90, shadow=False,
                            labels=dfj['subcategory'], legend=True, fontsize=14)
            june.set_title("Max Mustermann's Expenses for June")
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

            plt.figure(figsize=(3, 3))
            dfm = pd.DataFrame(expm, columns=['subcategory', 'amount'])
            june = dfm.plot(kind='pie', y='amount', autopct='%1.1f%%', startangle=90, shadow=False,
                            labels=dfj['subcategory'], legend=True, fontsize=14)
            june.set_title("Max Mustermann's Expenses for May")
            pdf.savefig()
            plt.close()

            plt.figure(figsize=(3, 3))
            dfa = pd.DataFrame(expa, columns=['subcategory', 'amount'])
            june = dfa.plot(kind='pie', y='amount', autopct='%1.1f%%', startangle=90, shadow=False,
                            labels=dfj['subcategory'], legend=True, fontsize=14)
            june.set_title("Max Mustermann's Expenses for April")
            pdf.savefig()
            plt.close()

            # Creation of column charts showing income vs expenses for the last 3 months
            plt.figure(figsize=(6, 8))
            list = [1, 2, 3]
            colj = ['red', 'red', 'blue']
            valj = [expj[0][1], expj[1][1], seq[0][0]]
            LABELSj = [expj[0][0], expj[1][0], incdeskj[0][0]]
            plt.bar(list, valj, color=colj, align='center')
            plt.xticks(list, LABELSj)
            plt.title("Max Mustermann's Expenses vs Income for June 2018")
            pdf.savefig()
            plt.close()

            plt.figure(figsize=(6, 8))
            list = [1, 2]
            colm = ['red', 'blue']
            valm = [expm[0][1], seq[1][0]]
            LABELSm = [expm[0][0], incdeskm[0][0]]
            plt.bar(list, valm, color=colm, align='center')
            plt.xticks(list, LABELSm)
            plt.title("Max Mustermann's Expenses vs Income for May 2018")
            pdf.savefig()
            plt.close()

            plt.figure(figsize=(6, 8))
            list = [1, 2]
            cola = ['red', 'blue']
            vala = [expa[0][1], seq[2][0]]
            LABELSa = [expa[0][0], incdeska[0][0]]
            plt.bar(list, vala, color=cola, align='center')
            plt.xticks(list, LABELSa)
            plt.title("Max Mustermann's Expenses vs Income for April 2018")
            pdf.savefig()
            plt.close()




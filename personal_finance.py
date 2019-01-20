
# coding: utf-8

# In[ ]:


import sqlite3
import base_calc
import sync
import income
import reporting

print("The syncing process has begun...\n")

# Splitwise sync process starts here

turn_one = sync.Sync()

turn_one.sync_process()

print("The syncing process has been completed.\n")

print("The base currency calculation process has begun...\n")

# Base calculation process starts from here

turn_two = base_calc.Base_Calculation()

turn_two.base_calc()

print("The base currency calculation process has been completed.\n")

print("The application is ready.\n")

# The user interface starts from here.

iterate = True

while iterate is True:
    
    command = int(input("\nWhat do you want to do?\nAttention: Please enter the number of the command that you want to execute (i.e. enter 1 to Add Income, enter 3 to Exit etc.)\n1 - Add Income\n2 - Get Report\n3 - Log Out\n", ))
    
    
    if command == 1:

        turn_three = income.Income()

        turn_three.income_input()

        continue
    
    if command == 2:
        
        print("\n\nProcess is running...\n")

        turn_four = reporting.Reporting()

        turn_four.create_report()

        print("Report has been created! Check the current directory.")

        continue
    
    if command == 3:
        
        print("\n\nYou have sucessfully logged out of the Personal Finance Application.\n\n")
        
        iterate = False


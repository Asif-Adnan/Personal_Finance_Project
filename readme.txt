_________________
REQUIRED PACKAGES
_________________

Please make sure that you have installed the following packages:

- splitwise
- sqlite3
- pandas
- matplotlib
- requests
- json


______________________________________
IMPORTANT INFO FOR APPLICATION RUNNING
______________________________________

Please make sure that all relevant files are in the same directory.

Please open personal_finance.py file and run it. Then database will be created automatically in the same directory with the name "[Max Mustermann's ID].sqlite".
After syncing process and base currency calculation process have been completed the application is ready for user input, which will be important for further reporting part.

***
ATTENTION: The base currency calculation process calls "https://fixer.io/" API for every single transaction record to be precise. As the Free Plan subscription of the API
only allows to call the API 1000 times per month, it is advisable to change the API key (access_key variable at the 84th syntax of base_calc.py file) by getting another Free 
Plan subscription with opeing a new account at "https://fixer.io/" after running the application for maximum 5 times.
***

It is recommended for user to start interacting with program adding income information.

Please input just the following values:
Choose Add Income (1), then any subcategary you wish (1-5), then please type current year (2018), June as month (6 or 06), any day (1-31),
and any income amount. Please repeat the following procedure of income insertion for year 2018 month 5, and afterwards the same procedure for year 2018 month 4.


***
ATTENTION: It is extremely important to add information on income for 2018 and the following months to get the report:
June (06), May (05), April (04), as the next part of reporting
visualizes data only for last three months (as was prescribed in
 the project description)
***

After you added income information on last three months, you can press (2) to Get Report. It will be saved in the same directory with the name of current date and time "YYYY-MM-DD HH-MM-SS.pdf".
When you open this pdf file, on first three pages you will see pie charts of Max Mustermann's expenses per subcategory for the last 3 months (one chart per month) visualizing information got 
from Splitwise. On the next three pages are column charts showing Max Mustermann's expenses vs income data get from user for the last 3 months.

To Log Out from the application please run (3).
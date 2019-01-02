"""Personal finance forecasting app written in python3."""

# Created by Thomas Hallett on 03/03/2017.
# Copyright © 2017 Thomas Hallett. All rights reserved.
# finance_tracker.py
# Finance Tracker

# Import libraries
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import expenses_list
import balance_list
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt

print()
print("---------------------- Finance Tracker ----------------------")
print()

# Initiates program !!! Won't be neccesary once the balance_array is built and imprortable
def init(start_date, end_date):
    """Function which initiates program."""
    # Populating account1 table dates which are not already populated
    for single_date in daterange(start_date, end_date):
        balance_array[single_date] = [single_date,0,0,0]
        balance_array[single_date][0] = Decimal("0")

# Used for rounding decimal values for currency use
def round_decimal(x):
  return x.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

# Defining daterange function
def daterange(start_date, end_date):
    """Function takes in a start and end date. A range is output."""
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

# Function which updates an expense
def update_expense(expense, new_value, date_from):
    """Function updates an expense in the expense array and updates the
    balance from a given date """
    pass

# Function which updates account1 table. !!!! Add in date from to function
def update_tables(date_from):
    """Function updates account1 table. Requires updating to edit any table."""
    # Looping through balance_array day by day
    for key, value in balance_array.items():
        if key > date_from:
            # key > start_date prevents out of bounds errors for day 1
            if key > start_date:
                # balance = previous day's balance
                balance_array[key] = balance_array[key - datetime.timedelta(days=1)]
            # Looping through expense_array a day at a time
            for row in expenses_array:
                # If the day of the month equals the date of an expense the balance is updated
                if int(key.strftime("%d")) ==  row[1]:
                    # balance = previous day's balance minus expenses
                    new_balance = round_decimal(balance_array[key][0] - Decimal(row[2]))
                    # Update balance array
                    balance_array[key][0] = Decimal(new_balance)



# Function which updates balance on a specified day
def update_balance(new_balance, update_date):
    """Function updates balance on specified day."""
    print("update_balance called")
    # Setting the balance on specified date and updating tables beyond
    balance_array[update_date][0] = round_decimal(Decimal(new_balance))
    update_tables(update_date)

def save_array():
    """Function which saves the balance array"""
    file = open("testfile.py", "w")
    # Initiating library within text file
    file.write("# This is a file to store the balances for this application\n")
    file.write("from decimal import Decimal, ROUND_HALF_UP\n")

    file.write("balance_save =")

    # Pringing balance_array line by line
    for date in balance_array:
        file.write(str(balance_array))
    file.close()

# Loading external databases
expenses_array = expenses_list.my_list
balance_array = balance_list.my_list

# Defining start and end dates
start_date = date(2017, 4, 2)
end_date = start_date + relativedelta(years=1) + datetime.timedelta(days=1)

# Initialising balance_array
init(start_date, end_date)

# Printing all lines from balance_array
# for key, value in balance_array.items():
#    print (key, value)

# Printing all lines from expenses_array
# print("All expenses in expense database:")
# for row in expenses_array:
#    print(row)

# Updating balance to correct value
update_balance(Decimal(12345),date(2017,5,21))

# Printing balance table after update
# print()
# print("Printing balance_array post-update")
#for key, value in balance_array.items():
#    print (key, value)

# plot_array_x = []
# plot_array_y = []

# for key, value in balance_array.items():
#    plot_array_x.append(value)
#    plot_array_y.append(int(key.strftime("%Y%m%d")))


# plt.plot(plot_array_x)
# plt.ylabel('Balance (£)')
# plt.show()

# something={}

# something["poo"] = [1,2,3,4]

# print("Pringing first item from array within 'something' library")
# print(something["poo"][0])

print()

# printing row from account1 for today
#selected_date = date.today()
#print("Selected date: " + selected_date.strftime("%d/%m/%y"))
#print(balance_array[date.today()])

# printing row from expenses for item internet
#selected_expense = "water"
#print("Selected expense: " + selected_expense)
#for row in expenses_array:
#   if row[0] == selected_expense:
#       print(str(row[0]) + ": " + str(row[2]) + " on " + str(row[1]))

save_array()

#import testfile


print()
print("---------------------- Execution Ended ----------------------")
print()

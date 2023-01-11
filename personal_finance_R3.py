import csv
import json
import functools

''' Expected achievements of this code:
1) Be able to read a CSV file including all of my chequing account transactions.
2) Use AI to recognize which category the transctions fitts (E.G. food, rent...).
3) Calculate de sum per category.
4) Print a chart showing the % used per category.
'''

MONTH = input("Choose a month (e.g. dec22 or nov22): ").lower()
# MONTH = "dec22"
file = f"bmo_{MONTH}.csv"

def sum(transactions):
    sum_transactions = 0
    for value in transactions:
        sum_transactions += float(value)
    return sum_transactions


with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    index = -1 
    list_cash_flow = []
    cash_flow = 0

    for row in csv_reader:
            if len(row) > 0:
                if index < 1:
                    pass
                    index += 1
                else:
                    print("\nTransaction {}:\n".format(index))
                    print(row[3:4])
                    index += 1
                    transaction_value = row[3:4]
                    list_cash_flow = transaction_value + list_cash_flow
                    print("\nCash flow's list= {}\n".format(list_cash_flow))
                    cash_flow = sum(list_cash_flow)
                    print('Cash flow = {}'.format(cash_flow))
                    print('\n- ' +'- '*100)

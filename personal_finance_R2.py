import csv
import json
import datetime
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

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    index = -1 
    list_cash_flow = []
    for row in csv_reader:
            if len(row) > 0:
                if index < 1:
                    pass
                    index += 1
                else:
                    print("\nTransaction {}:".format(index))
                    print(row[3:4])
                    transaction_value = row[3:4]
                    list_cash_flow = transaction_value + list_cash_flow
                    print('List of the Cash flow= {}'.format(list_cash_flow))
                    # cash_flow = sum(list_cash_flow)
                    # print('Cash flow= {}'.format(list_cash_flow))
                    # index += 1


class Transactions:
    def __init__(self, bank_card, transcation_type, date, amount, description):
        self.bank_card = bank_card
        self.transaction_type = transcation_type
        self.date = date
        self.description = description 

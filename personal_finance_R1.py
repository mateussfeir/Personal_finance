import csv
import json
import datetime

MONTH = input("Choose a month (e.g. dec22 or nov22): ").lower()
# MONTH = "dec22"
file = f"bmo_{MONTH}.csv"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    index = -1
    for row in csv_reader:
            if len(row) > 0:
                if index < 1:
                    pass
                    index += 1
                else:
                    print("\nTransaction {}:".format(index))
                    print(row[1:])
                    index += 1


class Transactions:
    def __init__(self, bank_card, transcation_type, date, amount, description):
        self.bank_card = bank_card
        self.transaction_type = transcation_type
        self.date = date
        self.description = description 

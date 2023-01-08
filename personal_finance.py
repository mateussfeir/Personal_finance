import csv
import datetime

# MONTH = input("Choose a month (e.g. dec22 or oct22): ").lower()
MONTH = "dec22"
file = f"bmo_{MONTH}.csv"

# with open("bmo_dec_2022.csv", 'r') as csv_file:
with open(file, mode='r') as csv_file:
    csvreader = csv.reader(csv_file)
    index = 1
    for row in csvreader:
        print("\nTransaction {}:".format(index))
        print(row[1:])
        index += 1


class Transactions:
    def __init__(self, bank_card, transcation_type, date, amount, description):
        self.bank_card = bank_card
        self.transaction_type = transcation_type
        self.date = date
        self.description = description 


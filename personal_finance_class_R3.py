import csv
from datetime import datetime

# Creating the constructor
class Transaction:
    def __init__(self, bank_card, type, date, value, counterpart):
        self.bank_card = bank_card
        self.type = type
        self.date = date
        self.value = float(value)
        self.counterpart = counterpart

running = True
while running:
    MONTH = input("Choose the mouth (e.g. dec22 or nov22): ")
    print('1) Show the transactions.')
    print("2) Show your cash flow's result.")
    print("q) Quit.")
    user_choice = input('Choose your option: ')
    index = -1
    list_cash_flow = []

    with open(f'bmo_{MONTH}.csv', mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            if len(row) > 0:
                if index >= 1:
                    transaction = Transaction(row[0], row[1], row[2], row[3], row[4])
                    if user_choice == '1':
                        print("Transaction {}:\n".format(index))
                        print('Date: {}'.format(datetime.strptime(transaction.date, "%Y%m%d").date()))
                        print("Value: {:.2f}$, Counterpart: {}".format(transaction.value, transaction.counterpart))
                        print('-'*100)
                        index += 1
                    elif user_choice == '2':
                        pass
                    elif user_choice == 'q':
                        running = False
                else:
                    pass
                    index += 1
print('User left.')

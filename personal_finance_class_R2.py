import csv

# Creating the constructor

class Transaction:
    def __init__(self, bank_card, type, date, value, counterpart):
        self.bank_card = bank_card
        self.type = type
        self.date = date
        self.value = float(value)
        self.counterpart = counterpart

index = -1
MONTH = input("Choose the mouth (e.g. dec22 or nov22): ")
print('1) Show the transactions')
print("2) Show your cash flow's result")
user_choice = input('Choose your option: ')
with open(f'bmo_{MONTH}.csv', mode = 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        if len(row) > 0:
            if index >= 1:
                transaction = Transaction(row[0], row[1], row[2], row[3], row[4])
                if user_choice == '1':
                    print("Transaction {}:\n".format(index))
                    print("Date: {}\nValue: {:.2f}$, Counterpart: {}\n".format(transaction.date, transaction.value, transaction.counterpart))
                    print('-'*100)
                    index += 1
            else:
                pass
                index += 1

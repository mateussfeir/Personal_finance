import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Creating the constructor
'''In this part we are separating all the categories, organizing in way to call them for each specifically function'''
class Transaction:
    def __init__(self, bank_card, type, date, value, counterpart):
        self.bank_card = bank_card
        self.type = type
        self.date = date
        self.value = float(value)
        self.counterpart = counterpart

running = True
transaction_list = []
transactions_by_date = {}   

# Function to sum the values

def sum(transaction_list):
    sum_transaction = 0
    for value in transaction_list:
        sum_transaction += float(value)
    return sum_transaction

# Interface loop

while running:
    MONTH = input("Choose the month (nov22, dec22, jan23 etc...): ")
    print('1) Output all the transactions.')
    print("2) Calculate the Cash Flow.")
    print("3) Calculate the daily Cash Flow.")
    print("4) Plot the cash flow's chart per day.")
    print("q) Quit.")
    user_choice = input('Choose your option: ')
    index = -1

    # Opening the csv file in the read mode

    with open(f'bmo_{MONTH}.csv', mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            if len(row) > 0:
                if index >= 1:

                    # Here we are calling the Class, the order of the row means the order of the arguments in the class
                    # For example: Bank card, type, date, value and counterpart

                    transaction = Transaction(row[0], row[1], row[2], row[3], row[4])
                    if user_choice == '1':
                        
                        # 1) Output all the transactions.
                        # Printing the transaction show the index

                        print("Transaction {}:\n".format(index))

                        # Printing the date and converting the value receive (20230103) in a date 2023/01/03

                        print('Date: {}'.format(datetime.strptime(transaction.date, "%Y%m%d").date()))

                        # Printing the value of the transaction with two decimal places

                        print("Value: {:.2f}$, Counterpart: {}".format(transaction.value, transaction.counterpart))
                        print('-'*100)

                        # Increasing the value of the index + 1 to go to the next transaction

                        index += 1

                    elif user_choice == '2':

                        # 2) Calculate the Cash Flow
                        # Appending all of the transaction values to the transaction list meanwhile the loop is running
                        # Then outside the loop we are gonna calculate the cash flow

                        transaction_list.append(transaction.value)

                    elif user_choice == '3' or user_choice == '4':

                        # 3) Calculate the daily Cash Flow
                        # Again converting the string in date

                        date = datetime.strptime(transaction.date, "%Y%m%d").date()

                        # Creating an if statement to sum just transaction in the same day

                        if date in transactions_by_date:

                            # If the date is already in the list, append the transaction in the same date

                            transactions_by_date[date].append(transaction.value)
                        else: 
                            
                            # If not, it will add the date if it's value

                            transactions_by_date[date] = [transaction.value]

                    elif user_choice == 'q':
                        running = False
                else:
                    pass
                    index += 1
    if user_choice == '2':

        # To calculate the cash flow we are calling the sum function that we craeted in the beggining of the code

        cash_flow = sum(transaction_list)

        # Printing the cash flow using two decimal places
        
        print("{}'s Cash Flow: {:.2f}$".format(MONTH, cash_flow))

    elif user_choice == '3':
        
        for date, values in transactions_by_date.items():

            # Sum the daily cash flow

            daily_cash_flow = sum(values)

            # Print the date and the daily cash flow

            print("Cash flow of {}: {:.2f}$".format(date, daily_cash_flow))
        
    elif user_choice == '4':
        cumulative_cash_flow = 0
        data_list = []
        value_list = []
        for date, values in transactions_by_date.items():

            daily_cash_flow = sum(values)
            cumulative_cash_flow += daily_cash_flow
            value_list.append(cumulative_cash_flow)
            data_list.append(date)
            
        # print('Data list: {}'.format(data_list))
        # print('List of values: {}'.format([format(value, '.2f') for value in value_list]))

        # Ploting the chart
        plt.plot(data_list, value_list)
        plt.title("{}'s Cash Flow".format(MONTH))
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.show()

print('User left.')

import csv
import matplotlib.pyplot as plt


''' Expected achievements of this code:
1) Be able to read a CSV file including all of my chequing account transactions.
2) Use AI to recognize which category the transctions fitts (E.G. food, rent...).
3) Calculate de sum per category.
4) Print a chart showing the % used per category.

Problems to solve: Im trying to filter just transaction from uber to create another list, but my code
isn't recognizing the string equality.

'''

MONTH = input("Choose a month (e.g. dec22 or nov22): ").lower()
file = f"bmo_{MONTH}.csv"
print('1) Run the code')
print("2) Plot the Cash Flow's chart")
user_choice = input('Insert your choice:')
cash_flow_list = []
transactions_list = []
index = -1
index_list = []
cash_flow = 0
list_debit = []
list_credit = []
list_uber = []

def sum(transactions):
    sum_transactions = 0
    for value in transactions:
        sum_transactions += float(value)
    return sum_transactions


def plot(list2, list1):
    plt.plot(list1, list2, color = 'green', marker='x')
    plt.title(MONTH + "'s Cash Flow")
    plt.xlabel('N of transactions', fontsize = 12)
    plt.ylabel('Value', fontsize = 12)
    plt.grid(True)
    plt.show()


if user_choice == "1":
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
                if len(row) > 0:
                    if index < 1:
                        pass
                        index += 1
                    else:
                        print("\nTransaction {}: {}\n".format(index, row[2:5]))
                        transaction_value = row[3:4]
                        transactions_list += transaction_value
                        print("\nTransactions list= {}\n".format(transactions_list))
                        cash_flow = sum(transactions_list)
                        cash_flow_list.append(cash_flow)
                        index += 1
                        print("{}'s Cash flow = {:.2f}$".format(MONTH, cash_flow))
                        if str(row[4:5]) in '[DN]UBER':
                            print('Working')
                        else:
                            print('Not working')
                        print('\n- ' +'- '*100)
                else:
                    pass
        for value in transactions_list:
            if float(value) < 0:
                list_debit.append(float(value))
            elif float(value) > 0:
                list_credit.append(float(value))
            else:
                print('Error')
        print('List of credit = {}'.format(list_credit))
        print('Total credit = {:.2f}$'.format(sum(list_credit)))
        print('List of debit = {}'.format(list_debit))
        print('Total debit = {:.2f}$'.format(sum(list_debit)))

if user_choice == '2':
    with open(file, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
                if len(row) > 0:
                    if index < 1:
                        pass
                        index += 1
                    else:
                        transaction_value = row[3:4]
                        transactions_list += transaction_value
                        cash_flow = sum(transactions_list)
                        cash_flow_list.append(cash_flow)
                        index += 1
                        index_list.append(index)
        plot(cash_flow_list, index_list)

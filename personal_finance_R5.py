import csv

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
    list_debit = []
    list_credit = []

    for row in csv_reader:
            if len(row) > 0:
                if index < 1:
                    pass
                    index += 1
                else:
                    print("\nTransaction {}: {}\n".format(index, row[2:5]))
                    index += 1
                    transaction_value = row[3:4]
                    list_cash_flow = transaction_value + list_cash_flow
                    print("\nCash flow's list= {}\n".format(list_cash_flow))
                    cash_flow = sum(list_cash_flow)
                    print("{}'s Cash flow = {:.2f}$".format(MONTH, cash_flow))
                    print('\n- ' +'- '*100)
            else:
                pass
    for value in list_cash_flow:
        if float(value) < 0:
            list_debit.append(float(value))
        elif float(value) > 0:
            list_credit.append(float(value))
        else:
            print('Error')
    print('List of credit = {}$'.format(list_credit))
    print('Total credit = {:.2f}$'.format(sum(list_credit)))
    print('List of debit = {}$'.format(list_debit))
    print('Total debit = {:.2f}$'.format(sum(list_debit)))

    

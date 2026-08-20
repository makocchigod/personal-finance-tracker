import json
import matplotlib.pyplot as plt
print("\n======================================\n\n      Personal Finance Tracker     \n\n======================================\n\n\n")

def error():
    print("Incorrect Value! ")
    input("... ")
def display(dictionary):
    print("----------")
    for key, value in dictionary.items():
        print(f"{key}: {value}")
def create_bar_chart(x, y, color, title, x_label, y_label):
    plt.bar(x, y, color=color)
    plt.title(f"{title}")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.axhline(0, color='black', linewidth=1.5, linestyle='-')
    plt.show()
def add_transaction():
    with open("transactions_database.json", "r") as f:
        transactions = json.load(f)
    if transactions:
        new_id = max(i["id"] for i in transactions) + 1
    else:
        new_id = 1
    amount = 0
    while True:
        transaction_type = input("Would you like to add the earnings or expenditure? ")
        if transaction_type.lower() == "expenditure" or transaction_type.lower() == "earnings":
            transaction_type = transaction_type.lower()
            break
        else:
            error()
            continue
    while True:
        try:
            amount = float(input("\nEnter the amount: "))
            if amount < 0:
                error()
                continue
            break
        except ValueError:
            error()
            continue
    category = input("Enter the category: ")
    desc = input("Enter the description: ")
    date = ""
    while True:
        try:
            date = str(input("\nEnter the date (yyyy-mm-dd): "))
            if 1000 > int(date[:4]) or int(date[:4]) > 9999:
                raise ValueError
            elif 1 > int(date[5:7]) or int(date[5:7]) > 12:
                raise ValueError
            elif 1 > int(date[8:10]) or int(date[8:10]) > 31:
                raise ValueError
            else:
                break
        except ValueError:
            error()
            continue
    transaction = {"id": new_id, "type": transaction_type, "amount": amount, "category": category, "description": desc, "date": date}
    transactions.append(transaction)
    with open("transactions_database.json", "w", encoding="utf-8") as f:
        json.dump(transactions, f, ensure_ascii=False, indent=4)

def display_transactions():
    with open("transactions_database.json", "r") as f:
        transactions = json.load(f)
        for i in transactions:
            display(i)
        input("... ")
def find_transactions():
    with open("transactions_database.json", "r") as f:
        transactions = json.load(f)
    id_value = '-'
    typeval = '-'
    amount1 = 'Any'
    amount2 = 'Any'
    cat = '-'
    date1 = 'Any'
    date2 = 'Any'
    while True:
        keyword = input(f"\n\n==========\nTRANSACTION BROWSER\nFilters:\n\n-id: {id_value}\n-Type: {typeval}\n-Amount: {amount1} - {amount2}\n-Category: {cat}\n-Date: {date1} - {date2}\n\n-Exit\n-Reset\n-Search\n>>> ").lower()

        if keyword == "id":
            while True:
                try:
                    id_value = int(input("Enter the id: "))
                    if id_value > 0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error()
                    continue
        elif keyword == "type":
            while True:
                try:
                    typeval = input("Enter the type (expenditure/earnings): ")
                    if typeval not in ["earnings", "expenditure"]:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    error()
                    continue
        elif keyword == "amount":
            while True:
                try:
                    amount1 = float(input("Enter the price range you want to search for; if you want a specific amount, enter the same value twice.\n>>> "))
                    amount2 = float(input("Enter the second value\n>>> "))
                    break
                except ValueError:
                    error()
                    continue
        elif keyword == "category":
            while True:
                try:
                    cat = input("Enter the category: ").lower()
                    break
                except ValueError:
                    error()
                    continue
        elif keyword == "date":
            date1 = ''
            date2 = ''
            while True:
                try:
                    date1 = input("Enter the date range you want to search for; if you want a specific date, enter the same value twice(yyyy-mm-dd): ")
                    year1 = int(date1[:4])
                    if 1000 > year1 or year1 > 9999:
                        raise ValueError
                    month1 = int(date1[5:7])
                    day1 = int(date1[8:10])
                    if 1 > month1 or month1 > 12:
                        raise ValueError
                    elif month1 == 2:
                        if day1 > 29:
                            raise ValueError
                    if 1 > day1 or day1 > 31:
                        raise ValueError
                    break
                except ValueError:
                    error()
                    continue
            while True:
                try:
                    date2 = input("Enter the second date: ")
                    year2 = int(date2[:4])
                    if 1000 > year2 or year2 > 9999:
                        raise ValueError
                    month2 = int(date2[5:7])
                    day2 = int(date2[8:10])
                    if 1 > month2 or month2 > 12:
                        raise ValueError
                    elif month2 == 2:
                        if day2 > 29:
                            raise ValueError
                    if 1 > day2 or day2 > 31:
                        raise ValueError
                    break
                except ValueError:
                    error()
                    continue
        elif keyword == "reset":
            id_value = '-'
            typeval = '-'
            amount1 = 'Any'
            amount2 = 'Any'
            cat = '-'
            date1 = 'Any'
            date2 = 'Any'
        elif keyword == "search":
            searches = transactions
            searches_id = []
            searches_type = []
            searches_amount = []
            searches_cat = []
            searches_date = []
            if id_value != '-':
                for i in searches:
                    if i["id"] == id_value:
                        searches_id.append(i)
                searches = searches_id
            if typeval != '-':
                for i in searches:
                    if i["type"].lower() == typeval.lower():
                        searches_type.append(i)
                searches = searches_type
            if amount1 != 'Any':
                for i in searches:
                    if amount2 >= i["amount"] >= amount1 or amount2 <= i["amount"] <= amount1:
                        searches_amount.append(i)
                searches = searches_amount
            if cat != '-':
                for i in searches:
                    if i["category"].lower() == cat:
                        searches_cat.append(i)
                searches = searches_cat
            if date1 != 'Any':
                for i in searches:
                    if date2 >= i["date"] >= date1 or date2 <= i["date"] <= date1:
                        searches_date.append(i)
                searches = searches_date
            for i in searches:
                display(i)
            input("... ")
        elif keyword == "exit":
            break
def delete_transactions():
    with open("transactions_database.json", "r") as f:
        transactions = json.load(f)
    new_transactions = []
    value = 0
    while True:
        try:
            value = int(input("Enter the id of transaction to delete: "))
            break
        except ValueError:
            error()
            continue
    for i in transactions:
        if i["id"] != value:
            new_transactions.append(i)
    with open("transactions_database.json", "w") as f:
        json.dump(transactions, f, ensure_ascii=False, indent=4)
    print("Deleted! ")
    input("... ")
def statistics():
    with open("transactions_database.json", "r") as f:
        transactions = json.load(f)
    chart_x = set()
    for i in transactions:
        chart_x.add(i["date"][:7])
    chart_y = []
    for i in chart_x:
        earnings = 0
        for j in transactions:
            if j["date"][:7] == i and j["type"] == "earnings":
                earnings += j["amount"]
            if j["date"][:7] == i and j["type"] == "expenditure":
                earnings -= j["amount"]
        chart_y.append(earnings)
    chart_x = list(chart_x)
    create_bar_chart(chart_x, chart_y, 'green', 'Monthly summary', 'Month', 'Earnings')
    months = set()
    for i in transactions:
        months.add(i["date"][:7])
    categories = set()
    for i in transactions:
        categories.add(i["category"])
    months = sorted(list(months))
    for i in months:
        chart_y = []
        for j in categories:
            earnings = 0
            for k in transactions:
                if k["date"][:7] == i and k["type"] == "expenditure" and k["category"] == j:
                    earnings -= k["amount"]
                if k["date"][:7] == i and k["type"] == "earnings" and k["category"] == j:
                    earnings += k["amount"]
            chart_y.append(earnings)
        categories = list(categories)
        create_bar_chart(categories, chart_y, 'red', i, 'Categories', 'Earnings')
    input("... ")
while True:
    choice = input("\n1. Add Transaction\n\n2. Display All Transactions\n\n3. Browse Transactions\n\n4. Statistics\n\n5. Delete Transaction\n\n6. Exit\n\n\nWhat would you like to do?: ")
    if choice == '6' or choice.lower() == 'exit':
        exit()
    elif choice == '1' or choice.lower() == 'add transaction' or choice.lower() == 'add':
        add_transaction()
    elif choice == '2' or choice.lower() == 'display' or choice.lower() == 'display all transactions':
        display_transactions()
    elif choice == '3' or choice.lower() == 'browse' or choice.lower() == 'browse transactions':
        find_transactions()
    elif choice == '5' or choice.lower() == 'delete' or choice.lower() == 'delete transaction':
        delete_transactions()
    elif choice == '4' or choice.lower() == 'statistics':
        statistics()
    else:
        error()
        continue
import csv
from datetime import datetime

FILE = "data.csv"

def add_expense():
    amount = input("Amount: ")
    category = input("Category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

def view_report():
    total = 0
    category_data = {}

    with open(FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            _, amount, category = row
            amount = float(amount)

            total += amount
            category_data[category] = category_data.get(category, 0) + amount

    print("Total खर्च:", total)
    print("Category-wise:")
    for k, v in category_data.items():
        print(k, ":", v)

def menu():
    while True:
        print("\n1.Add 2.Report 3.Exit")
        choice = input("Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_report()
        else:
            break

menu()
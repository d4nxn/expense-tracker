import json

transactions = [
    {
        "type" : "Income",
        "amount" : 3600,
        "description" : "Salary",
        "category" : "Work" 
    },
    {
        "type" : "Expense",
        "amount" : 250,
        "description" : "Groceries",
        "category" : "Food"
    }
]

def show_menu():
    print("\n1. Add income")
    print("2. Add expense")
    print("3. Show transactions")
    print("4. Show balance")
    print("5. Exit")

def show_transactions(transactions):
    for transaction in transactions:
        print(f"{transaction['type']}: {transaction['amount']} zl - {transaction['description']} ({transaction['category']})")

def show_balance(transactions):
    balance = 0

    for transaction in transactions:
        if transaction["type"] == "Income":
            balance += transaction["amount"]
        elif transaction["type"] == "Expense":
            balance -= transaction["amount"]

    print("Balance:", balance)

def add_expense(transactions):
    print("\nChoose a category: ")
    print("1. Food")
    print("2. Transport")
    print("3. Entertainment")
    print("4. Other")

    category_choice = input("Category: ")
    if category_choice == "1":
        category = "Food"
    elif category_choice == "2":
        category = "Transport"
    elif category_choice == "3":
        category = "Entertainment"
    else:
        category = "Other"
        
    amount = float(input("Amount: "))
    description = input("Description: ")

    transaction = {
        "type": "Expense",
        "category": category,
        "amount": amount,
        "description": description
    }

    transactions.append(transaction)
    save_transactions(transactions)
    print("Expense added!")

def add_income(transactions):
    print("\nChoose type of income: ")
    print("1. Salary")
    print("2. Side Hustle")
    print("3. Other")
    income_type = input("Type: ")
    if income_type == "1":
        income_category = "Salary"
    elif income_type =="2":
        income_category = "Side Hustle"
    else:
        income_category = "Other"
    amount = float(input("Amount: "))
    description = input("Description: ")

    transaction = {
        "type": "Income",
        "category" : income_category,
        "amount": amount,
        "description": description
    }

    transactions.append(transaction)
    save_transactions(transactions)
    print("Income added!")

def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)


while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_income(transactions)

    elif choice == "2":
        add_expense(transactions)

    elif choice == "3":
        show_transactions(transactions)

    elif choice == "4":
        show_balance(transactions)

    elif choice == "5":
        print("Have a nice day!")
        break

    else:
        print("Invalid option, please try again.")
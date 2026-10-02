_PATHWAY_EXPENSES_JSON = "week_8/expenses.json"
_PATHWAY_BUDGETS_JSON = "week_8/budgets.json"
_SLEEP_AMOUNT = 5
import json
import time



def sleep_for_a_while():
    time.sleep(_SLEEP_AMOUNT)

def add_expense(expense_amount, expense_category, expense_date, expense_note):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    data.append({"amount": expense_amount, "category": expense_category, "date": expense_date, "note": expense_note})
    with open(_PATHWAY_EXPENSES_JSON, "w") as file:
        json.dump(data, file)
    with open(_PATHWAY_BUDGETS_JSON, "r") as file:
        budgets = json.load(file)
    for budget in budgets:
        if budget['category'] == expense_category:
            budget['current_budget'] =  float(budget['current_budget']) - float(expense_amount)
            print(f"Updated budget for category {expense_category}: {budget['current_budget']}")
    with open(_PATHWAY_BUDGETS_JSON, "w") as file:
        json.dump(budgets, file)
        

def edit_expense(expense_index):
    sleep_for_a_while()
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    if 0 <= expense_index < len(data):
        expense = data[expense_index]
        print(f"Editing expense: {expense}")
        new_amount = input(f"Enter new amount (current: {expense['amount']}): ")
        new_category = input(f"Enter new category (current: {expense['category']}): ")
        new_date = input(f"Enter new date (current: {expense['date']}): ")
        new_note = input(f"Enter new note (current: {expense['note']}): ")
        expense['amount'] = new_amount
        expense['category'] = new_category
        expense['date'] = new_date
        expense['note'] = new_note
        with open(_PATHWAY_EXPENSES_JSON, "w") as file:
            json.dump(data, file)
        print(f"Updated expense: {expense}")
    else:
        print("Invalid expense index")

def remove_expense(expense_index):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    if 0 <= expense_index < len(data):
        user_confirmation = input(f"Are you sure you want to remove expense {data[expense_index]}? (yes/no): ")
        if user_confirmation.lower() == "yes":
            removed_expense = data.pop(expense_index)
            with open(_PATHWAY_EXPENSES_JSON, "w") as file:
                json.dump(data, file)
            with open(_PATHWAY_BUDGETS_JSON, "r") as file:
                budgets = json.load(file)
                for budget in budgets:
                    if budget['category'] == removed_expense['category']:
                        budget['current_budget'] = float(budget['current_budget']) + float(removed_expense['amount'])
                with open(_PATHWAY_BUDGETS_JSON, "w") as file:
                    json.dump(budgets, file)
            print(f"Removed expense: {removed_expense}")
        else:
            print("Expense removal cancelled")
    else:
        print("Invalid expense index")


def find_expense():
    expense_date = input("Enter the date of the expense (YYYY-MM-DD): ")
    expense_category = input("Enter the category of the expense: ")
    expense_amount = input("Enter the amount of the expense: ")
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    expense_index = -1
    for i, expense in enumerate(data):
        if expense['date'] == expense_date and expense['category'] == expense_category and expense['amount'] == expense_amount:
            expense_index = i
            break
    return expense_index

def view_all_expenses():
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for expense in data:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Note: {expense['note']}")


def view_expenses_by_category(category):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for expense in data:
        if expense['category'] == category:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Note: {expense['note']}")


def view_expenses_by_date(date):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for expense in data:
        if expense['date'] == date:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Note: {expense['note']}")


def view_all_categories():
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    categories = set(expense['category'] for expense in data)
    for category in categories:
        print(category)


def add_budget(budget_category, budget_monthly_amount):
    with open(_PATHWAY_BUDGETS_JSON, "r") as file:
        data = json.load(file)
    data.append({"category": budget_category, "monthly_amount": budget_monthly_amount, "current_budget": float(budget_monthly_amount)})
    with open(_PATHWAY_BUDGETS_JSON, "w") as file:
        json.dump(data, file)


def change_budget(budget_category, budget_monthly_amount, add_difference=False):
    with open(_PATHWAY_BUDGETS_JSON, "r") as file:
        budgets = json.load(file)
    for budget in budgets:
        if budget['category'] == budget_category:
            if add_difference:
                budget['current_budget'] = float(budget['current_budget']) + (float(budget_monthly_amount) - float(budget['monthly_amount']))
            budget['monthly_amount'] = budget_monthly_amount
    with open(_PATHWAY_BUDGETS_JSON, "w") as file:
        json.dump(budgets, file)
        

def next_month():
    with open(_PATHWAY_BUDGETS_JSON, "r") as file:
        budgets = json.load(file)
    for budget in budgets:
        budget['current_budget'] = float(budget['current_budget']) + float(budget['monthly_amount'])
    with open(_PATHWAY_BUDGETS_JSON, "w") as file:
        json.dump(budgets, file)


def view_all_budgets():
    with open(_PATHWAY_BUDGETS_JSON, "r") as file:
        budgets = json.load(file)
    for budget in budgets:
        print(f"Category: {budget['category']}, Monthly Amount: {budget['monthly_amount']}, Current Budget: {budget['current_budget']}")


while True:
    print("Welcome to the expense tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. edit an expense")
    print("4. View all Categories")
    print("5. move to next month")
    print("6. View all budgets")
    print("7. change/add a budget")
    print("8. remove an expense")
    print("9. Exit")
    
    user_choice = input("Enter your choice: ")
    
    if user_choice == "1":
        expense_amount = input("Enter expense amount: ")
        expense_category = input("Enter expense category: ")
        expense_date = input("Enter expense date (YYYY-MM-DD): ")
        expense_note = input("Enter expense note (optional): ")
        add_expense(expense_amount, expense_category, expense_date, expense_note)
        print(f"Added expense of {expense_amount} in category {expense_category}")
        
        
    elif user_choice == "2":
        user_input = input("Do you want to view all expenses? (yes/no): ")
        if user_input.lower() == "yes":
            view_all_expenses()
        elif user_input.lower() == "no":
            category_or_date = input("Do you want to view by category or date? (category/date): ")
            if category_or_date.lower() == "category":
                category = input("Enter category: ")
                view_expenses_by_category(category)
            elif category_or_date.lower() == "date":
                date = input("Enter date (YYYY-MM-DD): ")
                view_expenses_by_date(date)
        else:
            print("Invalid choice, please try again.")
    
    
    elif user_choice == "3":
        print("Edit an expense selected")
        expense_index = find_expense()
        edit_expense(expense_index)
            
            
    elif user_choice == "4":
        print("View all Categories selected")
        view_all_categories()
        
        
    elif user_choice == "5":
        print("Move to next month selected")
        next_month()
        
        
    elif user_choice == "6":
        print("View all budgets selected")
        view_all_budgets()
        
        
    elif user_choice == "7":
        user_input = input("Do you want to 'add' or 'change' a budget? ")
        if user_input.lower() == "add":
            budget_category = input("Enter the category for the budget: ")
            budget_monthly_amount = input("Enter the monthly budget amount: ")
            add_budget(budget_category, budget_monthly_amount)
            print(f"Added budget for category {budget_category} with monthly amount {budget_monthly_amount}")
        elif user_input.lower() == "change":
            budget_category = input("Enter the category for the budget: ")
            budget_monthly_amount = input("Enter the new monthly budget amount: ")
            user_input_now = input("Do you want to add the difference to the current budget? (yes/no): ")
            if user_input_now.lower() == "yes":
                change_budget(budget_category, budget_monthly_amount, add_difference=True)
            elif user_input_now.lower() == "no":
                change_budget(budget_category, budget_monthly_amount, add_difference=False)
            else:
                print("Invalid choice, please try again.")
        else:
            print("Invalid choice, please try again.")
        

    elif user_choice == "8":
        while True:
            expense_index = find_expense()
            if expense_index == -1:
                print("Expense not found.")
                break
            with open(_PATHWAY_EXPENSES_JSON, "r") as file:
                data = json.load(file)
            print({data[expense_index]})
            user_input = input("Are you sure you want to remove this expense? (yes/no): ")
            if user_input.lower() == "yes":
                remove_expense(expense_index)
            elif user_input.lower() == "no":
                exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
                if exit_or_try_again.lower() == "exit":
                    break
            else:
                exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
                if exit_or_try_again.lower() == "exit":
                    break


    elif user_choice == "9":
        print("Exiting program")
        exit()
    else:
        print("Invalid choice, please try again.")
    sleep_for_a_while()
    
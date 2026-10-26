import json
import time
import datetime

_PATHWAY_EXPENSES_JSON = "expenses.json"
_PATHWAY_BUDGETS_JSON = "budgets.json"
_PATHWAY_CATEGORIES_JSON = "categories.json"
_PATHWAY_INTERNAL_DATA_JSON = "internal_data.json"
_SLEEP_AMOUNT = 5
_SHOW_AMOUNT = 5
with open(_PATHWAY_INTERNAL_DATA_JSON, "r") as file:
    internal_data = json.load(file)
_HIGHEST_ID = internal_data[0]["highest_id"]


def expenses_section():
    print("Welcome to the Expenses section")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Edit an expense")
    print("4. Remove an expense")
    print("5. Back to main menu")
    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        add_expense()
        # expense_amount = input("Enter expense amount: ")
        # expense_category = input("Enter expense category: ")
        # expense_date = input("Enter expense date (YYYY-MM-DD): ")
        # expense_note = input("Enter expense note (optional): ")
        # add_expense(expense_amount, expense_category, expense_date, expense_note)
        # print(f"Added expense of {expense_amount} in category {expense_category}")

    elif user_choice == "2":
        view_expense()
        # user_input = input("Do you want to view all expenses? (yes/no): ")
        # if user_input.lower() == "yes":
        #     view_all_expenses()
        # elif user_input.lower() == "no":
        #     category_or_date = input("Do you want to view by category or date? (category/date): ")
        #     if category_or_date.lower() == "category":
        #         category = input("Enter category: ")
        #         view_expenses_by_category(category)
        #     elif category_or_date.lower() == "date":
        #         date = input("Enter date (YYYY-MM-DD): ")
        #         view_expenses_by_date(date)
        #     else:
        #         print("Invalid choice, please try again.")
        # else:
        #     print("Invalid choice, please try again.")

    elif user_choice == "3":
        edit_expense()
        # print("Edit an expense selected")
        # expense_index = find_expense()
        # edit_expense(expense_index)

    elif user_choice == "4":
        remove_expense()
        # while True:
        #     expense_index = find_expense()
        #     if expense_index == -1:
        #         print("Expense not found.")
        #         break
        #     with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        #         data = json.load(file)
        #     print(json.dumps(data[expense_index], indent=4))
        #     user_input = input("Are you sure you want to remove this expense? (yes/no): ")
        #     if user_input.lower() == "yes":
        #         remove_expense(expense_index)
        #     elif user_input.lower() == "no":
        #         exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
        #         if exit_or_try_again.lower() == "exit":
        #             break
        #     else:
        #         exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
        #         if exit_or_try_again.lower() == "exit":
        #             break

    elif user_choice == "5":
        return
    else:
        print("Invalid choice, please try again.")


def add_expense():
    expense_amount = input("Enter expense amount: ")
    expense_category, is_new_category = check_expense_category()
    expense_sub_category = input("Enter expense sub-category (optional): ")
    year, month, day = get_dates()
    expense_date = f"{year}-{month:02d}-{day:02d}"
    expense_note = input("Enter expense note (optional): ")
    print(f"Added expense of {expense_amount} in category {expense_category}")
    if is_new_category:
        with open(_PATHWAY_CATEGORIES_JSON, "r") as file:
            categories = json.load(file)
        categories[expense_category] = {
            "total_spent": expense_amount,
            "last_updated": str(datetime.date.today()),
            "total_expenses": 1
        }
        with open(_PATHWAY_CATEGORIES_JSON, "w") as file:
            json.dump(categories, file)
    elif not is_new_category:
        with open(_PATHWAY_CATEGORIES_JSON, "r") as file:
            categories = json.load(file)
        categories[expense_category]["total_spent"] += float(expense_amount)
        categories[expense_category]["last_updated"] = str(datetime.date.today())
        categories[expense_category]["total_expenses"] += 1
        with open(_PATHWAY_CATEGORIES_JSON, "w") as file:
            json.dump(categories, file)
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    with open(_PATHWAY_EXPENSES_JSON, "w") as file:
        data[str(len(data) + 1).zfill(9)] = {
            "id": str(len(data) + 1).zfill(9),
            "amount": expense_amount,
            "category": expense_category,
            "sub_category": expense_sub_category,
            "date": expense_date,
            "note": expense_note
        }
        json.dump(data, file)
    with open(_PATHWAY_BUDGETS_JSON, "r") as file:
        budgets = json.load(file)
    for budget in budgets:
        if budget['category'] == expense_category:
            budget['current_budget'] =  float(budget['current_budget']) - float(expense_amount)
            print(f"Updated budget for category {expense_category}: {budget['current_budget']}")
    with open(_PATHWAY_BUDGETS_JSON, "w") as file:
        json.dump(budgets, file)


# def check_expense_amount(expense_amount):
    # try:
    #     amount = float(expense_amount)
    #     if amount < 0:
    #         print("Expense amount cannot be negative.")
    #         return False
    #     return True
    # except ValueError:
    #     print("Invalid expense amount.")
    #     return False


def check_expense_category():
    print("Please enter the category.")
    while True:
        category = input()
        result = find_category(category)
        if result == None:
            print("This will create a new category.")
            print("Is this correct? (yes/no): ")
            confirmation = input()
            if confirmation.lower() == "yes" or confirmation.lower() == "y":
                return category, True
            elif confirmation.lower() == "no" or confirmation.lower() == "n":
                continue
        return category, False



def find_category(category):
    with open(_PATHWAY_CATEGORIES_JSON, "r") as file:
        data = json.load(file)
    if category in data:
        return data[category]
    return None


def print_expense(expense_index):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    if 0 <= expense_index < len(data):
        expense = data[expense_index]
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Sub-category: {expense['sub_category']}, Date: {expense['date']}, Note: {expense['note']}")


def view_expense():
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
    else:
        print("Invalid choice, please try again.")

def edit_expense():
    print("Edit an expense selected")
    expense_index = find_expense()
    #edit_expense(expense_index)
    sleep_for_a_while()
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    if 0 <= expense_index < len(data):
        expense = data[expense_index]
        print(f"Editing expense: {expense}")
        new_amount = input(f"Enter new amount (current: {expense['amount']}): ")
        new_category = input(f"Enter new category (current: {expense['category']}): ")
        new_sub_category = input(f"Enter new sub-category (current: {expense['sub_category']}): ")
        new_date = input(f"Enter new date (current: {expense['date']}): ")
        new_note = input(f"Enter new note (current: {expense['note']}): ")
        expense['amount'] = new_amount
        expense['category'] = new_category
        expense['sub_category'] = new_sub_category
        expense['date'] = new_date
        expense['note'] = new_note
        with open(_PATHWAY_EXPENSES_JSON, "w") as file:
            json.dump(data, file)
        print(f"Updated expense: {expense}")
    else:
        print("Invalid expense index")

def remove_expense():
    while True:
        expense_index = find_expense()
        if expense_index == -1:
            print("Expense not found.")
            break
        with open(_PATHWAY_EXPENSES_JSON, "r") as file:
            data = json.load(file)
        print_expense(expense_index)
        user_input = input("Are you sure you want to remove this expense? (yes/no): ")
        if user_input.lower() == "yes":
            with open(_PATHWAY_EXPENSES_JSON, "r") as file:
                data = json.load(file)
            if 0 <= expense_index < len(data):
                # user_confirmation = input(f"Are you sure you want to remove expense {data[expense_index]}? (yes/no): ")
                # if user_confirmation.lower() == "yes":
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
                return
            else:
                print("Invalid expense index")
        # else:
        #     print("Expense removal cancelled")
            
            #remove_expense(expense_index)
        elif user_input.lower() == "no":
            exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
            if exit_or_try_again.lower() == "exit":
                break
        else:
            exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
            if exit_or_try_again.lower() == "exit":
                break
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
    possible_expenses = []
    expense_index = -1
    expense_id = input("Please enter the ID of the expense: ")
    if expense_id != "":
        return str(int(expense_id) + 1)
    
    expense_category = input("Enter the category of the expense: ")
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for i, expense in enumerate(data):
        if expense['category'] == expense_category:
            possible_expenses.append(expense)
    if len(possible_expenses) == 0:
        print("No possible expenses found.")
    elif len(possible_expenses) == 1:
        for i, expense in enumerate(data):
            if expense['category'] == expense_category:
                expense_index = i
                return expense_index
    elif len(possible_expenses) <= _SHOW_AMOUNT:
        print("Possible expenses:")
        for expense in possible_expenses:
            print_expense(data.index(expense))

    expense_sub_category = input("Enter the sub-category of the expense: ")
    expenses = possible_expenses
    possible_expenses = []
    for i, expense in enumerate(expenses):
        if expense['sub_category'] == expense_sub_category:
            possible_expenses.append(expense)
    if len(possible_expenses) == 0:
        print("No possible expenses found.")
    elif len(possible_expenses) == 1:
        for i, expense in enumerate(data):
            if expense['sub_category'] == expense_sub_category:
                expense_index = i
                return expense_index
    elif len(possible_expenses) <= _SHOW_AMOUNT:
        print("Possible expenses:") 
        for expense in possible_expenses:
            print_expense(expense_index)   
    expense_date = input("Enter the date of the expense (YYYY-MM-DD): ")
    expenses = possible_expenses
    possible_expenses = []
    for i, expense in enumerate(expenses):
        if expense['date'] == expense_date:
            possible_expenses.append(expense)
    if len(possible_expenses) == 0:
        print("No possible expenses found.")
    elif len(possible_expenses) == 1:
        for i, expense in enumerate(data):
            if expense['date'] == expense_date:
                expense_index = i
                return expense_index
    elif len(possible_expenses) <= _SHOW_AMOUNT:
        print("Possible expenses:") 
        for expense in possible_expenses:
            print_expense(data.index(expense))
    expense_amount = input("Enter the amount of the expense: ")
    expenses = possible_expenses
    possible_expenses = []
    for i, expense in enumerate(expenses):
        if expense['amount'] == expense_amount:
            possible_expenses.append(expense)
    if len(possible_expenses) == 0:
        print("No possible expenses found.")
    elif len(possible_expenses) == 1:
        for i, expense in enumerate(data):
            if expense['amount'] == expense_amount:
                expense_index = i
                return expense_index
    elif len(possible_expenses) <= _SHOW_AMOUNT:
        print("Possible expenses:") 
        for expense in possible_expenses:
            print_expense(data.index(expense))
    expense_note = input("Enter the note of the expense: ")
    expenses = possible_expenses
    possible_expenses = []
    for i, expense in enumerate(expenses):
        if expense['note'] == expense_note:
            possible_expenses.append(expense)
    if len(possible_expenses) == 0:
        print("No possible expenses found.")
    elif len(possible_expenses) == 1:
        for i, expense in enumerate(data):
            if expense['note'] == expense_note:
                expense_index = i
                return expense_index
    elif len(possible_expenses) <= _SHOW_AMOUNT:
        print("Possible expenses:") 
        for expense in possible_expenses:
            print_expense(data.index(expense))
    # with open(_PATHWAY_EXPENSES_JSON, "r") as file:
    #     data = json.load(file)
    # for i, expense in enumerate(data):
    #     if expense['date'] == expense_date and expense['category'] == expense_category and expense['amount'] == expense_amount:
    #         expense_index = i
    #         break
    # return expense_index

def view_all_expenses():
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for expense in data:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Sub-category: {expense['sub_category']}, Date: {expense['date']}, Note: {expense['note']}")


def view_expenses_by_category(category):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for expense in data:
        if expense['category'] == category:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Sub-category: {expense['sub_category']}, Date: {expense['date']}, Note: {expense['note']}")


def view_expenses_by_date(date):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for expense in data:
        if expense['date'] == date:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Sub-category: {expense['sub_category']}, Date: {expense['date']}, Note: {expense['note']}")


def categories_section():
    print("Welcome to the Categories section")
    print("1. View all categories")
    print("2. Back to main menu")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        view_all_categories()
    
    elif user_input == "2":
        return
    
    else:
        print("Invalid choice, please try again.")


def view_all_categories():
    with open(_PATHWAY_CATEGORIES_JSON, "r") as file:
        data = json.load(file)
    categories = set(category for category in data)
    for category in categories:
        print(category)


def check_category_exists(category):
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    for expense in data:
        if expense['category'] == category:
            return True
    return False


def budgets_section():
    print("Welcome to the Budgets section")
    print("1. View all budgets")
    print("2. Add/change a budget")
    print("3. go to next month")
    print("4. Back to main menu")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        view_all_budgets()

    elif user_input == "2":
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
            
            
    elif user_input == "3":
        next_month()
        
    elif user_input == "4":
        return
    else:
        print("Invalid choice, please try again.")


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


def sleep_for_a_while():
    time.sleep(_SLEEP_AMOUNT)


def get_dates():
    print("Enter the date: YYYY-MM-DD")
    while True:
        date_input = input()
        try:
            year = int(date_input.split("-")[0])
            month = int(date_input.split("-")[1])
            day = int(date_input.split("-")[2])
            return year, month, day
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            print("Type exit to quit.")
        if date_input.lower() == "exit":
            return None, None, None


def end_prep():
    find_and_write_end_id()
    write_last_date()

def write_last_date():
    with open(_PATHWAY_INTERNAL_DATA_JSON, "r") as file:
        internal_data = json.load(file)
    internal_data[0]["last_date"] = str(datetime.date.today())
    with open(_PATHWAY_INTERNAL_DATA_JSON, "w") as file:
        json.dump(internal_data, file)

def find_and_write_end_id():
    with open(_PATHWAY_EXPENSES_JSON, "r") as file:
        data = json.load(file)
    max_id = max([int(expense_id) for expense_id in data.keys()]) if data else 0
    with open(_PATHWAY_INTERNAL_DATA_JSON, "r") as file:
        internal_data = json.load(file)
    internal_data[0]["highest_id"] = max_id
    with open(_PATHWAY_INTERNAL_DATA_JSON, "w") as file:
        json.dump(internal_data, file)


def main():
    while True:
        print("Welcome to the finance tracker")
        print("1. Expenses")
        print("2. Categories")
        print("3. Budgets")
        print("4. Exit")
        user_choice = input("Enter your choice: ")
        
        
        if user_choice == "1":
            expenses_section()
            # print("Welcome to the Expenses section")
            # print("1. Add expense")
            # print("2. View expenses")
            # print("3. Edit an expense")
            # print("4. Remove an expense")
            # print("5. Back to main menu")
            # user_choice = input("Enter your choice: ")
            # if user_choice == "1":
            #     expense_amount = input("Enter expense amount: ")
            #     expense_category = input("Enter expense category: ")
            #     expense_date = input("Enter expense date (YYYY-MM-DD): ")
            #     expense_note = input("Enter expense note (optional): ")
            #     add_expense(expense_amount, expense_category, expense_date, expense_note)
            #     print(f"Added expense of {expense_amount} in category {expense_category}")


            # elif user_choice == "2":
            #     user_input = input("Do you want to view all expenses? (yes/no): ")
            #     if user_input.lower() == "yes":
            #         view_all_expenses()
            #     elif user_input.lower() == "no":
            #         category_or_date = input("Do you want to view by category or date? (category/date): ")
            #         if category_or_date.lower() == "category":
            #             category = input("Enter category: ")
            #             view_expenses_by_category(category)
            #         elif category_or_date.lower() == "date":
            #             date = input("Enter date (YYYY-MM-DD): ")
            #             view_expenses_by_date(date)
            #         else:
            #             print("Invalid choice, please try again.")
            #     else:
            #         print("Invalid choice, please try again.")


            # elif user_choice == "3":
            #     print("Edit an expense selected")
            #     expense_index = find_expense()
            #     edit_expense(expense_index)


            # elif user_choice == "4":
            #     while True:
            #         expense_index = find_expense()
            #         if expense_index == -1:
            #             print("Expense not found.")
            #             break
            #         with open(_PATHWAY_EXPENSES_JSON, "r") as file:
            #             data = json.load(file)
            #         print(json.dumps(data[expense_index], indent=4))
            #         user_input = input("Are you sure you want to remove this expense? (yes/no): ")
            #         if user_input.lower() == "yes":
            #             remove_expense(expense_index)
            #         elif user_input.lower() == "no":
            #             exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
            #             if exit_or_try_again.lower() == "exit":
            #                 break
            #         else:
            #             exit_or_try_again = input("Expense not removed. Try again. Press Enter to continue or type 'exit' to quit: ")
            #             if exit_or_try_again.lower() == "exit":
            #                 break


            # elif user_choice == "5":
            #     continue
            # else:
            #     print("Invalid choice, please try again.")





        elif user_choice == "2":
            categories_section()
            # print("Welcome to the Categories section")
            # print("1. View all categories")
            # print("2. Back to main menu")
            # user_input = input("Enter your choice: ")
            # if user_input == "1":
            #     view_all_categories()

            # elif user_input == "2":
            #     continue

            # else:
            #     print("Invalid choice, please try again.")




        elif user_choice == "3":
            budgets_section()
            # print("Welcome to the Budgets section")
            # print("1. View all budgets")
            # print("2. Add/change a budget")
            # print("3. go to next month")
            # print("4. Back to main menu")
            # user_input = input("Enter your choice: ")
            # if user_input == "1":
            #     view_all_budgets()
            
            
            # elif user_input == "2":
            #     user_input = input("Do you want to 'add' or 'change' a budget? ")
            #     if user_input.lower() == "add":
            #         budget_category = input("Enter the category for the budget: ")
            #         budget_monthly_amount = input("Enter the monthly budget amount: ")
            #         add_budget(budget_category, budget_monthly_amount)
            #         print(f"Added budget for category {budget_category} with monthly amount {budget_monthly_amount}")
            #     elif user_input.lower() == "change":
            #         budget_category = input("Enter the category for the budget: ")
            #         budget_monthly_amount = input("Enter the new monthly budget amount: ")
            #         user_input_now = input("Do you want to add the difference to the current budget? (yes/no): ")
            #         if user_input_now.lower() == "yes":
            #             change_budget(budget_category, budget_monthly_amount, add_difference=True)
            #         elif user_input_now.lower() == "no":
            #             change_budget(budget_category, budget_monthly_amount, add_difference=False)
            #         else:
            #             print("Invalid choice, please try again.")
            #     else:
            #         print("Invalid choice, please try again.")
                
                
            # elif user_input == "3":
            #     next_month()
                
                
            # elif user_input == "4":
            #     continue
            # else:
            #     print("Invalid choice, please try again.")



        elif user_choice == "4":
            print("Exiting the finance tracker")
            end_prep()
            break




        else:
            print("Invalid choice, please try again.")



if __name__ == "__main__":
    main()



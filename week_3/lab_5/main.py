months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
current_month_index = 0
budget = 0
month_budget = 25
while True:
    user_input = input()
    if user_input == "next month":
        current_month_index = (current_month_index + 1) % 12
        budget += month_budget
        print(months[current_month_index])
        print("Budget:", budget)
    else:
        budget -= float(user_input)
        print("Budget:", budget)
        
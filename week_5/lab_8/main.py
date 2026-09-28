_PATHWAY_BUDGET = "week_5/lab_8/current_budget.txt"
_PATHWAY_HISTORY = "week_5/lab_8/history.txt"
with open(_PATHWAY_BUDGET, "r") as file:
    current_budget = float(file.read())
month_budget = 25
while True:
    user_input = input()
    if user_input == "next month":
        current_budget += month_budget
        with open(_PATHWAY_BUDGET, "w") as file:
            file.write(str(current_budget))
        with open(_PATHWAY_HISTORY, "a") as file:
            file.write(user_input + ", " + str(current_budget) + "\n")
        print("Budget:", current_budget)
    else:
        current_budget -= float(user_input)
        with open(_PATHWAY_BUDGET, "w") as file:
            file.write(str(current_budget))
        with open(_PATHWAY_HISTORY, "a") as file:
            file.write(user_input + ", " + str(current_budget) + "\n")
        print("Budget:", current_budget)
        
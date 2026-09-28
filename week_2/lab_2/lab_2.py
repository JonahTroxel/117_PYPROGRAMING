"""This program takes a user's score as input and determines the corresponding letter grade based on predefined minimum score thresholds for each grade. The thresholds are defined as constants at the beginning of the program. The program uses conditional statements to compare the user's score against these thresholds and prints the appropriate letter grade.
"""
_MIN_A = 90
_MIN_B = 80
_MIN_C = 70
_MIN_D = 60

user_score = int(input("Enter your score: "))

if user_score >= _MIN_A:
    print("Your grade is A.")
elif user_score >= _MIN_B:
    print("Your grade is B.")
elif user_score >= _MIN_C:
    print("Your grade is C.")
elif user_score >= _MIN_D:
    print("Your grade is D.")
else:
    print("Your grade is F.")
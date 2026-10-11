
# Broken Student Exam Score Calculator

scores = [80, 90, 70]

total = 0

for score in scores:
    total += score

average = total / len(scores)

print("Average score:", average)

if average >= 60:
    print("Student passed!")
else:
    print("Student failed!")

"""counting sequence
"""
start_num = int(input("Enter the starting number: "))
max_count = int(input("Enter the maximum count: "))
error = False
if start_num == max_count:
    print("No counting was done because the starting number is equal to the maximum count.")
    error = True
elif start_num > max_count:
    print("No counting was done because the starting number is greater than the maximum count.")
    error = True
while start_num < (max_count + 1) and error == False:
    print(start_num)
    start_num += 1

if not error:
    print("Counting complete.")
def calculate(first_num, sec_num, function):
    if function == "1":
        return first_num + sec_num
    elif function == "2":
        return first_num - sec_num
    elif function == "3":
        return first_num * sec_num
    elif function == "4":
        if sec_num != 0:
            return first_num / sec_num
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

def main():
    while True:    
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        function = input("Enter choice (1/2/3/4/5): ")
        if function == "5":
            print("Exiting the program.")
            break
        first_num = float(input("Enter first number: "))
        sec_num = float(input("Enter second number: "))

        result = calculate(first_num, sec_num, function)
        print(f"The result is: {result}")
        

if __name__ == "__main__":
    main()
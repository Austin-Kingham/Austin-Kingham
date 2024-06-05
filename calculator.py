operator = input("Enter an operator (+ - / *): ")
num_1 = float(input("Enter your 1st number: "))
num_2 = float(input("Enter your 2nd number: "))

if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "/":
    print(num_1 / num_2)
elif operator == "*":
    print(num_1 * num_2)
else:
    print(f"{operator} is not a valid operator")

    

def calc(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        return num1/num2
    else:
        print("operation invalid")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (addition, subtraction, multiplication, division: ")

result = calc(num1, num2, operation)
print(result)
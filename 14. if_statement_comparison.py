

def max_num(num1, num2, num3):
# Fist Implementation

#     if num1 > num2:
#         largest = num1
#     else:
#         largest = num2
#
#     if num3 > largest:
#         largest = num3
#
#     return largest

# Second Implementation
    if  num1 > num2 and num1 >num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = max_num(num1, num2, num3)
print("Largest number is ", + result)

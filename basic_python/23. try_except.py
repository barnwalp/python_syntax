

# This is too broad exception and will catch any
# exceptions or error like the statement in line 10
try:
    number = int(input("Enter a number: "))
    print(number)
    # following line also cause the console to
    # print invalid error
    value = 10 / 0
except:
    print("invalid input")

# Better way to catch error is to specify the error
try:
    number = int(input("Enter a number: "))
    print(number)
    value = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
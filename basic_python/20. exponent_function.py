
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(int(pow_num)):
        result = result * base_num
    return result

base_num = float(input("Enter base number: "))
pow_num = float(input("Enter power number: "))

print(raise_to_power(base_num, pow_num))

# modes are 'r', 'w', 'a', 'r+'
employee_file = open("employee.txt", "r")
# print(employee_file.read())
# print("-------------------------")
# print(employee_file.readline())
# print(employee_file.readline())
# print("-------------------------")
# print(employee_file.readlines())
# print("-------------------------")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

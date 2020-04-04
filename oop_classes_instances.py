class Employee:
    # pass means the class is empty and to be skipped
    pass


# emp1 is the instance of the class
emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

# manually setting the variable of the instance
emp1.first = "Pankaj"
emp1.last = "Barnwal"
emp1.email = "suno.pankaj@gmail.com"
emp1.pay = 60000

emp2.first = "Kumari"
emp2.last = "Payal"
emp2.email = "nitjsr.payal@gmail.com"
emp2.pay = 50000

print(emp1.email)
print(emp2.email)

"""
Now instead of manually providing the variables in the instance
one can define the variables in the class itself through __init__
method.
"""

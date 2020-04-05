"""
class variables are variables that are shared among all instances
of the class while instance variables are unique for each instances
like name or pay
"""


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # this method is for intialization as constructor in other lang
    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@indianoil.com'
        # this will increase the no of empls at every intialization
        # it is also prduent to increase it in class istead of self
        # as in self.num_of_emps
        Employee.num_of_emps += 1


    def fullname(self):
        # '{} {}' is the placeholder
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # class variables can be accessed through instance
        self.pay = int(self.pay * self.raise_amount)


# emp1 is the instance of the class
emp1 = Employee('Pankaj', 'Barnwal', 60000)
emp2 = Employee('Kumari', 'Payal', 50000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# any instance will first check whether attribute is in the
# instance. if it doesn't then it will also check the class it
# is in or inherited from for the variables
print("\nclass variable accessed from instance: "+ str(emp1.raise_amount))
print("class variable accessed from class: " + str(Employee.raise_amount))

# printing namespace of employee 1
print(emp1.__dict__)

# printing namespace of Employee class
print("\n")
print(Employee.__dict__)

print("\n------------------\n")
# it changes the raise amount on whole class
# Employee.raise_amount = 1.05

# this creates a new variable in emp1
emp1.raise_amount = 1.05
print(emp1.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.num_of_emps)
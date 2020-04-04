class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # repr is an unambiguous representation of an object and used
    # for debugging
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.email)

    # str is made for readable representation of an object
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


emp_1 = Employee('Pankaj', 'Barnwal', 60000)
emp_2 = Employee('Kumari', 'Payal', 60000)

# this will first check str function and then look for repr
print(emp_1)

print("\n----------Dunder Functions----------\n")

print(1+2)
print('a' + 'b')

# in the background this is being achieved through dunder methods like this
print(int.__add__(1,2))
print(str.__add__('a', 'b'))

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@indianoil.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# inherit from Employee class
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # parent class will handle initialization of these variables
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    # default value of mutable datatype such as list or dictionary
    # should never be passed while initialization
    def __init__(self, first, last, pay, employees = None):
        # parent class will handle initialization of these variables
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# provides details about Developer class
# print(help(Developer))

dev_1 = Developer('Pankaj', 'Barnwal', 50000, 'Python')
dev_2 = Developer('Kumari', 'Payal', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print(mgr_1.email)
mgr_1.print_emp()

# check if object is an instance of the mentioned class
print(isinstance(mgr_1, Developer))

# check if a class is a subclass of the mentioned class
print(issubclass(Developer, Employee))

print("\n--------Developer----------\n")

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)


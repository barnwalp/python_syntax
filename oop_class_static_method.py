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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    # as per convention this method start with from
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Pankaj', 'Barnwal', 60000)
emp_2 = Employee('Kumari', 'Payal', 60000)

# way to change the class variable
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# using classmethod as alternative constructor
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-40000"
emp_str_3 = "Jane-Doe-50000"

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)

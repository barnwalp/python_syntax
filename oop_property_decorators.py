class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # we are defining email as a method but we can access this as
    # an attribute using @ property
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # creating a setter method for the fullname
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # creating a setter method for the fullname
    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

emp_1.fullname = 'Pankaj Barnwal'

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


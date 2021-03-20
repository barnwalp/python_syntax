# list is iterable but not an iterator
# iterable is something that can be looped over, such as list, tuple, string
# generator, files, dictionaries etc

# An Iterator is an object with a state so that it remembers where it is
# while iteration. calling an iter() method on a iterable returns an iterator

# while an iterable only has an __iter__() method, iterator has both __iter__()
# and __next__() method

my_tuple = ('apple', 'banana', 'cherry')
my_iter = iter(my_tuple)

# my_iter is and iterator of my_tuple, which is an iterable.
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print('-----------')


class PrintNumber:
    def __init__(self, max):
        self.max = max

    # if the user-defined object does not implement iter, next or getitem,
    # then TypeError exception is raised
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num


print_num = PrintNumber(5)
print_num_iter = iter(print_num)
print(next(print_num_iter))

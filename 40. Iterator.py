'''
Iterator is an object that contains a countable number of values, meaning that
you can traverse through all the value. In python, iterator is an object which
implements the iterator protocol, which consists of the methods __iter__()
and __next__()

Lists, tuples, dictionary, strings and sets are all iterable object. All these objects
have a iter() method, which is used to get an iterator.

iter() method is used to convert an iterable to iterator. iter() uses next()
for accessing value. it takes two parameter; first is the iterable and the
2nd is the sentinel which is a special value that is used to represent the
end of a sequence.

without sentinel, first object must support iteration protocol. it setinel
is provided, then object must be a callable object. The iterator created in
this case will call object with no arguments for each call to its __next__()
method; if the value returned is equal to sentinel, StopIteration will be raised

iteration object remembers iteration count via internal count variable.
once iteration is complete, it raises a Stopiteration exception so it can
be used to traverse the container just once.
'''

my_tuple = ('apple', 'banana', 'cherry')
my_iter = iter(my_tuple)
# my_iter is and iterator of my_tuple, which is an iterable.
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print('-----------')

for data in my_tuple:
    print(data)


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

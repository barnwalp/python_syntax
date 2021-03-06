"""
for an object to be iterable, it must have an __iter__() method. for example
list is an iterable but not an iterator, but if we run an __iter__method on
the list, it will return an iterator.
"""
nums = [1, 2, 3]

i_nums = nums.__iter__()    # iter(num) is same

dir(nums)       # will not have __next__()
dir(i_nums)     # will have __next__()

# print(next(i_nums))
# print(next(i_nums))     # it remembers the state
# print(next(i_nums))
# print(next(i_nums))     # will raise error as there are only 3 value

# for loop basically gets an iterator of original object like we did on line 8
# and then it's getting the next value until it hits a stop iteration exception
# Iterator is an object with a state so that it remembers where it is during
# iteration. Basically it is doing something like this
# iterators can only go forward
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
print('-----------------')


class MyRange:
    def __init__(self, my_list=None):
        # self.value = start
        # self.end = end
        if my_list is None:
            self.my_list = []
        else:
            self.my_list = my_list
        self.end = len(self.my_list)
        self.value = 0

    # iter method has to return an iterator, an object which has a next method
    def __iter__(self):
        return self

    # as iter has returned self, which needs to be an iterator. now its
    # imperative to ensure that self has next method as well
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.my_list[self.value]
        self.value += 1
        # print(current)
        return current


my_list = [8, 6, 7, 9, 2, 3]
nums = MyRange(my_list)
for num in nums:
    print(f'value of my_list is: {num}')

print('-------------------')


class Tailer:
    def __init__(self, cloth_type, style, measurements=None):
        self.cloth_type = cloth_type
        self.style = style
        if measurements is None:
            self.measurements = []
        self.measurements = measurements

    def create_dress(self):
        pass

    def stich(self):
        pass

    # def __iter__(self):
    #     return self
    #

    # def __next__(self):
    #     if self.measurements


if __name__ == "__main__":
    my_shirt = Tailer("shirt", "hip", [56, 50, 21, 10, 12])

    for vars, value in my_shirt.__dict__.items():
        print(f'{vars} --> {value}')

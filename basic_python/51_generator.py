# generator are  iterator where next() and iter() method are create_dress
# automatically

# generator can also be termed as a iterable which you can only iterate over
# once; generator does not store value in memory, they generate the values on
# the fly.


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# When you call a function that contains yield statement anywhere, you get a
# generator object, but no code runs. Then each time you extract an object
# from the generator, python executes code in the function untill it comes to
# yield statement, then it pauses & deliver the object.when you extract another
# object, python resumes just after the yield and continues until it reaches
# another yield. this continues until the function runs off the end.


nums = my_range(1, 10)

# calling the generator
print(nums)

# extracting value from generator
print(next(nums))

# another way to make a generator
mygenerator = (x*x for x in range(50))

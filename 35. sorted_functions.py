from student import Student
from operator import itemgetter, attrgetter

# sorting a dictionary
dict = {
    2: 'B',
    1: 'D',
    3: 'B',
    4: 'E',
    5: 'A'
}
print("\nprinting sorted dictionary is: " + str(sorted(dict)))

# sorting words in a sentence
sentence = "this is a test string from pankaj"
print("\nwords of the sentence in the sorted order: " + str(sorted(sentence.split(), key=str.lower)))

# sorting a tuple
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print("\ntuple sorted based on 2nd index: " + str(sorted(student_tuples, key=lambda student: student[2])))
print("\ntuple sorted based on 0th index: " + str(sorted(student_tuples, key=itemgetter(0))))


# sorting a tuple based on second element
def take_second(element):
    return element[1]


random = [
    (2, 2),
    (3, 5),
    (4, 1),
    (1, 3)
]
print("\nsorted list: " + str(sorted(random, key=take_second)))

# sorting an object
student_objects = [
    Student("john", "Physics", 3, True),
    Student('jane', 'Chemistry', 3.5, False),
    Student('dave', 'Math', 2.9, False)
]

# sorted(student_objects, key=lambda b: b.gpa)
# print("\n")
# for student in student_objects:
#     print("GPA of " + str(student.person) + " is: " + str(student.gpa))
# print("\n")
# sorted(student_objects, key=attrgetter('gpa'))
# for student in student_objects:
#     print("GPA of " + str(student.person) + " is: " + str(student.gpa))
print("-----------------------------------")
student_objects.sort(key=lambda a: a.gpa)
# on large list you will get better performance using attrgetter
# as your key. this is just an optimised (lower lever) form of
# lambda function
student_objects.sort(key=attrgetter('gpa'), reverse=True)


for student in student_objects:
    print("GPA of " + str(student.person) + " is: " + str(student.gpa))

from student import Student

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

# to check if Student class is working
student1 = Student("john", "Physics", 3, True)
print(student1.person)

# sorting an object
student_objects = [
    student1,
    Student('jane', 'Chemistry', 3.5, False),
    Student('dave', 'Math', 2.9, False)
]
print("\n" + str(student1.major))
print(sorted(student_objects, key=lambda student: student.gpa))
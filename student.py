class Student:
    def __init__(self, name, major, gpa):
        self.person = name
        self.major = major
        self.gpa = gpa
        # self.is_on_probabtion = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

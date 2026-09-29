class Student:
    def __init__(self,student_id,name,dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0
class Course:
    def __init__(self,course_id,name,credits):
        self.id = course_id
        self.name = name
        self.credits = credits


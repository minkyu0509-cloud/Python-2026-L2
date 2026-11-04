class Student:
    def __init__(self,id,name,dob):
        self.id = id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"[{self.id}] {self.name} - DoB: {self.dob}"

class Course:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"[{self.id}] {self.name}"
class Mark:
    def __init__(self,student_id,course_id,mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark
    def __str__(self):
        return f"Student: [{self.student_id}] - Course: [{self.course_id}] - Mark: {self.mark}"


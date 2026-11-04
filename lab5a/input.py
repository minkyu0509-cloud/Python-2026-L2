import pandas as pd
from domain import Student, Course, Mark


def input_students():
    students = []
    num = int(input("enter number of students: "))
    for _ in range(num):
        id = input("enter student id: ")
        name = input("enter student name: ")
        dob = input("enter student date of birth: ")
        student = Student(id, name, dob)
        students.append(student)
    return students
def input_courses():
    courses = []
    num = int(input("enter number of courses: "))
    for _ in range(num):
        id = input("enter course id: ")
        name = input("enter course name: ")
        course = Course(id, name)
        courses.append(course)
    return courses
def input_marks(students, courses):
    marks = []
    print("\n -- enter point --")
    course_id = input("enter course id: ")
    course_exists = any(course.id == course_id for course in courses)
    if not course_exists:   
        print("course id not found")
        return marks
    for student in students:
        mark_value = float(input(f"enter mark for student {student.name} (id: {student.id}): "))
        marks.append(Mark(student.id, course_id, mark_value))
        return marks

def load_dataframes():
    try:
        df_students = pd.read_csv('students.csv')
        df_courses = pd.read_csv('courses.csv')
        df_marks = pd.read_csv('marks.csv')
        return df_students, df_courses, df_marks
    except FileNotFoundError:
        print("One or more CSV files not found.")
        return None, None, None
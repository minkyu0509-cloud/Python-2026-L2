import math
import numpy as np
import curses
#--students class--
class Student:
    def __init__(self,student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0
#--course class
class Course:
    def __init__(self, course_id, name,credits):
        self.id = course_id
        self.name = name
        self.credits = credits

#--system management--
class SchoolSystem:
    def __init__(self,stdscr):
        self.students = []
        self.courses = []
        self.stdscr = stdscr
    def input_student(self):
        num = int(input("Enter the number of students: "))
        for _ in range(num):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (YYYY-MM-DD): ")
            student = Student(student_id, name, dob)
            self.students.append(student)
    def input_course(self):
        num = int(input("Enter the number of courses: "))
        for _ in range(num):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            course = Course(course_id, name, credits)
            self.courses.append(course)
    def input_marks(self):
        if not self.students or not self.courses:
            print("Please input students and courses first.")
            return
        course_id = input("Enter course ID to input marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            print("Course not found.")
            return
        print(f"Inputting marks for course: {course.name}")
        for student in self.students:
            raw_mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
            rounded_mark = math.floor(raw_mark * 10) / 10  
            student.marks[course_id] = rounded_mark
            print(f" _>save mark:{rounded_mark}")
    def calculate_gpa(self):
        for student in self.students:
            if not student.marks:
                continue
            marks_array =[]
            credits_array = []
            for course_id,mark in student.marks.items():
                course = next((c for c in self.courses if c.id == course_id), None)
                if course:
                    marks_array.append(mark)
                    credits_array.append(course.credits)
            if credits array:   
                np_marks =  np.array(marks_array)
                np_credits = np.array(credits_array)
                raw_gpa = np.average(np_marks, weights=np_credits)
                student.gpa = math.floor(raw_gpa * 10) / 10
        print("GPA calculation completed.")
    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)
        print("Students sorted by GPA (highest to lowest):")
    def get_input(self, prompt, y, x=0):
        self.stdscr.addstr(y, x, prompt)
        self.stdscr.refresh()
        curses.echo()
        input_str = self.stdscr.getstr(y, x + len(prompt)).decode('utf-8')
        curses.noecho()
        return input_str
def display_results(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== DANH SÁCH SINH VIÊN & GPA ===", curses.A_BOLD)
        
        self.stdscr.addstr(2, 0, f"{'Mã SV':<10} | {'Họ và tên':<20} | {'GPA':<5}")
        self.stdscr.addstr(3, 0, "-" * 42)

        for i, s in enumerate(self.students):
            self.stdscr.addstr(4 + i, 0, f"{s.id:<10} | {s.name:<20} | {s.gpa:<5.1f}")

        self.stdscr.addstr(6 + len(self.students), 0, "Ấn phím bất kỳ để thoát...")
        self.stdscr.getch()

#--main --
def main(stdscr):
    system = SchoolSystem(stdscr)
    system.input_student()
    system.input_course()
    system.input_marks()
    system.calculate_gpa()
    system.sort_students_by_gpa()
    system.display_results()

if __name__ == "__main__":
    curses.wrapper(main)



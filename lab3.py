import math
import numpy as np
import curses

# -- TẠO KHUÔN MẪU SINH VIÊN --
class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

# -- TẠO KHUÔN MẪU MÔN HỌC --
class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

# -- HỆ THỐNG QUẢN LÝ (GIAO DIỆN CURSES) --
class SchoolSystem:
    def __init__(self, stdscr):
        self.students = []
        self.courses = []
        self.stdscr = stdscr

    def get_input(self, prompt, y, x=0):
        """Hàm công cụ giúp lấy dữ liệu nhập vào từ màn hình Curses"""
        self.stdscr.addstr(y, x, prompt)
        self.stdscr.refresh()
        curses.echo()
        input_str = self.stdscr.getstr(y, x + len(prompt)).decode('utf-8')
        curses.noecho()
        return input_str

    def input_student(self):
        self.stdscr.clear()
        num_str = self.get_input("Enter the number of students: ", 0)
        try:
            num = int(num_str)
        except ValueError:
            return

        for i in range(num):
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"--- Nhap thong tin Sinh vien {i+1} ---", curses.A_BOLD)
            student_id = self.get_input("Enter student ID: ", 1)
            name = self.get_input("Enter student name: ", 2)
            dob = self.get_input("Enter student date of birth (YYYY-MM-DD): ", 3)
            self.students.append(Student(student_id, name, dob))

    def input_course(self):
        self.stdscr.clear()
        num_str = self.get_input("Enter the number of courses: ", 0)
        try:
            num = int(num_str)
        except ValueError:
            return

        for i in range(num):
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"--- Nhap thong tin Mon hoc {i+1} ---", curses.A_BOLD)
            course_id = self.get_input("Enter course ID: ", 1)
            name = self.get_input("Enter course name: ", 2)
            credits_str = self.get_input("Enter course credits: ", 3)
            
            # Gán giá trị mặc định nếu người dùng nhập sai số tín chỉ
            credits = int(credits_str) if credits_str.isdigit() else 1 
            self.courses.append(Course(course_id, name, credits))

    def input_marks(self):
        self.stdscr.clear()
        if not self.students or not self.courses:
            self.stdscr.addstr(0, 0, "Please input students and courses first. Press any key...")
            self.stdscr.getch()
            return

        course_id = self.get_input("Enter course ID to input marks: ", 0)
        course = next((c for c in self.courses if c.id == course_id), None)
        
        if not course:
            self.stdscr.addstr(2, 0, "Course not found. Press any key...")
            self.stdscr.getch()
            return

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, f"Inputting marks for course: {course.name}", curses.A_BOLD)
        
        for i, student in enumerate(self.students):
            # In dòng nhắc nhập điểm và dịch dần tọa độ y xuống dưới (i + 2)
            raw_mark_str = self.get_input(f"Enter mark for {student.name} (ID: {student.id}): ", i + 2)
            try:
                raw_mark = float(raw_mark_str)
                # Làm tròn xuống 1 chữ số thập phân
                rounded_mark = math.floor(raw_mark * 10) / 10.0  
                student.marks[course_id] = rounded_mark
            except ValueError:
                self.stdscr.addstr(i + 2, 50, "-> Lỗi! Đã bỏ qua.")
        
        self.stdscr.addstr(len(self.students) + 4, 0, "Saved marks! Press any key...")
        self.stdscr.getch()

    def calculate_gpa(self):
        for student in self.students:
            if not student.marks:
                continue
            
            marks_array = []
            credits_array = []
            
            for course_id, mark in student.marks.items():
                course = next((c for c in self.courses if c.id == course_id), None)
                if course:
                    marks_array.append(mark)
                    credits_array.append(course.credits)
                    
            # Đã sửa lỗi thiếu dấu gạch dưới ở dòng này
            if credits_array:  
                np_marks = np.array(marks_array)
                np_credits = np.array(credits_array)
                raw_gpa = np.average(np_marks, weights=np_credits)
                student.gpa = math.floor(raw_gpa * 10) / 10.0

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)

    # Đã sửa lỗi thụt lề: Đưa hàm này vào bên trong lớp SchoolSystem
    def display_results(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== DANH SÁCH SINH VIÊN & GPA ===", curses.A_BOLD)
        
        self.stdscr.addstr(2, 0, f"{'Mã SV':<10} | {'Họ và tên':<20} | {'GPA':<5}")
        self.stdscr.addstr(3, 0, "-" * 42)

        for i, s in enumerate(self.students):
            self.stdscr.addstr(4 + i, 0, f"{s.id:<10} | {s.name:<20} | {s.gpa:<5.1f}")

        self.stdscr.addstr(6 + len(self.students), 0, "Ấn phím bất kỳ để thoát...")
        self.stdscr.getch()

# -- LUỒNG CHẠY CHÍNH --
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
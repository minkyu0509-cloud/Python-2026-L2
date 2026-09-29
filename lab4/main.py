import curses
import math
import numpy as np
import input
import output

def calculate_gpa(students_list, courses_list):
    """Sử dụng Numpy để tính GPA có trọng số cho danh sách sinh viên"""
    for student in students_list:
        if not student.marks:
            continue
        
        marks_array = []
        credits_array = []
        
        for course_id, mark in student.marks.items():
            course = next((c for c in courses_list if c.id == course_id), None)
            if course:
                marks_array.append(mark)
                credits_array.append(course.credits)
                
        if credits_array:
            np_marks = np.array(marks_array)
            np_credits = np.array(credits_array)
            raw_gpa = np.average(np_marks, weights=np_credits)
            student.gpa = math.floor(raw_gpa * 10) / 10.0

def sort_students(students_list):
    """Sắp xếp sinh viên theo GPA giảm dần"""
    students_list.sort(key=lambda s: s.gpa, reverse=True)

def main(stdscr):
    # 1. Khởi tạo kho dữ liệu trống
    students = []
    courses = []

    # 2. Điều phối mô-đun nhập liệu
    input.input_student_data(stdscr, students)
    input.input_course_data(stdscr, courses)
    input.input_marks_data(stdscr, students, courses)

    # 3. Tính toán toán học và sắp xếp
    calculate_gpa(students, courses)
    sort_students(students)

    # 4. Điều phối mô-đun hiển thị đầu ra
    output.display_results(stdscr, students)

if __name__ == "__main__":
    curses.wrapper(main)
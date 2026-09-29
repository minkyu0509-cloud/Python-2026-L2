import math
import curses
from domains.domain import Student, Course

def get_input(stdscr, prompt, y, x=0):
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()
    curses.echo()
    input_str = stdscr.getstr(y, x + len(prompt)).decode('utf-8')
    curses.noecho()
    return input_str

def input_student_data(stdscr, students_list):
    stdscr.clear()
    num_str = get_input(stdscr, "Enter the number of students: ", 0)
    try:
        num = int(num_str)
    except ValueError:
        return

    for i in range(num):
        stdscr.clear()
        stdscr.addstr(0, 0, f"--- Nhap thong tin Sinh vien {i+1} ---", curses.A_BOLD)
        student_id = get_input(stdscr, "Enter student ID: ", 1)
        name = get_input(stdscr, "Enter student name: ", 2)
        dob = get_input(stdscr, "Enter student date of birth (YYYY-MM-DD): ", 3)
        students_list.append(Student(student_id, name, dob))

def input_course_data(stdscr, courses_list):
    stdscr.clear()
    num_str = get_input(stdscr, "Enter the number of courses: ", 0)
    try:
        num = int(num_str)
    except ValueError:
        return

    for i in range(num):
        stdscr.clear()
        stdscr.addstr(0, 0, f"--- Nhap thong tin Mon hoc {i+1} ---", curses.A_BOLD)
        course_id = get_input(stdscr, "Enter course ID: ", 1)
        name = get_input(stdscr, "Enter course name: ", 2)
        credits_str = get_input(stdscr, "Enter course credits: ", 3)
        credits = int(credits_str) if credits_str.isdigit() else 1 
        courses_list.append(Course(course_id, name, credits))

def input_marks_data(stdscr, students_list, courses_list):
    stdscr.clear()
    if not students_list or not courses_list:
        stdscr.addstr(0, 0, "Please input students and courses first. Press any key...")
        stdscr.getch()
        return

    course_id = get_input(stdscr, "Enter course ID to input marks: ", 0)
    course = next((c for c in courses_list if c.id == course_id), None)
    
    if not course:
        stdscr.addstr(2, 0, "Course not found. Press any key...")
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(0, 0, f"Inputting marks for course: {course.name}", curses.A_BOLD)
    
    for i, student in enumerate(students_list):
        raw_mark_str = get_input(stdscr, f"Enter mark for {student.name} (ID: {student.id}): ", i + 2)
        try:
            raw_mark = float(raw_mark_str)
            rounded_mark = math.floor(raw_mark * 10) / 10.0  
            student.marks[course_id] = rounded_mark
        except ValueError:
            stdscr.addstr(i + 2, 50, "-> Lỗi! Đã bỏ qua.")
    
    stdscr.addstr(len(students_list) + 4, 0, "Saved marks! Press any key...")
    stdscr.getch()
students = []
courses =[]
marks = {}

def input_number_of_students():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                print("Please enter a positive integer.")
                continue
            return num_students
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def input_student_info():
    num_students = input_number_of_students()
    for i in range(num_students):
        print(f"\nEntering information for student {i + 1}:")
        s_id = input("Enter student ID: ")
        s_name = input("Enter student name: ")
        s_dob = input("Enter student date of birth (YYYY-MM-DD): ")

        student = {
            "id": s_id,
            "name": s_name,
            "dob": s_dob
        }
        students.append(student)

def input_number_of_courses():
    while True:
        try:
            num_courses = int(input("Enter the number of courses: "))
            if num_courses <= 0:
                print("Please enter a positive integer.")
                continue
            return num_courses
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def input_course_info():
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        print(f"\nEntering information for course {i + 1}:")
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")

        course = {
            "id": c_id,
            "name": c_name
        }
        courses.append(course)

if __name__ == "__main__":
   
    input_student_info()
    input_course_info()
    
    
    print("\n[Dữ liệu Sinh viên]:", students)
    print("\n[Dữ liệu Môn học]:", courses)

def input_marks():
    if not students or not courses:
        print("Please enter student and course information first.")
        return

    for course in courses:
        print(f"\nEntering marks for course: {course['name']} (ID: {course['id']})")
        for student in students:
            while True:
                try:
                    mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
                    if mark < 0 or mark > 100:
                        print("Please enter a mark between 0 and 100.")
                        continue
                    marks[(student['id'], course['id'])] = mark
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

def input_marks_for_course():
    if not students or not courses:
        print("Please enter student and course information first.")
        return

    print("\n--- SELECT A COURSE TO INPUT MARKS ---")
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")
    
    selected_course_id = input("Enter Course ID to input marks: ")

    course_exists = any(c['id'] == selected_course_id for c in courses)
    if not course_exists:
        print(f"Error: Course ID '{selected_course_id}' not found.")
        return

    print(f"\n--- INPUT MARKS FOR COURSE: {selected_course_id} ---")
    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
                if mark < 0 or mark > 20: 
                    print("Please enter a valid mark (0 to 20).")
                    continue
                marks[(student['id'], selected_course_id)] = mark
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def list_courses():
    if not courses:
        print("No courses available.")
        return
    print("\n--- LIST OF COURSES ---")
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")

def list_students():
    if not students:
        print("No students available.")
        return
    print("\n--- LIST OF STUDENTS ---")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | DOB: {student['dob']}")

def show_marks_for_given_course():
    if not marks:
        print("No marks available.")
        return

    selected_course_id = input("Enter Course ID to show marks: ")

    course_name = next((c['name'] for c in courses if c['id'] == selected_course_id), None)
    if not course_name:
        print(f"Error: Course ID '{selected_course_id}' not found.")
        return

    print(f"\n--- STUDENT MARKS FOR COURSE: {course_name} ---")
    
    found_marks = False
    for (s_id, c_id), mark in marks.items():
        if c_id == selected_course_id:
            student_name = next((s['name'] for s in students if s['id'] == s_id), "Unknown")
            print(f"Student: {student_name} (ID: {s_id}) | Mark: {mark}")
            found_marks = True
            
    if not found_marks:
        print("No marks entered for this course yet.")

def main():
    while True:
        print("\n" + "="*30)
        print("STUDENT MARK MANAGEMENT SYSTEM")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("0. Exit")
        print("="*30)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_student_info()
        elif choice == '2':
            input_course_info()
        elif choice == '3':
            input_marks_for_course()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_marks_for_given_course()
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
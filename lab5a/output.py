import pandas as pd
def export_to_csv(students_list, courses_list, marks_list):
    students_data = [{'id': student.id, 'name': student.name, 'dob': student.dob} for student in students_list]
    courses_data = [{'id': course.id, 'name': course.name} for course in courses_list]
    marks_data = [{'student_id': mark.student_id, 'course_id': mark.course_id, 'mark': mark.mark} for mark in marks_list]

    df_students = pd.DataFrame(students_data)
    df_courses = pd.DataFrame(courses_data)
    df_marks = pd.DataFrame(marks_data)

    df_students.to_csv('students.csv', index=False)
    df_courses.to_csv('courses.csv', index=False)
    df_marks.to_csv('marks.csv', index=False)

    print("Data exported to CSV files successfully.")
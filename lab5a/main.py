from input import input_students, input_courses, input_marks, load_dataframes
from output import export_to_csv
import pandas as pd

def query_students(df_students):
    print("\n -- query students --")
    print("\n hint: name = 'Mr. Volunteer' or id = 'S001'")
    condition = input("enter query condition: ")
    if '=' in condition and '==' not in condition :
        condition = condition.replace('=', '==')
    try:
        result = df_students.query(condition)
        if result.empty:
            print("No students found matching the condition.")
        else:
            print(result)
    except Exception as e:
        print(f"Error in query: {e}")
def main():
    print(" == Student Management System ==")

    students = input_students()
    courses = input_courses()
    marks = input_marks(students, courses)
    export_to_csv(students, courses, marks)
    df_students, df_courses, df_marks = load_dataframes()

    if df_students is not None:
        query_students(df_students)

if __name__ == "__main__":
    main()

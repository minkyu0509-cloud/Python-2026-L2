import threading
import pickle
import gzip
import time
import os

class Person:
    def __init__(self):
        self.__id = ""
        self.__name = ""
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def input(self):
        self.__id = input("Enter ID: ")
        self.__name = input("Enter Name: ")
class Student(Person):
    def __init__(self):
        super().__init__()
        self.__dob = ""
    def input(self):
        print("--student information--")
        super().input()
        self.__dob = input("Enter Date of Birth: ")
    def list(self):
        print(f"Student [ID:{self.get_id()}, Name: {self.get_name()}, Date of Birth: {self.__dob}]")

class Course:
    def __init__(self):
        self.__id =""
        self.__name = ""
    def input(self):
        print("--course information--")
        self.__id = input("Enter ID: ")
        self.__name = input("Enter Name: ")
    def list(self):
        print(f"Course [ID:{self.__id}, Name: {self.__name}]")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name

class Mark:
    def __init__(self,student,course):
        self.__student = student
        self.__course = course
        self.__score = 0.0
    def input(self):
        self.__score = float(input(f"Enter score for student {self.__student.get_name()} in course {self.__course.get_name()}: "))
    def list(self):
        print(f"Mark [Student: {self.__student.get_name()}, Course: {self.__course.get_name()}, Score: {self.__score}]")

class Management:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = []
        self.__load_data()
    
    def __load_data(self):
        if os.path.exists("data.pkl.gz"):
            try:
                with gzip.open("data.pkl.gz", "rb") as f:
                    data = pickle.load(f)
                self.__students = data.get('students',[])
                self.__courses = data.get('courses',[])
                self.__marks = data.get('marks',[])
                print("data loaded from data.pkl.gz")
                
            except Exception as e:
                print(f"Failed to load data: {e}")

            

    def __background_save(self,data):
        print("\n [thread]")
        time.sleep(2)
        with gzip.open("data.pkl.gz","wb") as f:
            pickle.dump(data, f)
        print("\n[thread] save!")


    def trigger_save_thread(self):
        data = {
            'students' : self.__students,
            'courses' : self.__courses,
            'marks' : self.__marks
        }
        save_thread = threading.Thread(target=self.__background_save, args=(data,))
        save_thread.start()
    

    
    def add_student(self):
            num = int(input("Enter number of students: "))
            for _ in range(num):
                s = Student()
                s.input()
                self.__students.append(s)
            self.trigger_save_thread()
    def add_course(self):
            num = int(input("Enter number of courses: "))
            for _ in range(num):
                c = Course()
                c.input()
                self.__courses.append(c)
            self.trigger_save_threaf()
    def add_mark(self):
            course_id = input("Enter course ID to add marks: ")
            target_course = None
            for c in self.__courses:
                if c.get_id() == course_id:
                    target_course = c
                    break
            if not target_course:
                print("Course not found.")
                return
            for s in self.__students:
                m = Mark(s, target_course)
                m.input()
                self.__marks.append(m)
            self.trigger_save_thread()
    def show_all(self):
        print("== Students ==")
        for s in self.__students:
            s.list()
        print("== Courses ==")
        for c in self.__courses:
            c.list()
        print("== Marks ==")
        for m in self.__marks:
            m.list()
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Add Mark")
            print("4. Show All")
            print("5. Exit")
            choice = input("\nEnter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_course()
            elif choice == '3':
                self.add_mark()
            elif choice == '4':
                self.show_all()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = Management()
    system.menu()
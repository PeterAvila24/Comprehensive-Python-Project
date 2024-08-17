import json
import logging 
from data_structures import Student, Course, LinkedList, BinarySearchTree
from exceptions import CourseNotFoundError, StudentNotFoundError, InvalidGradeError
from database import insert_course, insert_student, get_courses, get_students_in_course

logging.basicConfig(
    filename='student_management_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def add_course(courses):
    course_id = input("Enter Course ID: ")
    course_name = input("Enter course Name: ")

    if course_id in courses:
        print("Course ID already exists!")
        logging.warning(f"Attempt to add a duplicate xourse: {course_id}")
    else:
        insert_course(course_id, course_name)
        courses[course_id] = Course(course_id, course_name)
        logging.info(f"Course '{course_name}' added with ID {course_id}")
        print(f"Course '{course_name}' added succesfully!")

def add_student_to_course(courses, transaction_history):
    course_id = input("Enter Course ID: ")

    try:

        if course_id not in courses:
            raise CourseNotFoundError("Course ID not found")
        

        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")

        course = courses[course_id]

        if course.get_student(student_id) is not None:
            print("Student ID already exist in thsi course!")
            logging.warning(f"Attempt to add a duplicate student: {student_id} top course {course_id}")
        else:
            student = Student(student_id, student_name)
            course.add_student(student)
            insert_student(student_id, student_name, course_id)
            transaction_history.append(f"Added student {student_name} (ID: {student_id} to course {course.course_name})")
            logging.info(f"Student {student_name} (ID: {student_id}) added to course '{course.course_name}'")
            print(f"Student '{student_name}' added to course '{course.course_name}' succesfully!")
    
    except CourseNotFoundError as e:
        logging.error(e)
        print(e)
    


def view_courses(courses):

    if not courses:
        print("No courses available.")
    else:
        for course_id, course in courses.items():
            print(f"{course}")

def view_students_in_course(courses):
    course_id = input("Enter Course ID: ")

    if course_id not in courses:
        raise CourseNotFoundError("Course ID was not found")
    else:
        course = courses[course_id]
        students = course.list_students()

        if not students:
            print(f"No students enrolled in  {course.course_name}.")
        else:
            for student in students:
                print(f"{student}")

def assign_grade_to_student(courses, transaction_history):
    course_id = input("Enter the course ID: ")

    if course_id not in courses:
        raise CourseNotFoundError("Course ID not found.")
        
    

    student_id = input("Enter Student ID: ")
    course = courses[course_id]
    student = course.get_student(student_id)

    if student is None:
        raise StudentNotFoundError("Student ID not found in this course!")
    else:
        try:
            grade = float(input("Enter grade: "))
            student.add_grades(grade)
            transaction_history.append(f"Assigned grade {grade} to {student.name} (ID: {student_id}) in course {course.course_name}")
            print(f"Grade {grade} assigned to {student.name}.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    

def view_student_average_grade(courses):
    course_id = input("Enter Course ID: ")

    if course_id not in courses:
        raise CourseNotFoundError("Course ID was not found")
    
    student_id = input("Enter Student ID: ")
    course = courses[course_id]
    student = course.get_student(student_id)

    if student is None:
        raise StudentNotFoundError("Student ID not found in this Course.")
    else:
        print(f"{student.name}'s average garde: {student.get_average_grade():.2f}")

def view_transaction_history(transaction_history):
    print("Transaction History: ")
    transaction_history.display()


def remove_student_from_course(courses, transacation_history):
    course_id = input("Enter Course ID: ")

    if course_id not in courses:
        raise CourseNotFoundError("Course ID was not found")
        return
    
    student_id = input("Enter Student ID: ")

    course = courses[course_id]
    student = course.get_student(student_id)

    if student is None:
        raise StudentNotFoundError("Student ID not found in this Course.")
    else:
        course.remove_student(student_id)
        transacation_history.append(f"Removed Student {student.name} (ID: {student_id} from course {course.course_name})")
        print(f"Student '{student.name}' removed from course '{course.course_name}' successfully!")

def search_student_in_all_courses(courses):
    student_id = input("Enter Student ID to search: ")


    found = False

    for course_id, course in courses.items():
        student = course.get_student(student_id)

        if student:
            print(f"Student found in course '{course.course_name}' (Course ID: {course_id}): {student}")
            found = True
            break
    
    if not found:
        print("Student ID not found in any courses.")

def delete_course(courses, transaction_history):
    course_id = input("Enter Course ID to delete: ")

    if course_id in courses:
        deleted_course = courses.pop(course_id)
        transaction_history.append(f"Deleted course {deleted_course.course_name} (ID: {course_id})")
        print(f"Course '{deleted_course.course_name}' deleted successfully!")
    else:
        raise CourseNotFoundError("Course ID not found!")

def update_student_info(courses, transaction_history):
    course_id = input("Enter Course ID: ")

    if course_id not in courses:
        raise CourseNotFoundError("Course ID not found!")
        return
    
    student_id = input("Enter Student ID: ")
    course = courses[course_id]
    student = course.get_student(student_id)

    if student is None:
        raise StudentNotFoundError("Student ID not found in this course!")
    else:
        new_name = input(f"Enter new name for {student.name}")
        old_name = student.name
        student.name = new_name
        transaction_history.append(f"Updated student name from {old_name} to {new_name} in course {course.course_name}") 
        print(f"Student ID '{student_id}' name updated from '{old_name}' to '{new_name}' successfully!")  

def save_data(courses, filename="data.json"):
    data = {}

    for course_id, course in courses.items():
        data[course_id] = {
            "course_name": course.course_name,
            "students": [
                {
                    "student_id": student.student_id,
                    "name": student.name,
                    "grades": student.grades
                }   for student in course.list_students()
            ]
        }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data saved to {filename} successfully")

def load_data(filename="data.json"):
    courses = {}
    
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        for course_id, course_data in data.items():
            course = Course(course_id, course_data["course_name"])
            for student_data in course_data["students"]:
                student = Student(
                    student_data["student_id"],
                    student_data["name"]
                )

                for grade in student_data["grades"]:
                    student.add_grades(grade)
                course.add_student(student)
            courses[course_id] = course
        print(f"Data Loaded from {filename} successfully!")
    except FileNotFoundError:
        print(f"No saved data found ({filename}). Starting with an empty dataset.")
    return courses

def main():
    filename = "data.json"
    courses = load_data(filename)
    courses = {}
    transaction_history = LinkedList()
    print("Welcome to the Student Management System")

    while True:
        print("\n1. Add Course")
        print("2. Add Student to Course")
        print("3. View All Courses")
        print("4. View Students in a Course")
        print("5. Assign Grade to Student")
        print("6. View Students Average grade")
        print("7. View Transaction History")
        print("8. Remove Student from course")
        print("9. Search student in all courses")
        print("10. Delete Course")
        print("11. Update Student Information")
        print("12. Save Data")
        print("13. Load Data")
        print("14. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == '1':
                add_course(courses)
            elif choice == '2':
                add_student_to_course(courses, transaction_history)
            elif choice == '3':
                view_courses(courses)
            elif choice == '4':
                view_students_in_course(courses)
            elif choice == '5':
                assign_grade_to_student(courses, transaction_history)
            elif choice == '6':
                view_student_average_grade(courses)
            elif choice == '7':
                view_transaction_history(transaction_history)
            elif choice == '8':
                remove_student_from_course(courses, transaction_history)
            elif choice == '9':
                search_student_in_all_courses(courses)
            elif choice == '10':
                delete_course(courses, transaction_history)
            elif choice == '11':
                update_student_info(courses, transaction_history)
            elif choice == '12':
                save_data(courses, filename)
            elif choice == '13':
                courses = load_data(filename)
            elif choice == '14':
                save_data(courses, filename)
                print("Exiting...")

                break
            else:
                print("Invalid choice, please try again.")

        except CourseNotFoundError as e:
            print(e)
        except StudentNotFoundError as e:
            print(e)
        except InvalidGradeError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occured: {e}")

    input("Code complete press enter to continue...")
    


if __name__ == "__main__":
    main()




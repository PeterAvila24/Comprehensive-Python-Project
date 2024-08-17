import unittest
from database import create_tables, insert_course, insert_student, get_courses, get_students_in_course

class TestDatabase(unittest.TestCase):
    def setUp(self):
        create_tables()

    def test_insert_and_get_courses(self):
        insert_course('CS101', 'Intro to Computer Science')
        courses = get_courses()
        self.assertIn(('CS101', 'Intro to Computer Science'), courses)

    def test_insert_and_get_students(self):
        insert_course('CS102', 'Data Structures')
        insert_student('S001', 'Alice', 'CS102')
        students = get_students_in_course('CS102')
        self.assertIn(('S001', 'Alice', 'CS102'), students)

if __name__ == '__main__':
    unittest.main()

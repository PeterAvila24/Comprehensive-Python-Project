# First tesing implementation
import unittest
from ComprehensivePythonProject import add_course, add_student_to_course, assign_grade_to_student, view_student_average_grade
from data_structures import Student, Course, LinkedList, BinarySearchTree
from exceptions import CourseNotFoundError, StudentNotFoundError, InvalidGradeError
from unittest.mock import patch


class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.course = Course('CS101', 'Introduction to Computer Science')
        self.student = Student('S123', 'John Doe')
        self.course.add_student(self.student)
        self.courses = {'CS101': self.course}
        self.transaction_history = LinkedList()

    @patch('builtins.input', side_effect=['CS101', 'S124', 'Jane Doe'])
    def test_add_student_to_course(self, mock_input):
        # Adding a student to a course
        add_student_to_course(self.courses, self.transaction_history)
        
        # Check if the student was added
        course = self.courses['CS101']
        student = course.get_student('S124')
        
        self.assertIsNotNone(student)  # Ensure student was added
        self.assertEqual(student.name, 'Jane Doe')  # Ensure student has the correct name

if __name__ == "__main__":
    unittest.main()

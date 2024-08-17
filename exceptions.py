class CourseNotFoundError(Exception):
    """Exception raised when a course is not found."""
    pass

class StudentNotFoundError(Exception):
    """Exception riased when a student is not found."""
    pass

class InvalidGradeError(Exception):
    """Exception raised for invalid grade inputs."""
    pass
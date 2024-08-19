from flask import Flask, render_template, request, redirect, url_for
from ComprehensivePythonProject import Student, Course

app = Flask(__name__)

# Dummy data for demonstration
students = []
courses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manage_students', methods=['GET', 'POST'])
def manage_students():
    if request.method == 'POST':
        # Handle form submissions here
        student_id = request.form.get('student_id')
        name = request.form.get('name')
        if student_id and name:
            students.append(Student(student_id, name))
        elif request.form.get('remove_id'):
            remove_id = request.form.get('remove_id')
            # Implement the remove logic
            students[:] = [student for student in students if student.student_id != remove_id]
        return redirect(url_for('manage_students'))
    
    return render_template('students.html', students=students)

@app.route('/manage_courses', methods=['GET', 'POST'])
def manage_courses():
    if request.method == 'POST':
        course_id = request.form.get('course_id')
        course_name = request.form.get('course_name')
        if course_id and course_name:
            courses.append(Course(course_id, course_name))
        elif request.form.get('remove_id'):
            remove_id = request.form.get('remove_id')
            # Implement the remove logic
            courses[:] = [course for course in courses if course.course_id != remove_id]
        return redirect(url_for('manage_courses'))
    
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)

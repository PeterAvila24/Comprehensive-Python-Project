from flask import Flask, render_template, request, redirect, url_for
from ComprehensivePythonProject import ( 
    add_student_to_course,
    get_courses,
    get_students_in_course
)

app = Flask(__name__)

@app.route('/')
def index():
    courses = get_courses()
    return render_template('index.html', courses=courses)

@app.route('/course/<course_id>')
def course(course_id):
    students = get_students_in_course(course_id)
    return render_template('course.html', students=students, course_id=course_id)

@app.route('/add_student', methods=['POST'])
def add_student():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    add_student_to_course(course_id, student_id)
    return redirect(url_for('course', course_id=course_id))

if __name__ == '__main__':
    app.run(debug=True)
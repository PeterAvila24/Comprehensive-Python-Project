# database.py

import sqlite3

def create_tables():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS courses (course_id TEXT PRIMARY KEY, course_name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS students (student_id TEXT PRIMARY KEY, student_name TEXT, course_id TEXT, FOREIGN KEY(course_id) REFERENCES courses(course_id))''')
    conn.commit()
    conn.close()

def insert_course(course_id, course_name):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('INSERT INTO courses (course_id, course_name) VALUES (?, ?)', (course_id, course_name))
    conn.commit()
    conn.close()

def insert_student(student_id, student_name, course_id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    c.execute('SELECT COUNT(*) FROM students WHERE student_id = ?', (student_id,))
    if c.fetchone()[0] > 0:
        raise Exception(f"Student with ID {student_id} already exists.")

    c.execute('INSERT INTO students (student_id, student_name, course_id) VALUES (?, ?, ?)', (student_id, student_name, course_id))
    conn.commit()
    conn.close()

def get_courses():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT * FROM courses')
    courses = c.fetchall()
    conn.close()
    return courses

def get_students_in_course(course_id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students WHERE course_id = ?', (course_id,))
    students = c.fetchall()
    conn.close()
    return students

def remove_student(student_id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()

"""from cryptography.fernet import Fernet

# Generate a key (only needs to be done once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt data
def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data):
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data
"""
class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grades(self, grade):
        #encrypted_grade = encrypt_data(str(grade))
        self.grades.append(grade)

    def get_average_grade(self):
        #if not self.encrypted_grade:
        #    return 0
        #decrypted_grades = [int(decrypt_data(grade)) for grade in self.encrypted_grades]
        return sum(self.grades) / len(self.grades) if self.grades else 0
        
    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - Avg. Grade: {self.get_average_grade()}"
    

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students_bst = BinarySearchTree()

    def add_student(self, student):
        self.students_bst.insert(student)

    def get_student(self, student_id):
        node = self.students_bst.search(student_id)
        return node.student if node else None
    
    def list_students(self):
        students_list = []
        self.students_bst.in_order_traversal(self.students_bst.root, students_list)
        return students_list
    
    def __str__(self):
        return f"Course: {self.course_name} (ID: {self.course_id})"
    
    def remove_student(self, student_id):
        self.students_bst.remove(student_id)
    

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = LinkedListNode(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class TreeNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, student):
        if self.root is None:
            self.root = TreeNode(student)
        else:
            self._insert_recursive(self.root, student)

    def _insert_recursive(self, node, student):
        if student.student_id < node.student.student_id:
            if node.left is None:
                node.left = TreeNode(student)
            else:
                self._insert_recursive(node.left, student)
        elif student.student_id > node.student.student_id:
            if node.right is None:
                node.right = TreeNode(student)
            else:
                self._insert_recursive(node.right, student)

    def search(self, student_id):
        return self._search_recursive(self.root, student_id)
    
    def _search_recursive(self, node, student_id):
        if node is None or node.student.student_id == student_id:
            return node
        elif student_id < node.student.student_id:
            return self._search_recursive(node.left, student_id)
        else:
            return self._search_recursive(node.right, student_id)  #test update 
    

    def in_order_traversal(self, node, students_list):
        if node is not None:
            self.in_order_traversal(node.left, students_list)
            students_list.append(node.student)
            self.in_order_traversal(node.right, students_list)


    def remove(self, student_id):
        self.root = self._remove_recursive(self.root, student_id)

    def _remove_recursive(self, node, student_id):
        if node is None:
            return node
        if student_id < node.student.student_id:
            node.left = self._remove_recursive(node.left, student_id)
        elif student_id > node.student.student_id:
            node.right = self._remove_recursive(node.right, student_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            

            min_larger_node = self._get_min(node.right)
            node.student = min_larger_node.student
            node.right = self._remove_recursive(node.right, min_larger_node.student.student_id)

        return node
    
    def _get_min(self, node):
        current = node 
        while current.left is not None:
            current = current.left
            
        return current
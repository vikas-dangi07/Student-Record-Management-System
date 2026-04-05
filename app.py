from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -----------------------------
# Student Linked List Node
# -----------------------------
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

# -----------------------------
# Linked List for Student Records
# -----------------------------
class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, marks):
        new_student = Student(roll_no, name, marks)
        if not self.head:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student

    def get_all_students(self):
        students = []
        current = self.head
        while current:
            students.append({
                "roll_no": current.roll_no,
                "name": current.name,
                "marks": current.marks
            })
            current = current.next
        return students

    def delete_student(self, roll_no):
        current = self.head
        prev = None
        while current:
            if current.roll_no == roll_no:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search_student(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                return {
                    "roll_no": current.roll_no,
                    "name": current.name,
                    "marks": current.marks
                }
            current = current.next
        return None

# -----------------------------
# Create Object
# -----------------------------
students = StudentList()

# -----------------------------
# Routes
# -----------------------------
@app.route('/add', methods=['POST'])
def add_student():
    data = request.json
    try:
        roll_no = int(data['roll_no'])
        marks = int(data['marks'])
        name = data['name']
    except (ValueError, KeyError):
        return jsonify({"message": "Invalid input"}), 400

    students.add_student(roll_no, name, marks)
    return jsonify({"message": "Student added successfully!"})

@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(students.get_all_students())

@app.route('/delete/<int:roll_no>', methods=['DELETE'])
def delete_student(roll_no):
    if students.delete_student(roll_no):
        return jsonify({"message": "Deleted successfully"})
    return jsonify({"message": "Student not found"}), 404

@app.route('/search/<int:roll_no>', methods=['GET'])
def search_student(roll_no):
    print("Searching for:", roll_no)  # For debugging
    result = students.search_student(roll_no)
    if result:
        return jsonify(result)
    return jsonify({"message": "Student not found"}), 404

# -----------------------------
# Run Flask
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)

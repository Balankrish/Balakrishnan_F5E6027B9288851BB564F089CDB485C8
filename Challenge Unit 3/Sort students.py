class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students):
    return sorted(students, key=lambda student: student.cgpa, reverse=True)


students = [
    Student('Bala', '001', 8.5),
    Student('bhuvaneshwaran', '007', 6.7),
    Student('arun', '002', 8.6),
    Student('krishnan', '005', 9.9),
    Student('gopi krishnan', '006', 9.6),
    Student('gopika', '003', 9.7),
    Student('balan', '004', 5.7),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, Cgpa: {}"

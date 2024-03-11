class Students:
    def __int__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    
    def grade_distribution(self):
        grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        for mark in self.marks:
            if mark >= 90:
                grades['A'] += 1
            elif mark >= 80:
                grades['B'] += 1
            elif mark >= 70:
                grades['C'] += 1
            elif mark >= 60:
                grades['D'] += 1
            else:
                grades['F'] += 1
        return grades
    
def read_student_data():
    students = []
    # Read student data, for example from user input
    # Add each student to the list
    # For demonstration, let's add some sample data
    students.append(Students("Alice", [80, 75, 90]))
    students.append(Students("Bob", [70, 65, 85]))
    students.append(Students("Charlie", [95, 85, 75]))
    return students

# Call the function and print results
students_list = read_student_data()
for student in students_list:
    print(f"Student: {student.name}")
    print(f"Average marks: {student.calculate_average()}")
    print("Grade distribution:", student.grade_distribution())
    print()
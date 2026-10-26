from Demos.win32cred_demo import target
from Student import Student

students = [Student(1,'Adesh',[95,85,90]),
        Student(2, 'Alice',[90,88,91]),
        Student(3,'Bob',[85,84,92]),
        Student(4, 'Smith',[94,92,86]),
        Student(5,'Tony',[98,91,96]),
        ]


#1. Display Students
def display_all_students(student_list):
    print("\n--- All Student Records ---")
    for student in student_list:
        print(student)


# 2. Search by ID
def search_by_id(student_list, rollno):
    print(f"\n--- Search Result for Roll No: {rollno} ---")
    for student in student_list:
        if student.rollno == rollno:
            student.display_student()
            return student
    print(f"Student with Roll No {rollno} not found.")
    return None


# 3. Sort by Name
def sort_by_name(student_list):
    print("\n--- Students Sorted by Name ---")
    sorted_list = sorted(student_list, key=lambda s: s.studentName)
    for student in sorted_list:
        print(student)
    return sorted_list



# 4. Calculate GPA of a student by ID
def calculate_student_gpa(student_list, rollno):
    print(f"\n--- GPA Calculation for Roll No: {rollno} ---")
    for student in student_list:
        if student.rollno == rollno:
            gpa = student.calculate_gpa()
            print(f"Student: {student.studentName} | GPA: {gpa:.2f}")
            return gpa
    print(f"Student with Roll No {rollno} not found.")
    return None

display_all_students(students)
search_by_id(students, 103)
sort_by_name(students)
calculate_student_gpa(students, 102)
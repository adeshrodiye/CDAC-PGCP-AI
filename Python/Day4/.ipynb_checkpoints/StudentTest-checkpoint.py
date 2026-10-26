from Demos.win32cred_demo import target

from Student import Student

list = [Student(1,'Adesh',[95,85,90]),
        Student(2, 'Alice',[90,88,91]),
        Student(3,'Bob',[85,84,92]),
        Student(4, 'Smith',[94,92,86]),
        Student(5,'Tony',[98,91,96]),
        ]
#1. Display Students
for i in list:
    print(i)

#2. Search by id
target = int(input("Enter Roll No:"))
#next(generator, default)
found_student = next((s for s in list if s.roll == target),None)

if found_student:
    print("Found Student:",found_student)
else:
    print("No Student found")
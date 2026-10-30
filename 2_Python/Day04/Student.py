class Student:

    def __init__(self, roll, name, marks):
        self._roll = roll
        self._name = name
        self._marks = marks


    def __str__(self):
        return (f"Student Data : {self._name} - {self._roll} - {self._marks}")

    def calculate_gpa(self):
        m = self._marks
        gpa = (1 / 3)*m[0] + (1 / 2)*m[1] + (1 / 4)*m[2]
        return gpa

    def display_student(self):
        print(self)




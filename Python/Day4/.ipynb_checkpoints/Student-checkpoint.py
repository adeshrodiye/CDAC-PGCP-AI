class Student:

    def __init__(self, roll, name, marks):
        self._roll = roll
        self._name = name
        self._marks = marks


    def __str__(self):
        return (f"Student Data : {self._name} - {self._roll} - {self._marks}")

    def gpa(self, m1,m2,m3):
        return ((1/3)*m1 + (1/2)*m2 + (1/4)*m3)

    @property
    def roll(self):
        return self._roll

    @property
    def name(self):
        return self._name



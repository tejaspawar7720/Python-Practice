class Student:
    def __init__(self, py, m3, java):
        self.py = py
        self.m3 = m3
        self.java = java

    @property
    def percentage(self):
        print((self.py + self.java + self.m3 ) / 3 , "%") 

mark = Student(48,87,64)
mark.percentage        
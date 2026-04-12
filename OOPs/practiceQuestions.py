class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print("Testing decorator :")

    def averag1(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("Hi", self.name,"Your Average Score is ",sum/len(self.marks))


s1 = Student("Tejas",[88, 95, 45, 88, 98 , 78])
s1.hello()
s1.averag1() 
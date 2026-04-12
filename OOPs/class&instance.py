class Student:
    collage_name= "Sandip university"
    def __init__(self, collage_name, marks):
        self.collage_name =  collage_name
        self.marks = marks

    def hel(self):
        print("Welcome to, ", self.collage_name)
    
    def get_marks(self):
        return self.marks

s1 = Student("Ssvps", 85)
s1.hel()
print(s1.get_marks())
 

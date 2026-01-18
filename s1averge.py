class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def averge_marks(self):
        sum = 0
        for mark in self.marks:
         sum += mark
        print("hi", self.name, "your average marks is", sum/3)
        
s1 = Student("Sohail", [85, 90, 78])
print(s1.name, s1.marks)
print(s1.averge_marks())
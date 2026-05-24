class student:
    def __init__(self,marks):
        self.__marks=marks
    def grade(self):
         if self.__marks>=90:
            return "A"
         elif self.__marks>=70:
            return "B"
         elif self.__marks>=50:
            return "C"
         else:
            return "Fail"
s=student(82)
print("marks= ",s._student__marks) 
print("grade= ",s.grade())      
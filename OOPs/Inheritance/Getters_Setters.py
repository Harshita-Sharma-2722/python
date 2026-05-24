class student:
    def __init__(self,name):
        self.__name=name
    def set_name(self,name): #used for update the name
            self.__name=name
    def get_name(self): # used to show the value
            return self.__name
s=student("rahul")
print("name= ",s.get_name())
s.set_name("amit")
print("updated name= ",s.get_name())
            
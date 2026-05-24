class father:
    def drive(self):
        print("driving")
class mother:
    def cook(self):
       print("cooking") 
class daughter(father,mother):
    pass
d=daughter()
d.cook()
d.drive()            
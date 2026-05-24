class grandmother:
    def story(self):
        print("story telling")
class mother(grandmother):
    def cook(self):
        print("cooking")
class daughter(mother):
    def dance(self):
        print("dancing")
d=daughter()
d.story()
d.cook()                        
    
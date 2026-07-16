class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def get_marks(self):
        print(self.__marks)   
    def set_marks(self,new_marks):
        self.__marks=new_marks


student1=Student("Lavish",99)   

# print(student1.name)   
# student1.get_marks()
student1.set_marks(100)
student1.get_marks()
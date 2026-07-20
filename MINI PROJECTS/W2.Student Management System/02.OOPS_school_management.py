from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,id):
        self.name=name
        self.id=id

    @abstractmethod
    def show_details(self):
        pass    
class Student(Person):
    def __init__(self,name,id,age,standard):
        super().__init__(name,id)
        self.age=age
        self.standard=standard
    def show_details(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Age:",self.age)
        print("Standard:",self.standard)
class Teacher(Person):
    def __init__(self,name,id,Subject,Salary):
        super().__init__(name,id)
        self.Subject=Subject
        self.Salary=Salary
    def show_details(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Subject:",self.Subject)
        print("Salary:",self.Salary)
class School:
    def __init__(self):
        self.student=[]
        self.teacher=[]
    def add_student(self,student):
        self.student.append(student)
    def add_teacher(self,teacher):
        self.teacher.append(teacher)
    def show_all_student(self):
        for student in self.student:
            student.show_details()
    def show_all_teacher(self):
        for teacher in self.teacher:
            teacher.show_details()
    def search_student(self,id):
        for student in self.student:
            if student.id==id:
                student.show_details()

school=School()
student1=Student("Lavish", 101, 21, "B.Tech")
student2=Student("Rahul", 102, 20, "BCA")
teacher1=Teacher("Amit Sir", 201, "Python", 50000)
teacher2=Teacher("Riya Ma'am", 202, "Java", 60000)

school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)
school.add_teacher(teacher2)
print("List Of Students")
school.show_all_student()
print("list of Teachers")
school.show_all_teacher()
            

        

        
        
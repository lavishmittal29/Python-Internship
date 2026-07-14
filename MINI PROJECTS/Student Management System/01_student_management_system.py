#Pragram for mini project : Student Management System

#user input details
name=input("Enter Name: ")
age=int(input("Enter Age: "))
city=input("Enter City: ")


#input stored in dictionary
student={
    "Name": name,
    "Age" : age,
    "City": city,
    "Course": "B.Tech CSE (AI)"
}

print("Student Details:",student)

#SUBJECTS in list[]
subjects=["Python","HTML","CSS","SQL"]

#SKILLS in tuple()
skills=("Communication","Leadership","Problem Solving","Management")

#hobbies in sets{}
hobbies={"Music","Coding","Music","Photography"}

#creating fuction()
def show_student():
    print("Student Details:", student)
def show_subject():
    print("List of Subjects",subjects)
def show_skills():
    print("List of Skills:",skills)
def show_hobbies():
    print("Hobbies:",hobbies)

#Eligiblity check for internship using if else...
if age>=18:
    eligibility=("Eligible for Internship")
else:
    eligibility=("Not Eligible")

#calling function 
show_student()
show_subject()
show_skills()
show_hobbies()

#list methods 
subjects.append("Power BI")
print("Subjects list:",subjects)

subjects.insert(1,"Java")
print("Subjects List:",subjects)

subjects.remove("HTML")
print("Subjects List:",subjects)

subjects.pop(-1)
print("Subjects List: ",subjects)

subjects.sort()
print("Sorted Subjects List:",subjects)

subjects.reverse()
print("Reverse Subjects List:",subjects)

#using dictionary methods
student.update({"Phone":8827972224}) 

print("=========================")
print("     STUDENT REPORT      ")
print("=========================")
print("  ")
print(student)
print("  ")
print("Subjects:",subjects)
print("  ")
print("Skills:",skills)
print("  ")
print("Hobbies:",hobbies)
print("  ")
print("Eligibility:",eligibility)
print("  ")
print("=========================")

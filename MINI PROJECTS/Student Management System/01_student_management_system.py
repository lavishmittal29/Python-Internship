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
    print("Eligible for Internship")
else:
    print("Not Eligible")

    
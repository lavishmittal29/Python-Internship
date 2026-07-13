students={
    "Name": "Lavish",
    "Age" : 23,
    "City": "Indore",
    "College": "Parul University"
}

print("Student:",students)
print("Name:",students["Name"])
print("College name:",students["College"])
print("Number of keys:",len(students))

#methods in dictonary 

#methode1 : update()
students.update({"Course":"B.tech CSE (AI)"})
print("updated dic:",students)

#method2 : pop()
students.pop("City")
print("updated dic:",students)

#method3: keys() & value()
print("keys:",students.keys())
print("Value:",students.values())
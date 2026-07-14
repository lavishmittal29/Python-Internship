name="Lavish Mittal"

print("Complete Strings:",name)
print("First Character:",name[0])
print("Last Character:",name[-1])
print("First six Character:",name[0:6])
print("Last Six character:",name[-6:])
print("Total Characters:",len(name))

#string methods 

#using upper()
print("Original:",name)
print("Upper:",name.upper())
print("Original:",name)

#using lower()
print("Originnal:",name)
print("lowercase:",name.lower())
print("Original:",name)

name1="   Lavish Mittal    "
#using strip()
print("Strip string:",name1.strip())

#using replace()
print("Replacing words:",name.replace("Lavish","Navneet"))

#using find()
print("Index value of Mittal:",name.find("Mittal"))

#using count()
print("count:",name.count("a"))

#using split()
print("STRING TO LIST:",name.split())
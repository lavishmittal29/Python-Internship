fruits={"apple","mango","banana","apple","orange","banana"}

print("fruits name:",fruits)
print("TOTAL COUNT: ",len(fruits))

#using set moethods (add()).....
fruits.add("kiwi")
print("updated set:",fruits)
print("totol number of fruits:",len(fruits))

#menthod2 : remove()
fruits.remove("mango")
print("updated set:",fruits)
print("totol number of fruits:",len(fruits))

#method3: discard()
fruits.discard("papaya")

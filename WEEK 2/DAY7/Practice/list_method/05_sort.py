numbers=[12,45,78,66,95,75,35,16]

print('original list:',numbers)
numbers.sort()
print("Sorted List of number:", numbers)
print("smallest number:",min(numbers))
print("largest number:",max(numbers))
#decending order
numbers.sort(reverse=True)
print("Decending order of list:",numbers)
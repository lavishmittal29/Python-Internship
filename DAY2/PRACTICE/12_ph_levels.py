# program to anaylze the ph level of a solution
ph_level = float(input("Enter the ph level of the solution: "))
if ph_level < 7:
    print("The solution is acidic.")
elif ph_level == 7:
    print("The solution is neutral.")
else:
    print("The solution is basic.")        
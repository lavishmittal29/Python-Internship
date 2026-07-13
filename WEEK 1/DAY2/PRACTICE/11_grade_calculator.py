# Program to calculate the grade of a student based on marks.
marks=int(input("Enter the marks: "))
if marks==100:
    print("Grade: O (Outstanding)")
elif marks>=95:
    print("Grade: A+ (Excellent)")
elif marks>=90:
    print("Grade: A (Very Good)")
elif marks>=80:
    print("Grade: B (Good)")
elif marks>=70:
    print("Grade: C (Average)")
elif marks>=60:
    print("Grade: D (Below Average)")
elif marks>=50:
    print("Grade: E (Poor)")
elif marks>=40:
    print("Grade: P (Pass)")  
elif marks<40 and marks>=0:
    print("Grade: F (Fail)")
else:
    print("Invalid marks entered. Please enter a valid number between 0 and 100.")        
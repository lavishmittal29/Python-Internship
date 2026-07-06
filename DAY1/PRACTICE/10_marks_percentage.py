# marks and percentage calculation
marks_subject1 = float(input("Enter marks obtained in subject 1: "))
marks_subject2 = float(input("Enter marks obtained in subject 2: "))
marks_subject3 = float(input("Enter marks obtained in subject 3: "))
marks_subject4 = float(input("Enter marks obtained in subject 4: "))
total_marks = marks_subject1 + marks_subject2 + marks_subject3 + marks_subject4
percentage =(total_marks / 400) * 100
print("Total marks obtained:", total_marks)
print("Percentage:", percentage, "%")
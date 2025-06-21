student1_marks = int(input("Enter the marks of student 1: "))
student2_marks = int(input("Enter the marks of student 2: "))
student3_marks = int(input("Enter the marks of student 3: "))
total_marks = student1_marks + student2_marks + student3_marks
average_marks = total_marks / 3
if average_marks >= 85:
    print('student passed')
else:
    print('student failed')
    
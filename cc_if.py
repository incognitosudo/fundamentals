#Grading system for students
gradeToTest = input("Input Student Grade 0-100: ")

if gradeToTest =="100":
    print("A+")
elif gradeToTest >= "90":
    print("A")
elif gradeToTest >= "80":
    print("B")
elif gradeToTest >= "70":
    print("C")
elif gradeToTest >= "60":
    print("D") 
else:
    print("F")

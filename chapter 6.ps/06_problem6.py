marks = int(input("Enter your marks:"))

if(marks<=100 and marks >=90):
    grade = "A"

elif(marks<=90 and marks >=80):
    grade = "B"
elif(marks<=80 and marks >=70):
    grade = "C"
elif(marks<=70 and marks >=60):
    grade = "D"
elif(marks<=60 and marks >=50):
    grade = "E"
elif(marks<50):
    grade = "F"

print("If your grade is :" , grade)






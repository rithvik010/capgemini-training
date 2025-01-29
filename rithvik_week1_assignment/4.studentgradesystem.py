student_name=input("Enter student name : ")
subject1=int(input("enter subject 1 marks "))
subject2=int(input("enter subject 2 marks "))
subject3=int(input("enter subject 3 marks "))
subject4=int(input("enter subject 4 marks "))
subject5=int(input("enter subject 5 marks "))
add=subject1+subject2+subject3+subject4+subject5

avg=add/5
if avg>40 and avg<60:
    print(f"{student_name} scored {add} out of 500 and grade is C")
elif avg>60 and avg<80:
    print(f"{student_name} scored {add} out of 500 and grade is B")
elif avg>80:
    print(f"{student_name} scored {add} out of 500 and grade is A")
else:
    print("{student_name} scored {add} out of 500 and failed")


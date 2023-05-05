num=int(input("Enter number of students: "))
student_ls=[]

for i in range(1,num+1):
    student_ls.append(input(f"Enter name for student {i}: "))

print("Sorted list: ", sorted(student_ls))
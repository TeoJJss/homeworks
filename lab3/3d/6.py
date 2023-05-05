name=input("Enter the student's name: ")
tp=input("Enter the student's TP number: ")
mark_ls=[]

for i in range(1,6):
    mark_ls.append(int(input(f"Enter the mark for Subject {i}: ")))

print("Student Name:",name)
print("TP Number:",tp)
print("Total Marks:",sum(mark_ls))
perc=sum(mark_ls)/5
print(f"Percentage: {perc}%")

print("Grade: ", end="")
if perc>=80:
    print("A")
elif perc>=70:
    print("B")
elif perc>=60:
    print("C")
elif perc>=50:
    print("D")
else:
    print("F")
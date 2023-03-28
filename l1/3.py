# Get Student name and mark, and calculate average mark

names=[]
marks=[]
 
# Input
for i in range(10):
    print("Student", i+1)
    name=input("Please input name: ")
    mark=int(input(f"Please input mark for {name}: "))
    names.append(name)
    marks.append(mark)

#Display each name and mark
print(",".join(names))


#Display average
print(f"Average: {sum(marks) / len(marks)}")
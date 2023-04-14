num=int(input("How many students? "))
marks=[]

for i in range(num):
    print(f"Student {i+1}")
    name=input("Name: ")
    mark=int(input("Mark: "))
    if name and mark in range(101):
        marks.append(mark)

print(sum(marks)/len(marks))
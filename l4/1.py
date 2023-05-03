name=input("Enter a name: ")
first=0
middle=len(name)//2 
last=len(name)-1

for i in range(len(name)):
    if i in [first,middle,last]:
        print(name[i], end="")
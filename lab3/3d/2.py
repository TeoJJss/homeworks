size=int(input("Enter size: "))
ls=[]

for i in range(size):
    ls.append(int(input(f"Enter integer {i+1}:")))

for i in ls:
    print(i)

print("The sum is",sum(ls))
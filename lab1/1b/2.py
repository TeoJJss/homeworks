total=tmp=0

for i in range(5):
    tmp=float(input(f"Number {i+1}: "))
    total+=tmp
print("Average: "+str(total/5))
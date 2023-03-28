total=tmp=0

for i in range(5):
    tmp=int(input(f"Number {i+1}: "))
    total+=tmp

print(f"Average: {total/5}")
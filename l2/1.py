total=tmp=0

for i in range(3):
    tmp=int(input(f"Number {i+1}: "))
    total+=tmp

print(f"Sum: {total}")

# print(sum([int(input(f"number {i+1}: ")) for i in range(3)]))
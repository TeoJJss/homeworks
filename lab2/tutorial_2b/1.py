num=int(input("Number: "))
ls=[str(x) for x in range(1, num+1)]

print("The first 7 natural number is: \n" + " ".join(ls))
print(f"The Sum of Natural Number upto {num} terms:",sum(map(int, ls)))
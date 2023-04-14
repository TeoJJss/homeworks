num=int(input("Num: ")) # Ask user for input
power=int(input("To the power of: "))

ans=1
for i in range(power):
    ans*=num

print(ans)
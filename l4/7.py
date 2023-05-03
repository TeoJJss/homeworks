str1="Bye 2022 and welcome 2023"

sum=count=0

for i in str1:
    if i.isnumeric():
        count+=1
        sum+=int(i)

print(f"Sum is: {sum} Average is {sum/count}")
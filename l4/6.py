str1 = "Welcome to APU, APU Uni, Kuala Lumpur, Malaysia"
str2 ="APU"
count=0

for i in range(len(str1)):
    if str1[i:i+3]==str2:
        count+=1

print("The APU count is",count)
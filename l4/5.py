str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
j=1
for i in str1:
    print(i, str2[-j])
    j+=1
